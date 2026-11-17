The two parts behave differently for two different reasons.

## Part 1: `z = 1` gives the same id

```python
z = 1
print(id(z))
z = 1
print(id(z))
```

CPython pre-creates and caches small integers (from -5 to 256). There is only **one** `1` object in the whole program, and every `1` you write points to it. So the id is the same, and it is the same object, not a reused address.

```python
a = 1
b = 1
print(a is b)   # True
```

(Large numbers like `1000` are not guaranteed to work this way. Don't rely on it.)

## Part 2: `k = [1, 2]` gives different ids

```python
k = [1, 2]
print(id(k))     # address A
k = [1, 2]
print(id(k))     # address B (different)
```

A list literal creates a **new list object every time**, because lists are mutable and Python can't share them. The order of events on the second line matters:

1. Python evaluates the right side first and **creates a new list**. At this moment `k` still points to the old list, so the old list is **alive**.
2. The new list cannot take address A, because the old list is still sitting there, so it gets address **B**.
3. Only then is the name `k` re-pointed to the new list.
4. The old list now has no references, so it is deleted and address A becomes free.

This is the "alive together, so different addresses" rule again. The new list was created while the old one still existed.

If you add a third assignment, it may land back on **A**, because A was freed in the meantime:

```python
k = [1, 2]   # A
k = [1, 2]   # B
k = [1, 2]   # often A again
```

## Summary

| Code               | Objects created         | Why the id looks like this                                            |
| ------------------ | ----------------------- | --------------------------------------------------------------------- |
| `z = 1` twice      | None new, `1` is cached | Same object, same id                                                  |
| `k = [1, 2]` twice | A new list each time    | Old list is still alive when the new one is created, so different ids |

Immutable small values like `1` can be shared safely, but mutable objects like lists must always be separate.
