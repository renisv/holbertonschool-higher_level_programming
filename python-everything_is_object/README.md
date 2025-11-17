# Python3: Mutable, Immutable... Everything is Object!

![Python Objects](https://miro.medium.com/max/1400/1*2wP28GnHQJREMqc4Bl

Python treats everything as an object, each with an identity, type, and value. Understanding the distinction between mutable and immutable objects is crucial for writing efficient and bug-free Python code. In this post, I share fundamental concepts about objects, their mutability, and how Python handles them, along with examples that illustrate these ideas.

## id and type

Every Python object has a unique identity which can be obtained via the `id()` function. The `type()` function reveals the object's type.

Example:

```python
a = [1, 2, 3]
print(id(a))        # e.g. 139847293847
print(type(a))      # <class 'list'>
```

This identity is akin to the object's memory address and shows that even if two objects look equal, they might not be the same object.

## Mutable Objects

Mutable objects allow their contents to be changed without changing their identity. Common examples include lists, dictionaries, and sets.

```python
a = [1, 2, 3]
print(id(a))       # 139847293847
a.append(4)
print(id(a))       # same id, object modified in place
print(a)           # [1, 2, 3, 4]
```

Here, `a` remains the same object even after modification.

## Immutable Objects

Immutable objects cannot be changed once created. Any operation that would alter them creates a new object. Examples include integers, floats, strings, and tuples.

```python
s = "Hello"
print(id(s))       # 123456789
s = s + " World"
print(id(s))       # different id, new object created
print(s)           # "Hello World"
```

## Why Does Mutability Matter?

Python treats mutable and immutable objects differently because of their underlying behavior:

- Mutable objects can be changed in place.
- Immutable objects require reallocation on changes (new object created).

It affects how variables reference objects and how operations on these objects behave during assignment and function calls.

## How Arguments Are Passed to Functions

Python passes arguments by object reference. The behavior differs based on mutability:

- For immutable objects, reassigning inside functions doesn't alter the original object.
- For mutable objects, changes inside functions affect the same object outside.

Examples:

```python
def increment(n):
    n += 1
a = 1
increment(a)
print(a)  # Output: 1 (immutable, original unchanged)
```

```python
def add_element(lst):
    lst.append(4)
l = [1, 2, 3]
add_element(l)
print(l)  # Output: [1, 2, 3, 4] (mutable, original modified)
```

## Advanced Learnings

Through challenges and tasks, I deepened my grasp on object identity (`is`), equality (`==`), and how assignment and operations like `+` and `+=` influence mutable and immutable types differently. For example, concatenation with `+` creates new list objects, whereas `+=` modifies lists in-place.

Understanding these nuances helps write more predictable Python programs, avoid bugs related to unexpected mutations, and better optimize memory usage.

***

I published this article on [Medium](#) and shared on [LinkedIn](#).

***

This blog covers foundational and advanced insights into Python’s object model, demonstrating the intricate and elegant design of Python’s type and memory management system.

[1](https://www.geeksforgeeks.org/python/mutable-vs-immutable-objects-in-python/)
[2](https://realpython.com/python-mutable-vs-immutable-types/)
[3](https://datasciencedojo.com/blog/mutable-and-immutable-objects-in-python/)
[4](https://unstop.com/blog/mutable-and-immutable-in-python)
[5](https://stackoverflow.com/questions/4828080/how-to-make-an-immutable-object-in-python)
[6](https://docs.python.org/3/reference/datamodel.html)
[7](https://www.youtube.com/watch?v=l5TLtKxga5E)
[8](https://www.reddit.com/r/learnpython/comments/163dw52/mnemonic_for_remembering_mutable_and_immutable/)
