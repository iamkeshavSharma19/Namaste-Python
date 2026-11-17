Let me simplify it. There is only **one idea** behind all of this:

> Every `companies[1:2]` creates a **new list**. The only question is whether the previous list is still alive when the new one is created.

## Part 1: Four lines, no variables

**Line 1:** `print(id(companies[1:2]))`
- A new list is created, say at address **X**.
- `id()` gives X, and it is printed.
- Nobody is holding the list, so Python deletes it. **X is free again.**

**Line 2:** `print(id(companies[1:2]))`
- Another new list is created. X was just freed, so it often lands on **X again**.
- You see the **same number**, but it is a different object that reused the spot.

**Line 3:** `print(companies[1:2] == companies[1:2])` → **True**
- `==` compares **values**, not addresses.
- Both lists contain `['Tech Mahindra']`, so the result is True.

**Line 4:** `print(companies[1:2] is companies[1:2])` → **False**
- `is` asks "are these the same object?"
- Both lists are created and must **exist at the same time** for the comparison, so they cannot share an address.
- Result: False.

## Part 2: With variables

```python
a = companies[1:2]
print(id(a))     # address A
b = companies[1:2]
print(id(b))     # address B
c = companies[1:2]
print(id(c))     # address C
```

- `a` holds the first list, so it stays alive and its address is **not freed**.
- The second list cannot use A, so it gets **B**. The same happens with **C**.
- You see **three different numbers**.

## Why Part 1 and Part 2 look different

| Situation | Is the old list still alive? | Result |
|---|---|---|
| Part 1, `id()` on separate lines | No, deleted right after printing | Often the same id |
| Part 1, `is` in one expression | Yes, both exist together | Always False |
| Part 2, stored in `a`, `b`, `c` | Yes, variables hold them | Always different ids |

## What `==` and `is` mean

- `==` asks: **do they have the same content?** (True here)
- `is` asks: **are they the same object in memory?** (False here)

Two separate lists can have the same content but still be different objects, just like two photocopies of the same page.

## The one rule

> **Alive together → different addresses.**
> **One dies before the other is born → they may share an address.**

The same id in Part 1 does **not** mean Python returned the same list. It means the memory spot was reused after the first list was deleted.