Aapke code mein `companies` define nahi hai, toh main assume kar raha hoon:

```python
companies = ["TCS", "Tech Mahindra", "Infosys"]
```

## Line by line

**1. `tech_mahindra = companies[1:2]`**

Slicing hamesha ek **naya list object** banata hai. Yeh `companies` ke index 1 se 2 se pehle tak ka element copy karke ek alag list banata hai:

```
companies      -> ["TCS", "Tech Mahindra", "Infosys"]   (address A)
tech_mahindra  -> ["Tech Mahindra"]                      (address B)
```

Dono alag objects hain, bas andar ki string same hai.

**2. `print(id(companies))` aur `print(id(tech_mahindra))`**

`id()` object ka memory identity batata hai. Dono ke **alag** number aayenge (A aur B), kyunki dono alag lists hain.

**3. `print(id(companies[1:2]))`**

Yahan Python phir se ek **nayi temporary list** banata hai. Pichli list `tech_mahindra` abhi zinda hai, toh yeh teesre address (C) par banegi. Isliye yeh `id(tech_mahindra)` se bhi alag aayega. Print hone ke baad yeh temporary list delete ho jaati hai.

**4. `companies[1:2] = "Wipro"`** (yahi asli gotcha hai)

Yahan slice **assignment** ho raha hai, jo original list ko **in-place modify** karta hai. Python right side ko iterable maanta hai, aur string iterable hoti hai, toh woh characters mein toot jaati hai: `'W','i','p','r','o'`.

Index 1 ka ek element hata kar yeh 5 characters daal diye jaate hain:

```python
['TCS', 'W', 'i', 'p', 'r', 'o', 'Infosys']
```

`["TCS", "Wipro", "Infosys"]` nahi milta.

**5. `print(id(companies))`**

Pehle jaisa hi number aayega (A), kyunki list ko naya object banaye bina usi object mein badla gaya hai. Slice assignment object ko mutate karta hai, replace nahi karta.

**6. `print(tech_mahindra)` aur `print(id(tech_mahindra))`**

```python
['Tech Mahindra']   # same B address
```

`tech_mahindra` slicing se bani ek **independent copy** thi, isliye `companies` mein jo bhi change hua uska is par koi asar nahi padta. Value aur id dono wahi rahenge.

## Key takeaways

| Cheez | Kya hota hai |
|---|---|
| `a[1:2]` (read) | Naya list object banta hai (shallow copy) |
| `a[1:2] = ...` (write) | Original list in-place badalti hai, id same rehti hai |
| `= "Wipro"` | String ke har character ko alag element bana deta hai |

## Sahi tarika

```python
companies[1:2] = ["Wipro"]   # list dena zaroori hai
# ya simply
companies[1] = "Wipro"
```

Dono se `['TCS', 'Wipro', 'Infosys']` milega.

Agar aap chaho toh main `is` operator aur shallow vs deep copy ke saath yeh concept aur clear kar sakta hoon.


Chalo is line ko step by step samajhte hain.

## Iterable kya hota hai?

**Iterable** woh cheez hoti hai jisme se aap **ek-ek karke items nikal sakte ho** (loop chala sakte ho).

Simple example: `for` loop.

```python
for x in ["a", "b", "c"]:
    print(x)
```

Output: `a`, `b`, `c` alag-alag aayenge. Matlab list iterable hai.

Python mein common iterables:

| Type | Example | Ek-ek karke kya milta hai |
|---|---|---|
| list | `["TCS", "Wipro"]` | "TCS", "Wipro" |
| tuple | `(1, 2, 3)` | 1, 2, 3 |
| **string** | `"Wipro"` | 'W', 'i', 'p', 'r', 'o' |
| range | `range(3)` | 0, 1, 2 |
| dict | `{"a": 1}` | keys |

Not iterable: `5` (int). `for x in 5:` karoge toh error aayega.

## String bhi iterable hai

