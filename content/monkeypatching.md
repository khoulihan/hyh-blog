Title: Runtime Class Modification
Date: 2020-03-25 17:51
Modified: 2020-03-25 23:12
Category: Programming
Tags: python, micropython
Slug: runtime-class-modification
Authors: Kevin Houlihan
Summary: Batteries-included package development in Python requires an unorthodox approach when targeting microcontrollers.
Status: published

Python is probably my favourite language, so I was excited some years ago when a project appeared on Kickstarter to develop a [Python runtime for microcontrollers](http://micropython.org/ "MicroPython"), and an associated microcontroller board.

However, writing Python for a microcontroller does have some constraints that aren't really a factor when writing Python for other environments. Having maybe only 100KB of RAM to work with, keeping code size as low as possible is essential.

When I wrote a [package to support the TI tmp102 temperature sensor](https://github.com/khoulihan/micropython-tmp102 "micropython-tmp102 repository"), I initially included all the required functionality in a single importable class. It used 15KB of RAM after import, which does leave space for other code, but since some of the functionality is mutually exclusive I knew I could probably do better.

This post is about what I ended up with and how it works.

## Importable Features

The core functionality of the package can be leveraged by importing the `Tmp102` class and creating an instance. This leaves the sensor in its default configuration, in which it performs a reading 4 times per second and makes the most recent available to your code on request. The details of initialising the object are explained in the [documentation](https://github.com/khoulihan/micropython-tmp102/blob/master/README.md) if you actually want to use the module, so I won't go into them again here.

```python
from machine import I2C
from tmp102 import Tmp102
bus = I2C(1)
sensor = Tmp102(bus, 0x48)
print(sensor.temperature)
```

That's all well and good, but what if you want to make use of some of the more advanced features of the sensor, such as controlling the rate at which it takes readings (the "conversion rate")? Such features are structured as importable modules which add the required functionality into the `Tmp102` class. The `CONVERSION_RATE_1HZ` constant in the example below, as well as other relevant code, are added to the class when the `conversionrate` module is imported.

```python
from tmp102 import Tmp102
import tmp102.conversionrate
sensor = Tmp102(
    bus,
    0x48,
    conversion_rate=Tmp102.CONVERSION_RATE_1HZ
)
```

If you don't need to change the conversion rate in your project then the code to do so is never loaded. If you do need this or other features, all the functionality is still exposed through a single easy to use class.

## How?

The package is structured like this:

```text
tmp102
+-- __init__.py
+-- _tmp102.py
+-- alert.py
+-- conversionrate.py
+-- convertors.py
+-- extendedmode.py
+-- oneshot.py
+-- shutdown.py
```

The base `Tmp102` class is defined in `_tmp102.py`, along with some private functions and constants.

```python
REGISTER_TEMP = 0
REGISTER_CONFIG = 1

EXTENDED_MODE_BIT = 0x10

def _set_bit(b, mask):
    return b | mask

def _clear_bit(b, mask):
    return b & ~mask

def _set_bit_for_boolean(b, mask, val):
    if val:
        return _set_bit(b, mask)
    else:
        return _clear_bit(b, mask)


class Tmp102(object):

    def __init__(self, bus, address, temperature_convertor=None, **kwargs):
    	    self.bus = bus
        self.address = address
        self.temperature_convertor = temperature_convertor
        # The register defaults to the temperature.
        self._last_write_register = REGISTER_TEMP
        self._extended_mode = False
        .
        .
        .
```

To hide the private stuff from users of the package, the `__init__.py` imports the `Tmp102` class and then removes the `_tmp102` module from the namespace.

```python
from tmp102._tmp102 import Tmp102

del _tmp102
```

The interesting stuff happens in the feature sub-modules. Each feature module defines an `_extend_class` function which modifies the `Tmp102` class. Since importing a module runs it, this function can be called and then deleted to keep the namespace nice and clean - the module will actually be empty once imported. This pattern should be familiar to JavaScript developers!

```python
def _extend_class():
    # Modify Tmp102 here - Check the next code block!
    pass

_extend_class()
del _extend_class
```

Let's take a look at the `oneshot` module, which adds functionality to the `Tmp102` class to allow the sensor to be polled as necessary instead of constantly performing readings - very useful if you want to save power.

```python
def _extend_class():
    from tmp102._tmp102 import Tmp102
    from tmp102._tmp102 import _set_bit_for_boolean
    import tmp102.shutdown

    SHUTDOWN_BIT = 0x01
    ONE_SHOT_BIT = 0x80

    def initiate_conversion(self):
        """
        Initiate a one-shot conversion.
        """
        current_config = self._get_config()
        if not current_config[0] & SHUTDOWN_BIT:
            raise RuntimeError("Device must be shut down to initiate one-shot conversion")
        new_config = bytearray(current_config)
        new_config[0] = _set_bit_for_boolean(
            new_config[0],
            ONE_SHOT_BIT,
            True
        )
        self._set_config(new_config)
    Tmp102.initiate_conversion = initiate_conversion

    def _conversion_ready(self):
        current_config = self._get_config()
        return (current_config[0] & ONE_SHOT_BIT) == ONE_SHOT_BIT
    Tmp102.conversion_ready = property(_conversion_ready)
```

So what's going on here? First, the `Tmp102` class and any required functions are imported. Since it was imported in the package's `__init__` the class is already defined. Importing the private functions and constants in a function like this keeps them out of the global namespace.

```python
from tmp102._tmp102 import Tmp102
from tmp102._tmp102 import _set_bit_for_boolean
```

The `oneshot` module depends on the functionality from the `shutdown` module, so it is imported next.

```python
import tmp102.shutdown
```

Next, a couple of constants are defined. Through the magic of closure, these will only be available to the methods defined in this module.

```python
SHUTDOWN_BIT = 0x01
ONE_SHOT_BIT = 0x80
```

The rest of the function a method and a property which are added to the class by simply assigning them to attributes. These will be available to any instances of the class, exactly as if they were included in the class definition.

```python
def initiate_conversion(self):
    """
    Initiate a one-shot conversion.
    """
    current_config = self._get_config()
    if not current_config[0] & SHUTDOWN_BIT:
        raise RuntimeError("Device must be shut down to initiate one-shot conversion")
    new_config = bytearray(current_config)
    new_config[0] = _set_bit_for_boolean(
        new_config[0],
        ONE_SHOT_BIT,
        True
    )
    self._set_config(new_config)
Tmp102.initiate_conversion = initiate_conversion

def _conversion_ready(self):
    current_config = self._get_config()
    return (current_config[0] & ONE_SHOT_BIT) == ONE_SHOT_BIT
Tmp102.conversion_ready = property(_conversion_ready)
```

The other feature modules follow the same pattern.

## Savings

Importing the base `Tmp102` class uses about 3.53KB of RAM - quite a saving if that is all you need. The feature modules vary between 0.8KB and 4KB, or thereabouts. Importing them all uses 13.44KB, but it is unlikely that they would all be required in any given application.

## Conclusion

I thought of this approach as "monkey-patching" for a long time - the last refuge of the desperate and the damned - but I'm not sure that it is really, because the modifications are all being made internally to the package. It is definitely outside the norm for Python, but it achieved the goal of reducing RAM usage while maintaining a clean API.