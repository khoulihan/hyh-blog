Title: Bad Idioms
Date: 2020-01-10 14:11
Modified: 2020-03-25 23:20
Category: Programming
Tags: python, c-sharp
Slug: bad-idioms
Authors: Kevin Houlihan
Summary: A brief investigation of Python's EAFP idiom applied to C#.

Human languages are full to the brim with idioms - figurative ways of saying things that native speakers trot out without even thinking about them. Often, when translated literally into another language, the result is utter nonsense. For example, the phrase "tomar el pelo" in Spanish translates literally to English as "to take the hair", but the idiomatic way to say the same thing in English would be "to pull (someone's) leg". The same thing is roughly true of programming languages, with different languages having their own idiomatic or expected ways of achieving the same ends.

I recently made the mistake, after a period of writing Python code, of applying one of Python's idioms to C#. The task at hand was to check if a dictionary of lists already contained a particular key, and if not, add a new list for that key. The C# way to do this would probably be to check for the existence of the key first, then decide what to do - or even better, use the `TryGetValue` method of the dictionary to assign the value to a variable. This is known as "Look Before You Leap".

```csharp
List<object> l;
if (dict.ContainsKey(objectType))
{
    l = dict[objectType];
}
else
{
    l = new List<object>();
    dict.Add(objectType, l);
}
```

```csharp
List<object> l;
if (!dict.TryGetValue(objectType, out l))
{
    l = new List<object>();
    dict.Add(objectType, l);
}
```

But instead of doing either of those things, I applied a more pythonic idiom - that of "Easier to Ask Permission than Forgiveness" - and just tried retrieving the value, and catching the `KeyNotFoundException`:

```csharp
List<object> l;
try
{
    l = dict[objectType];
}
catch (KeyNotFoundException ex)
{
    l = new List<object>();
    dict.Add(objectType, l);
}
```

This turned an operation that should have taken milliseconds into one that was taking seconds, introducing a perceptible delay into my application.

Curious to know to exactly what extent performance differed between the above choices, and whether EAFP really would have been the better choice in Python, I decided to throw together some benchmark tests.

## Python

```python
import timeit

setup = """
d = {
    'a': [1, 2, 3,],
    'b': [4, 5, 6,],
    'c': [7, 8, 9,],
}
"""

test_except = """
try:
    v = d['d']
except KeyError:
    v = []
    d['d'] = v

del d['d']
"""

test_check = """
if 'd' in d:
    v = d['d']
else:
    v = []
    d['d'] = v

del d['d']
"""

print(timeit.timeit(setup=setup, stmt=test_except, number=1000000))
print(timeit.timeit(setup=setup, stmt=test_check, number=1000000))
```

This gave results of 0.46 seconds for a million EAFP operations, and about 0.08 seconds for a million LBYL operations, with everything else, I hope, being equal between the two tests. If the new key is not deleted every time (so that only the first check fails), the EAFP operation becomes marginally faster than the alternative (0.026 vs 0.037 seconds) on most runs.

## C\#

```csharp
Dictionary<string, List<string>> dict = new Dictionary<string, List<string>>()
{
    { "a", new List<string>() },
    { "b", new List<string>() },
    { "c", new List<string>() }
};

DateTime exceptStart = DateTime.UtcNow;
for (int i = 0; i < 1000; i++)
{
    List<string> v;
    try
    {
        v = dict["d"];
    }
    catch (KeyNotFoundException ex)
    {
        v = new List<string>();
        dict.Add("d", v);
    }
    dict.Remove("d");
}
TimeSpan exceptResult = DateTime.UtcNow - exceptStart;

DateTime tryGetStart = DateTime.UtcNow;
for (int i = 0; i < 1000000; i++)
{
    List<string> v;
    if (!dict.TryGetValue("d", out v))
    {
        v = new List<string>();
        dict.Add("d", v);
    }
    dict.Remove("d");
}
TimeSpan tryGetResult = DateTime.UtcNow - tryGetStart;

DateTime checkStart = DateTime.UtcNow;
for (int i = 0; i < 1000000; i++)
{
    List<string> v;
    if (!dict.ContainsKey("d"))
    {
        v = new List<string>();
        dict.Add("d", v);
    }
    else
    {
        v = dict["d"];
    }
    dict.Remove("d");
}
TimeSpan checkResult = DateTime.UtcNow - checkStart;

Console.WriteLine("Except: {0}", exceptResult.TotalSeconds);
Console.WriteLine("TryGet: {0:f10}", tryGetResult.TotalSeconds);
Console.WriteLine("Check: {0:f10}", checkResult.TotalSeconds);
Console.ReadKey(true);
```

Note that the EAFP test here is only performed a thousand times - because even running it that many times takes around 15 *entire* seconds! The two LBYL tests are nothing in comparison, executing a million times in around 0.05 seconds. This is a much bigger difference than I would have expected.

## Conclusion

The performance of a single operation like this doesn't necessarily say a lot about the real-world performance of any given application, but I think it is probably best to stick to the idioms of the language you're working in - and in C#, that means only throwing exceptions in exceptional circumstances. In Python, there may be circumstances where it would be better to "Look Before You Leap" as well, but the difference in performance is probably not large enough to matter in most cases.