Yeh point beginners ko confuse karta hai. String sirf ek "word" nahi hai, Python usse **characters ki sequence** maanta hai:

```python
for ch in "Wipro":
    print(ch)
```

Output:
```
W
i
p
r
o
```

## Ab asli line ka matlab

```python
companies[1:2] = "Wipro"
```

Slice assignment mein Python right side se kehta hai: "mujhe **iterable** de, main uske **ek-ek item** ko list mein daal dunga."

Aapne `"Wipro"` diya. Python ne usse iterate kiya aur 5 items mile: `'W'`, `'i'`, `'p'`, `'r'`, `'o'`. Phir un 5 items ko index 1 wali jagah par daal diya:

```python
['TCS', 'W', 'i', 'p', 'r', 'o', 'Infosys']
```

## Comparison

```python
companies[1:2] = "Wipro"     # string -> iterate hoga -> 5 alag characters
companies[1:2] = ["Wipro"]   # list -> iterate hoga -> 1 item: "Wipro"
```

Dusre case mein list ke andar sirf ek item hai ("Wipro" poora), isliye wahi insert hota hai. Isi wajah se maine kaha tha ki **list dena zaroori hai**.

## Yaad rakhne ka trick

Slice assignment (`a[x:y] = ...`) ke right side par hamesha **iterable** chahiye, aur Python usse khol kar uske items daalta hai. String ko woh "ek item" nahi, "characters ka collection" dekhta hai.

Agar chaho toh main `list("Wipro")` aur `extend()` ke examples bhi dikha sakta hoon, wahi same concept wahan bhi kaam karta hai.


Bahut accha sawaal hai, yeh exactly wahi confusion hai jo is example ka asli point hai. Jawab: **`companies[1:2]` ka matlab position ke hisaab se badalta hai** (left side ya right side).

## Do alag situations

**Right side / expression mein (read karna):**
```python
tech_mahindra = companies[1:2]
```
Yahan Python kehta hai: "slice ke items **nikaal ke** ek naya list bana do." Isliye new object banta hai.

**Left side par (assignment):**
```python
companies[1:2] = "Wipro"
```
Yahan Python kehta hai: "`companies` ke is hisse ko **replace** kar do." Yahan koi naya list nahi banti, kyunki Python `companies[1:2]` ko evaluate hi nahi karta. Woh seedha `companies` object ko bolta hai: "tu apne index 1 se 2 ke beech ka hissa badal le."

## Andar kya hota hai

Python in dono ko alag special methods se chalata hai:

```python
x = companies[1:2]        # companies.__getitem__(slice(1, 2))  -> naya list return karta hai
companies[1:2] = "Wipro"  # companies.__setitem__(slice(1, 2), "Wipro")  -> companies ko hi modify karta hai
```

- `__getitem__` ek value **return** karta hai (naya list).
- `__setitem__` kuch return nahi karta, bas `companies` ko **andar se badal deta hai**.

## Analogy

Socho `companies` ek notebook hai.

- **Read:** `companies[1:2]` = notebook ke page 2 ki **photocopy** nikalna. Photocopy alag cheez hai, usse kuch bhi karo, notebook par asar nahi.
- **Write:** `companies[1:2] = ...` = notebook ke page 2 par **seedha likhna/mita ke badalna**. Notebook khud badal gayi.

## Isi liye output aisa tha

```python
tech_mahindra = companies[1:2]   # photocopy (alag list, B)
companies[1:2] = "Wipro"         # original notebook mein edit (A, same id)
print(id(companies))             # A, wahi purana
print(tech_mahindra)             # ['Tech Mahindra'], photocopy par koi asar nahi
```

## Ek line mein

> Slice **read** karo toh copy milti hai, slice par **assign** karo toh original list edit hoti hai.

Same logic `del companies[1:2]` par bhi lagta hai: yeh bhi original list se element hata deta hai, koi copy nahi banata.


