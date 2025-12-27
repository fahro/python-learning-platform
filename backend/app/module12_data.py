MODULE_12_LESSONS = [
    {"title": "Uvod u NumPy", "order": 1, "duration_hours": 1, 
     "content": """# 📊 NumPy - Numerički Python

## Šta je NumPy?
NumPy (Numerical Python) je fundamentalna biblioteka za naučno računanje u Pythonu.

## Zašto NumPy?
- ⚡ **Brzina** - Do 50x brži od Python lista
- 🧮 **Vektorske operacije** - Bez petlji
- 📐 **Matematičke funkcije** - Bogata kolekcija
- 💾 **Efikasna memorija**

## Instalacija
```bash
pip install numpy
```

## Kreiranje Array-a
```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)  # int64
print(arr.shape)  # (5,)
```
""",
     "code_example": """import numpy as np

# Kreiranje arraya
arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")
print(f"Tip: {type(arr)}")
print(f"Shape: {arr.shape}")
print(f"Dtype: {arr.dtype}")
print(f"Ndim: {arr.ndim}")
print(f"Size: {arr.size}")

# 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\\n2D Array:\\n{arr2d}")
print(f"Shape: {arr2d.shape}")

# Operacije
print(f"\\narr * 2 = {arr * 2}")
print(f"arr + 10 = {arr + 10}")
print(f"arr ** 2 = {arr ** 2}")""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Kreiranje Arraya
Kreirajte numpy array [10, 20, 30, 40, 50] i ispišite njegov dtype.

### Vježba 2: 2D Array
Kreirajte 2D array [[1,2,3], [4,5,6]] i ispišite shape.

### Vježba 3: Atributi
Kreirajte array od 1 do 5 i ispišite size i ndim.""",
     "exercise_solution": """# Vježba 1
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(f"Dtype: {arr.dtype}")

# Vježba 2
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Shape: {arr2d.shape}")

# Vježba 3
arr = np.array([1, 2, 3, 4, 5])
print(f"Size: {arr.size}, Ndim: {arr.ndim}")""",
     "quiz": """[
{"question": "Kako se importuje NumPy?", "options": ["import numpy as np", "import np", "from numpy import all", "include numpy"], "correct": 0},
{"question": "np.array([1,2,3]) kreira?", "options": ["ndarray", "list", "tuple", "dict"], "correct": 0},
{"question": "arr.shape vraća?", "options": ["Dimenzije kao tuple", "Broj elemenata", "Tip", "Prvu vrijednost"], "correct": 0},
{"question": "arr.ndim vraća?", "options": ["Broj dimenzija", "Broj elemenata", "Tip", "Shape"], "correct": 0},
{"question": "NumPy je brži jer?", "options": ["Koristi C kod i homogene tipove", "Ima više funkcija", "Noviji je", "Koristi GPU"], "correct": 0}
]"""},

    {"title": "NumPy - Kreiranje Arraya", "order": 2, "duration_hours": 1,
     "content": """# 🔢 Metode za Kreiranje Arraya

## np.arange() - Sekvencijalni brojevi
```python
np.arange(10)        # [0, 1, ..., 9]
np.arange(2, 10)     # [2, 3, ..., 9]
np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
```

## np.linspace() - Ravnomjerno raspoređeni
```python
np.linspace(0, 1, 5)  # [0, 0.25, 0.5, 0.75, 1]
```

## np.zeros(), np.ones(), np.full()
```python
np.zeros(5)          # [0, 0, 0, 0, 0]
np.ones((2, 3))      # Matrica 2x3 jedinica
np.full((2, 2), 7)   # Matrica 2x2 sa 7
```

## np.random
```python
np.random.rand(3)         # 3 broja [0, 1)
np.random.randint(1, 10, 5)  # 5 cijelih [1, 10)
```
""",
     "code_example": """import numpy as np

print("=== arange ===")
print(f"arange(5): {np.arange(5)}")
print(f"arange(2, 8): {np.arange(2, 8)}")
print(f"arange(0, 20, 3): {np.arange(0, 20, 3)}")

print("\\n=== linspace ===")
print(f"linspace(0, 10, 5): {np.linspace(0, 10, 5)}")

print("\\n=== zeros, ones, full ===")
print(f"zeros(4): {np.zeros(4)}")
print(f"ones((2, 3)):\\n{np.ones((2, 3))}")
print(f"full((2, 2), 99):\\n{np.full((2, 2), 99)}")

print("\\n=== eye (jedinična matrica) ===")
print(f"eye(3):\\n{np.eye(3)}")

print("\\n=== random ===")
np.random.seed(42)
print(f"rand(4): {np.random.rand(4)}")
print(f"randint(1, 100, 5): {np.random.randint(1, 100, 5)}")""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Arange
Kreirajte array parnih brojeva od 0 do 20 koristeći np.arange().

### Vježba 2: Linspace
Kreirajte 5 jednako raspoređenih brojeva između 0 i 100.

### Vježba 3: Random
Generirajte 6 slučajnih cijelih brojeva između 1 i 50.""",
     "exercise_solution": """# Vježba 1
import numpy as np
parni = np.arange(0, 21, 2)
print(f"Parni: {parni}")

# Vježba 2
lin = np.linspace(0, 100, 5)
print(f"Linspace: {lin}")

# Vježba 3
rand = np.random.randint(1, 51, 6)
print(f"Random: {rand}")""",
     "quiz": """[
{"question": "np.arange(0, 10, 2) vraća?", "options": ["[0, 2, 4, 6, 8]", "[0, 2, 4, 6, 8, 10]", "[2, 4, 6, 8]", "[0, 1, 2]"], "correct": 0},
{"question": "np.linspace(0, 10, 3) vraća?", "options": ["[0, 5, 10]", "[0, 1, 2]", "[0, 10, 3]", "[3, 6, 9]"], "correct": 0},
{"question": "np.zeros((2, 3)) kreira?", "options": ["Matricu 2x3 nula", "Array [2, 3]", "6 nula", "Error"], "correct": 0},
{"question": "np.eye(4) kreira?", "options": ["4x4 jediničnu matricu", "4 jedinice", "4x4 nula", "Array [4]"], "correct": 0},
{"question": "np.random.randint(1, 10, 5) vraća?", "options": ["5 cijelih od 1 do 9", "Broj 1-10", "5 decimalnih", "10 brojeva"], "correct": 0}
]"""},

    {"title": "NumPy - Operacije", "order": 3, "duration_hours": 1,
     "content": """# ⚡ Aritmetičke Operacije

## Vektorske operacije
```python
arr = np.array([1, 2, 3, 4])
arr + 10      # [11, 12, 13, 14]
arr * 2       # [2, 4, 6, 8]
arr ** 2      # [1, 4, 9, 16]
```

## Operacije između arraya
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
a + b         # [5, 7, 9]
a * b         # [4, 10, 18]
```

## Matematičke funkcije
```python
np.sqrt(arr)   # Korijen
np.exp(arr)    # e^x
np.log(arr)    # Prirodni logaritam
np.sin(arr)    # Sinus
np.abs(arr)    # Apsolutna vrijednost
```
""",
     "code_example": """import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(f"Original: {arr}")

print("\\n=== Aritmetičke operacije ===")
print(f"arr + 10 = {arr + 10}")
print(f"arr * 3 = {arr * 3}")
print(f"arr / 2 = {arr / 2}")
print(f"arr ** 2 = {arr ** 2}")
print(f"arr % 2 = {arr % 2}")

print("\\n=== Operacije između arraya ===")
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(f"a + b = {a + b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")

print("\\n=== Matematičke funkcije ===")
arr = np.array([1, 4, 9, 16, 25])
print(f"sqrt: {np.sqrt(arr)}")

arr2 = np.array([-3, -1, 0, 1, 3])
print(f"abs: {np.abs(arr2)}")""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Operacije
Kreirajte array [5, 10, 15, 20] i podijelite ga sa 5.

### Vježba 2: Korijen
Izračunajte korijen svakog elementa u [4, 16, 25, 36, 49].

### Vježba 3: Množenje arraya
Pomnožite [1, 2, 3] i [10, 20, 30].""",
     "exercise_solution": """# Vježba 1
import numpy as np
arr = np.array([5, 10, 15, 20])
print(f"arr / 5 = {arr / 5}")

# Vježba 2
arr = np.array([4, 16, 25, 36, 49])
print(f"sqrt = {np.sqrt(arr)}")

# Vježba 3
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(f"a * b = {a * b}")""",
     "quiz": """[
{"question": "np.array([1,2,3]) * 2 vraća?", "options": ["[2, 4, 6]", "[1, 2, 3, 1, 2, 3]", "Error", "6"], "correct": 0},
{"question": "np.sqrt(16) vraća?", "options": ["4.0", "256", "8", "Error"], "correct": 0},
{"question": "[1,2] + [3,4] kao NumPy?", "options": ["[4, 6]", "[1, 2, 3, 4]", "Error", "[4]"], "correct": 0},
{"question": "Šta je broadcasting?", "options": ["Automatsko prilagođavanje dimenzija", "Slanje podataka", "Kopiranje", "Sortiranje"], "correct": 0},
{"question": "np.abs([-5, 3]) vraća?", "options": ["[5, 3]", "[-5, 3]", "[5, -3]", "Error"], "correct": 0}
]"""},

    {"title": "NumPy - Indeksiranje i Slicing", "order": 4, "duration_hours": 1,
     "content": """# 🔍 Indeksiranje i Slicing

## 1D Array
```python
arr = np.array([10, 20, 30, 40, 50])
arr[0]        # 10 (prvi)
arr[-1]       # 50 (zadnji)
arr[1:4]      # [20, 30, 40]
arr[::2]      # [10, 30, 50]
```

## 2D Array
```python
arr[0, 0]     # Prvi red, prva kolona
arr[1, :]     # Drugi red (sve kolone)
arr[:, 0]     # Prva kolona (svi redovi)
```

## Boolean indeksiranje
```python
arr[arr > 2]  # Elementi veći od 2
arr[arr % 2 == 0]  # Parni elementi
```
""",
     "code_example": """import numpy as np

print("=== 1D Indeksiranje ===")
arr = np.array([10, 20, 30, 40, 50, 60, 70])
print(f"Array: {arr}")
print(f"arr[0] = {arr[0]}")
print(f"arr[-1] = {arr[-1]}")
print(f"arr[2:5] = {arr[2:5]}")
print(f"arr[::2] = {arr[::2]}")
print(f"arr[::-1] = {arr[::-1]}")

print("\\n=== 2D Indeksiranje ===")
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Matrica:\\n{matrix}")
print(f"matrix[0, 0] = {matrix[0, 0]}")
print(f"matrix[1] = {matrix[1]}")
print(f"matrix[:, 0] = {matrix[:, 0]}")
print(f"matrix[0:2, 1:3] =\\n{matrix[0:2, 1:3]}")

print("\\n=== Boolean indeksiranje ===")
arr = np.array([15, 22, 8, 33, 12, 45])
print(f"arr > 20: {arr[arr > 20]}")
print(f"Parni: {arr[arr % 2 == 0]}")""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Slicing
Iz [5, 10, 15, 20, 25, 30] izdvojite elemente od indeksa 2 do 4.

### Vježba 2: Filtriranje
Iz [12, 5, 23, 8, 17, 31] izdvojite brojeve veće od 10.

### Vježba 3: 2D
Kreirajte matricu 3x3 i izdvojite drugu kolonu.""",
     "exercise_solution": """# Vježba 1
import numpy as np
arr = np.array([5, 10, 15, 20, 25, 30])
print(f"arr[2:5] = {arr[2:5]}")

# Vježba 2
arr = np.array([12, 5, 23, 8, 17, 31])
print(f"Veći od 10: {arr[arr > 10]}")

# Vježba 3
m = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(f"Druga kolona: {m[:, 1]}")""",
     "quiz": """[
{"question": "arr[-1] vraća?", "options": ["Zadnji element", "Prvi element", "Error", "-1"], "correct": 0},
{"question": "arr[2:5] uključuje indeks 5?", "options": ["Ne", "Da", "Zavisi", "Error"], "correct": 0},
{"question": "arr[arr > 5] radi?", "options": ["Filtrira elemente > 5", "Vraća True/False", "Error", "Vraća 5"], "correct": 0},
{"question": "matrix[:, 0] vraća?", "options": ["Prvu kolonu", "Prvi red", "Sve", "Error"], "correct": 0},
{"question": "arr[::2] vraća?", "options": ["Svaki drugi element", "Prvih 2", "Zadnja 2", "Parove"], "correct": 0}
]"""},

    {"title": "NumPy - Statistika", "order": 5, "duration_hours": 1,
     "content": """# 📈 Statističke Funkcije

## Osnovne statistike
```python
arr = np.array([1, 2, 3, 4, 5])
np.sum(arr)       # 15 - suma
np.mean(arr)      # 3.0 - prosjek
np.median(arr)    # 3.0 - medijan
np.std(arr)       # standardna devijacija
np.var(arr)       # varijansa
np.min(arr), np.max(arr)
```

## Pozicije
```python
np.argmin(arr)    # Indeks minimuma
np.argmax(arr)    # Indeks maksimuma
```

## Agregacije po osama
```python
matrix = np.array([[1, 2], [3, 4]])
np.sum(matrix, axis=0)  # Po kolonama
np.sum(matrix, axis=1)  # Po redovima
```
""",
     "code_example": """import numpy as np

ocjene = np.array([78, 85, 92, 67, 88, 73, 95, 82])
print(f"Ocjene: {ocjene}")

print("\\n=== Statistike ===")
print(f"Suma: {np.sum(ocjene)}")
print(f"Prosjek: {np.mean(ocjene):.2f}")
print(f"Medijan: {np.median(ocjene)}")
print(f"Std: {np.std(ocjene):.2f}")
print(f"Min: {np.min(ocjene)}, Max: {np.max(ocjene)}")

print("\\n=== Pozicije ===")
print(f"Indeks min: {np.argmin(ocjene)}")
print(f"Indeks max: {np.argmax(ocjene)}")

print("\\n=== Agregacije po osama ===")
m = np.array([[10, 20, 30], [40, 50, 60]])
print(f"Matrica:\\n{m}")
print(f"Suma po kolonama: {np.sum(m, axis=0)}")
print(f"Suma po redovima: {np.sum(m, axis=1)}")
print(f"Prosjek po kolonama: {np.mean(m, axis=0)}")

print("\\n=== Kumulativno ===")
arr = np.array([1, 2, 3, 4, 5])
print(f"Cumsum: {np.cumsum(arr)}")""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Statistika
Za [85, 92, 78, 90, 88] izračunajte prosjek i std.

### Vježba 2: Pozicije
Pronađite indeks min i max u [23, 45, 12, 67, 34].

### Vježba 3: Osa
Za [[1,2,3],[4,5,6]] izračunajte sumu po kolonama.""",
     "exercise_solution": """# Vježba 1
import numpy as np
arr = np.array([85, 92, 78, 90, 88])
print(f"Prosjek: {np.mean(arr):.2f}")
print(f"Std: {np.std(arr):.2f}")

# Vježba 2
arr = np.array([23, 45, 12, 67, 34])
print(f"Indeks min: {np.argmin(arr)}")
print(f"Indeks max: {np.argmax(arr)}")

# Vježba 3
m = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Suma po kolonama: {np.sum(m, axis=0)}")""",
     "quiz": """[
{"question": "np.mean([2, 4, 6, 8]) vraća?", "options": ["5.0", "20", "4", "6"], "correct": 0},
{"question": "np.argmax([5, 9, 3]) vraća?", "options": ["1", "9", "3", "0"], "correct": 0},
{"question": "axis=0 znači?", "options": ["Po kolonama", "Po redovima", "Dijagonalno", "Sve"], "correct": 0},
{"question": "np.cumsum([1,2,3]) vraća?", "options": ["[1, 3, 6]", "[6]", "[1, 2, 3]", "[3, 2, 1]"], "correct": 0},
{"question": "np.std() računa?", "options": ["Standardnu devijaciju", "Sumu", "Prosjek", "Medijan"], "correct": 0}
]"""},

    {"title": "NumPy - Reshape", "order": 6, "duration_hours": 1,
     "content": """# 🔄 Reshape i Manipulacija

## Reshape
```python
arr = np.arange(12)
arr.reshape(3, 4)     # 3 reda, 4 kolone
arr.reshape(2, -1)    # 2 reda, auto kolone
arr.flatten()         # 1D
```

## Transpose
```python
matrix.T              # Transponiranje
```

## Spajanje
```python
np.concatenate([a, b])
np.vstack([a, b])     # Vertikalno
np.hstack([a, b])     # Horizontalno
```
""",
     "code_example": """import numpy as np

print("=== Reshape ===")
arr = np.arange(1, 13)
print(f"Original: {arr}")

m1 = arr.reshape(3, 4)
print(f"Reshape (3, 4):\\n{m1}")

m2 = arr.reshape(2, -1)
print(f"Reshape (2, -1):\\n{m2}")

print("\\n=== Flatten ===")
print(f"Flatten: {m1.flatten()}")

print("\\n=== Transpose ===")
m = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original:\\n{m}")
print(f"Transpose:\\n{m.T}")

print("\\n=== Spajanje ===")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"Concatenate: {np.concatenate([a, b])}")

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(f"Vstack:\\n{np.vstack([m1, m2])}")
print(f"Hstack:\\n{np.hstack([m1, m2])}")""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Reshape
Array [1..12] pretvorite u matricu 4x3.

### Vježba 2: Transpose
Kreirajte matricu 2x4 i transponirajte je.

### Vježba 3: Spajanje
Spojite [10, 20, 30] i [40, 50, 60].""",
     "exercise_solution": """# Vježba 1
import numpy as np
arr = np.arange(1, 13).reshape(4, 3)
print(arr)

# Vježba 2
m = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"Transpose:\\n{m.T}")

# Vježba 3
a = np.array([10, 20, 30])
b = np.array([40, 50, 60])
print(f"Spojeno: {np.concatenate([a, b])}")""",
     "quiz": """[
{"question": "arr.reshape(2, -1) znači?", "options": ["2 reda, auto kolone", "2 kolone", "Error", "-1 red"], "correct": 0},
{"question": "Šta radi .T?", "options": ["Transponira", "Transformira", "Testira", "Tipizira"], "correct": 0},
{"question": "np.vstack spaja?", "options": ["Vertikalno", "Horizontalno", "Dijagonalno", "Ne spaja"], "correct": 0},
{"question": "arr.flatten() vraća?", "options": ["1D array", "2D array", "Kopiju", "None"], "correct": 0},
{"question": "np.concatenate prima?", "options": ["Listu arraya", "Jedan array", "Stringove", "Brojeve"], "correct": 0}
]"""},

    {"title": "Uvod u Pandas", "order": 7, "duration_hours": 1,
     "content": """# 🐼 Pandas - Uvod

## Šta je Pandas?
Pandas je biblioteka za analizu podataka. Pruža DataFrame i Series strukture.

## Series - 1D označeni niz
```python
import pandas as pd
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
```

## DataFrame - 2D tabela
```python
df = pd.DataFrame({
    'ime': ['Ana', 'Marko'],
    'godine': [25, 30]
})
```

## Zašto Pandas?
- 📊 Čitanje CSV, Excel, SQL
- 🔍 Moćno filtriranje
- 📈 Statistika
""",
     "code_example": """import pandas as pd

print("=== Series ===")
s = pd.Series([100, 200, 300, 400])
print(s)
print(f"\\nSa custom indexom:")
ocjene = pd.Series([85, 92, 78], index=['Math', 'Physics', 'Chemistry'])
print(ocjene)
print(f"Physics: {ocjene['Physics']}")

print("\\n=== DataFrame ===")
df = pd.DataFrame({
    'ime': ['Ana', 'Marko', 'Ivana', 'Petar'],
    'godine': [25, 30, 22, 35],
    'grad': ['Sarajevo', 'Zagreb', 'Beograd', 'Ljubljana'],
    'plata': [2500, 3200, 2800, 4000]
})
print(df)

print(f"\\n=== Info ===")
print(f"Shape: {df.shape}")
print(f"Kolone: {df.columns.tolist()}")
print(f"\\nHead:\\n{df.head(2)}")
print(f"\\nDescribe:\\n{df.describe()}")""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Series
Kreirajte Series sa temp [22, 25, 19] i index ['Pon', 'Uto', 'Sri'].

### Vježba 2: DataFrame
Kreirajte DataFrame sa 3 proizvoda (ime, cijena).

### Vježba 3: Info
Ispišite shape i kolone DataFrame-a.""",
     "exercise_solution": """# Vježba 1
import pandas as pd
temp = pd.Series([22, 25, 19], index=['Pon', 'Uto', 'Sri'])
print(temp)

# Vježba 2
df = pd.DataFrame({
    'ime': ['Laptop', 'Telefon', 'Tablet'],
    'cijena': [1500, 800, 500]
})
print(df)

# Vježba 3
print(f"Shape: {df.shape}")
print(f"Kolone: {df.columns.tolist()}")""",
     "quiz": """[
{"question": "Kako se importuje Pandas?", "options": ["import pandas as pd", "import pd", "from pandas import all", "include pandas"], "correct": 0},
{"question": "Series je?", "options": ["1D označeni niz", "2D tabela", "3D kocka", "Graf"], "correct": 0},
{"question": "DataFrame je sličan?", "options": ["Excel tabeli", "Tekst fajlu", "Slici", "Grafu"], "correct": 0},
{"question": "df.shape vraća?", "options": ["(redovi, kolone)", "Broj redova", "Listu", "String"], "correct": 0},
{"question": "df.head() prikazuje?", "options": ["Prvih 5 redova", "Zadnjih 5", "Sve", "Info"], "correct": 0}
]"""},

    {"title": "Pandas - Selekcija Podataka", "order": 8, "duration_hours": 1,
     "content": """# 🔍 Selekcija u Pandas

## Selekcija kolona
```python
df['ime']              # Jedna kolona (Series)
df[['ime', 'godine']]  # Više kolona (DataFrame)
```

## loc - Label-based
```python
df.loc[0]              # Red sa indexom 0
df.loc[0, 'ime']       # Specifična ćelija
```

## iloc - Integer-based
```python
df.iloc[0]             # Prvi red
df.iloc[0, 1]          # Red 0, kolona 1
```

## Filtriranje
```python
df[df['godine'] > 25]
df[(df['godine'] > 20) & (df['plata'] > 3000)]
```
""",
     "code_example": """import pandas as pd

df = pd.DataFrame({
    'ime': ['Ana', 'Marko', 'Ivana', 'Petar'],
    'godine': [25, 30, 22, 35],
    'grad': ['Sarajevo', 'Zagreb', 'Beograd', 'Ljubljana'],
    'plata': [2500, 3200, 2800, 4000]
})
print("DataFrame:\\n", df)

print("\\n=== Selekcija kolona ===")
print(f"df['ime']:\\n{df['ime']}")

print("\\n=== loc ===")
print(f"df.loc[0]:\\n{df.loc[0]}")
print(f"df.loc[1, 'ime']: {df.loc[1, 'ime']}")

print("\\n=== iloc ===")
print(f"df.iloc[0, 1]: {df.iloc[0, 1]}")
print(f"df.iloc[0:2, 0:2]:\\n{df.iloc[0:2, 0:2]}")

print("\\n=== Filtriranje ===")
print(f"Stariji od 25:\\n{df[df['godine'] > 25]}")
print(f"\\nIz Sarajeva:\\n{df[df['grad'] == 'Sarajevo']}")""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Kolona
Iz DataFrame-a izdvojite kolonu 'ime'.

### Vježba 2: loc
Dohvatite vrijednost u prvom redu, koloni 'grad'.

### Vježba 3: Filter
Filtrirajte osobe mlađe od 30.""",
     "exercise_solution": """# Vježba 1
import pandas as pd
df = pd.DataFrame({
    'ime': ['Ana', 'Marko', 'Ivana'],
    'godine': [25, 30, 22],
    'grad': ['Sarajevo', 'Zagreb', 'Beograd']
})
print(df['ime'])

# Vježba 2
print(f"Grad: {df.loc[0, 'grad']}")

# Vježba 3
print(df[df['godine'] < 30])""",
     "quiz": """[
{"question": "df['kolona'] vraća?", "options": ["Series", "DataFrame", "List", "Dict"], "correct": 0},
{"question": "df.loc koristi?", "options": ["Labele", "Pozicije", "Oba", "Ništa"], "correct": 0},
{"question": "df.iloc koristi?", "options": ["Pozicije", "Labele", "Oba", "Ništa"], "correct": 0},
{"question": "df[df['x'] > 5] radi?", "options": ["Filtrira", "Vraća kolonu", "Error", "Briše"], "correct": 0},
{"question": "& u filteru znači?", "options": ["AND", "OR", "NOT", "XOR"], "correct": 0}
]"""},

    {"title": "Pandas - Grupiranje i Agregacije", "order": 9, "duration_hours": 1,
     "content": """# 📊 Grupiranje i Agregacije

## groupby
```python
df.groupby('grad')['plata'].mean()
df.groupby('odjel').agg({'plata': 'mean', 'godine': 'max'})
```

## Sortiranje
```python
df.sort_values('plata', ascending=False)
df.sort_values(['odjel', 'plata'])
```

## Agregacije
```python
df['plata'].sum()
df['godine'].mean()
df.groupby('odjel')['plata'].agg(['mean', 'min', 'max'])
```
""",
     "code_example": """import pandas as pd

df = pd.DataFrame({
    'ime': ['Ana', 'Marko', 'Ivana', 'Petar', 'Maja'],
    'odjel': ['IT', 'HR', 'IT', 'HR', 'IT'],
    'godine': [25, 30, 22, 35, 28],
    'plata': [2500, 3200, 2800, 4000, 3100]
})
print("DataFrame:\\n", df)

print("\\n=== Grupiranje ===")
print(f"Prosjek plate po odjelu:\\n{df.groupby('odjel')['plata'].mean()}")

print(f"\\nViše agregacija:\\n{df.groupby('odjel')['plata'].agg(['mean', 'min', 'max'])}")

print(f"\\nBroj po odjelu:\\n{df.groupby('odjel').size()}")

print("\\n=== Sortiranje ===")
print(f"Po plati (desc):\\n{df.sort_values('plata', ascending=False)}")

print(f"\\nPo odjelu pa plati:\\n{df.sort_values(['odjel', 'plata'])}")

print("\\n=== Agregacije ===")
print(f"Ukupna plata: {df['plata'].sum()}")
print(f"Prosječne godine: {df['godine'].mean():.1f}")""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Grupiranje
Izračunajte prosječnu platu po odjelu.

### Vježba 2: Sortiranje
Sortirajte po godinama opadajuće.

### Vježba 3: Agregacija
Izračunajte min i max plate po odjelu.""",
     "exercise_solution": """# Vježba 1
import pandas as pd
df = pd.DataFrame({
    'ime': ['Ana', 'Marko', 'Ivana'],
    'odjel': ['IT', 'HR', 'IT'],
    'plata': [2500, 3200, 2800]
})
print(df.groupby('odjel')['plata'].mean())

# Vježba 2
print(df.sort_values('plata', ascending=False))

# Vježba 3
print(df.groupby('odjel')['plata'].agg(['min', 'max']))""",
     "quiz": """[
{"question": "groupby('a')['b'].mean() radi?", "options": ["Prosjek b po grupama a", "Grupira po b", "Error", "Sortira"], "correct": 0},
{"question": "sort_values ascending=False?", "options": ["Opadajuće", "Rastuće", "Random", "Error"], "correct": 0},
{"question": "agg(['sum', 'mean']) vraća?", "options": ["Više agregacija", "Jednu", "Error", "Listu"], "correct": 0},
{"question": "df.groupby('x').size() vraća?", "options": ["Broj po grupama", "Veličinu df", "Error", "Shape"], "correct": 0},
{"question": "df['x'].sum() vraća?", "options": ["Sumu kolone", "Listu", "DataFrame", "Series"], "correct": 0}
]"""},

    {"title": "Pandas - Dodavanje i Brisanje", "order": 10, "duration_hours": 1,
     "content": """# ✏️ Modifikacija DataFrame

## Dodavanje kolone
```python
df['nova'] = df['plata'] * 12
df['bonus'] = 500
```

## Brisanje
```python
df.drop('kolona', axis=1)         # Kolonu
df.drop([0, 1], axis=0)           # Redove
df.drop(columns=['a', 'b'])       # Više kolona
```

## Izmjena vrijednosti
```python
df.loc[0, 'ime'] = 'Novo Ime'
df['plata'] = df['plata'] * 1.1
```

## Rename
```python
df.rename(columns={'old': 'new'})
```
""",
     "code_example": """import pandas as pd

df = pd.DataFrame({
    'ime': ['Ana', 'Marko', 'Ivana'],
    'plata': [2500, 3200, 2800]
})
print("Original:\\n", df)

print("\\n=== Dodavanje kolone ===")
df['godisnja'] = df['plata'] * 12
df['bonus'] = 500
print(df)

print("\\n=== Izračunata kolona ===")
df['ukupno'] = df['plata'] + df['bonus']
print(df)

print("\\n=== Brisanje kolone ===")
df2 = df.drop('bonus', axis=1)
print(df2)

print("\\n=== Izmjena vrijednosti ===")
df.loc[0, 'ime'] = 'Ana Anić'
print(df)

print("\\n=== Rename ===")
df3 = df.rename(columns={'plata': 'mjesecna_plata'})
print(df3.columns.tolist())

print("\\n=== Reset index ===")
df_filtered = df[df['plata'] > 2600]
print(df_filtered.reset_index(drop=True))""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Nova kolona
Dodajte kolonu 'godisnja' = plata * 12.

### Vježba 2: Brisanje
Obrišite kolonu 'bonus' iz DataFrame-a.

### Vježba 3: Izmjena
Promijenite ime u prvom redu u 'Test'.""",
     "exercise_solution": """# Vježba 1
import pandas as pd
df = pd.DataFrame({
    'ime': ['Ana', 'Marko'],
    'plata': [2500, 3200],
    'bonus': [500, 600]
})
df['godisnja'] = df['plata'] * 12
print(df)

# Vježba 2
df2 = df.drop('bonus', axis=1)
print(df2)

# Vježba 3
df.loc[0, 'ime'] = 'Test'
print(df)""",
     "quiz": """[
{"question": "df['nova'] = 100 radi?", "options": ["Dodaje kolonu sa 100", "Error", "Briše", "Ništa"], "correct": 0},
{"question": "drop axis=1 briše?", "options": ["Kolonu", "Red", "Sve", "Ništa"], "correct": 0},
{"question": "drop axis=0 briše?", "options": ["Red", "Kolonu", "Sve", "Ništa"], "correct": 0},
{"question": "rename columns radi?", "options": ["Preimenuje kolone", "Briše", "Dodaje", "Sortira"], "correct": 0},
{"question": "df.loc[0, 'x'] = 5 radi?", "options": ["Mijenja vrijednost", "Error", "Briše", "Dodaje red"], "correct": 0}
]"""},

    {"title": "Pandas - Missing Data", "order": 11, "duration_hours": 1,
     "content": """# 🕳️ Rad sa Missing Podacima

## Detekcija
```python
df.isnull()           # True gdje je NaN
df.notnull()          # True gdje nije NaN
df.isnull().sum()     # Broj NaN po koloni
```

## Uklanjanje
```python
df.dropna()           # Ukloni redove sa NaN
df.dropna(axis=1)     # Ukloni kolone sa NaN
df.dropna(subset=['kolona'])
```

## Popunjavanje
```python
df.fillna(0)          # Zamijeni sa 0
df.fillna(method='ffill')  # Forward fill
df['x'].fillna(df['x'].mean())  # Sa prosjekom
```
""",
     "code_example": """import pandas as pd
import numpy as np

df = pd.DataFrame({
    'ime': ['Ana', 'Marko', None, 'Petar'],
    'godine': [25, np.nan, 22, 35],
    'plata': [2500, 3200, np.nan, 4000]
})
print("DataFrame sa NaN:\\n", df)

print("\\n=== Detekcija ===")
print(f"isnull():\\n{df.isnull()}")
print(f"\\nBroj NaN po koloni:\\n{df.isnull().sum()}")

print("\\n=== Dropna ===")
print(f"dropna():\\n{df.dropna()}")

print("\\n=== Fillna ===")
df_filled = df.copy()
df_filled['godine'] = df_filled['godine'].fillna(df_filled['godine'].mean())
df_filled['plata'] = df_filled['plata'].fillna(0)
df_filled['ime'] = df_filled['ime'].fillna('Nepoznato')
print(f"Popunjeno:\\n{df_filled}")

print("\\n=== Provjera ===")
print(f"Ima NaN: {df_filled.isnull().any().any()}")""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Detekcija
Prebrojte koliko NaN ima u svakoj koloni.

### Vježba 2: Dropna
Uklonite sve redove koji imaju NaN.

### Vježba 3: Fillna
Popunite NaN u koloni 'godine' sa prosjekom.""",
     "exercise_solution": """# Vježba 1
import pandas as pd
import numpy as np
df = pd.DataFrame({
    'ime': ['Ana', None, 'Ivana'],
    'godine': [25, np.nan, 22]
})
print(df.isnull().sum())

# Vježba 2
print(df.dropna())

# Vježba 3
df['godine'] = df['godine'].fillna(df['godine'].mean())
print(df)""",
     "quiz": """[
{"question": "isnull() vraća?", "options": ["Boolean DataFrame", "Broj NaN", "Listu", "Error"], "correct": 0},
{"question": "dropna() uklanja?", "options": ["Redove sa NaN", "Sve NaN", "Kolone", "Ništa"], "correct": 0},
{"question": "fillna(0) radi?", "options": ["Zamjenjuje NaN sa 0", "Briše 0", "Dodaje 0", "Error"], "correct": 0},
{"question": "NaN u Pythonu je?", "options": ["np.nan", "None", "null", "0"], "correct": 0},
{"question": "isnull().sum() vraća?", "options": ["Broj NaN po koloni", "Total NaN", "Boolean", "Error"], "correct": 0}
]"""},

    {"title": "Pandas - CSV i Export", "order": 12, "duration_hours": 1,
     "content": """# 📁 Čitanje i Pisanje Fajlova

## CSV
```python
df = pd.read_csv('file.csv')
df.to_csv('output.csv', index=False)
```

## Excel
```python
df = pd.read_excel('file.xlsx')
df.to_excel('output.xlsx', index=False)
```

## Parametri read_csv
```python
pd.read_csv('file.csv', 
    sep=';',           # Separator
    header=0,          # Red sa headerom
    names=['a', 'b'],  # Imena kolona
    usecols=['a'],     # Samo neke kolone
    nrows=100          # Prvih N redova
)
```
""",
     "code_example": """import pandas as pd

# Kreiranje test DataFrame
df = pd.DataFrame({
    'ime': ['Ana', 'Marko', 'Ivana'],
    'godine': [25, 30, 22],
    'grad': ['Sarajevo', 'Zagreb', 'Beograd']
})
print("DataFrame:\\n", df)

# Simulacija CSV operacija
print("\\n=== CSV Operacije ===")
csv_string = df.to_csv(index=False)
print(f"CSV format:\\n{csv_string}")

# Kreiranje iz CSV stringa
from io import StringIO
df_from_csv = pd.read_csv(StringIO(csv_string))
print(f"Učitano iz CSV:\\n{df_from_csv}")

print("\\n=== Info o učitanom ===")
print(f"Shape: {df_from_csv.shape}")
print(f"Dtypes:\\n{df_from_csv.dtypes}")

print("\\n=== to_dict ===")
print(f"Dict: {df.to_dict()}")
print(f"Records: {df.to_dict('records')}")

print("\\n=== to_json ===")
print(f"JSON:\\n{df.to_json(orient='records', indent=2)}")""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: CSV
Kreirajte DataFrame i pretvorite ga u CSV string.

### Vježba 2: to_dict
Pretvorite DataFrame u listu rječnika (records).

### Vježba 3: Info
Ispišite dtypes učitanog DataFrame-a.""",
     "exercise_solution": """# Vježba 1
import pandas as pd
df = pd.DataFrame({
    'proizvod': ['A', 'B', 'C'],
    'cijena': [100, 200, 150]
})
csv = df.to_csv(index=False)
print(csv)

# Vježba 2
records = df.to_dict('records')
print(records)

# Vježba 3
print(df.dtypes)""",
     "quiz": """[
{"question": "read_csv vraća?", "options": ["DataFrame", "List", "Dict", "String"], "correct": 0},
{"question": "to_csv index=False znači?", "options": ["Bez index kolone", "Sa indexom", "Error", "Sortira"], "correct": 0},
{"question": "sep=';' znači?", "options": ["Separator je ;", "Separator je ,", "Error", "Ništa"], "correct": 0},
{"question": "nrows=100 čita?", "options": ["Prvih 100 redova", "100 kolona", "Sve", "Zadnjih 100"], "correct": 0},
{"question": "to_dict('records') vraća?", "options": ["Listu rječnika", "Rječnik", "Listu", "DataFrame"], "correct": 0}
]"""},

    {"title": "Deskriptivna Statistika - Uvod", "order": 13, "duration_hours": 2,
     "content": """# 📊 Osnove Deskriptivne Statistike

## Šta je Deskriptivna Statistika?
Deskriptivna statistika opisuje i sumira podatke kroz:
- **Kvantitativni pristup** - numerički opisuje podatke
- **Vizualni pristup** - grafikoni, histogrami, plotovi

## Tipovi Mjera
1. **Centralna tendencija** - sredina podataka (mean, median, mode)
2. **Varijabilnost** - raspršenost podataka (variance, std)
3. **Korelacija** - veza između varijabli

## Populacija vs Uzorak
- **Populacija** - svi elementi koji nas zanimaju
- **Uzorak** - reprezentativni podskup populacije

## Outliers (Ekstremne Vrijednosti)
Podaci koji se značajno razlikuju od ostatka:
- Prirodna varijacija
- Greške u mjerenju
- Greške u unosu podataka

## Python Biblioteke za Statistiku
```python
import statistics      # Ugrađena biblioteka
import numpy as np     # Numeričke operacije
import scipy.stats     # Napredna statistika
import pandas as pd    # Analiza podataka
```
""",
     "code_example": """import numpy as np
import pandas as pd
import statistics

# Kreiranje podataka
x = [8.0, 1, 2.5, 4, 28.0]
print(f"Lista: {x}")

# NumPy array
y = np.array(x)
print(f"NumPy array: {y}")

# Pandas Series
z = pd.Series(x)
print(f"Pandas Series:\\n{z}")

# Rad sa NaN (Not a Number)
import math
x_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]
y_nan = np.array(x_nan)
print(f"\\nArray sa NaN: {y_nan}")

# Provjera NaN
print(f"math.isnan(math.nan): {math.isnan(math.nan)}")
print(f"np.isnan(np.nan): {np.isnan(np.nan)}")

# Osnovne statistike
print(f"\\n=== Osnovne statistike ===")
print(f"Suma: {sum(x)}")
print(f"Min: {min(x)}, Max: {max(x)}")
print(f"Dužina: {len(x)}")""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Kreiranje Podataka
Kreirajte listu [15, 22, 8, 33, 12, 45] i pretvorite je u NumPy array.

### Vježba 2: Pandas Series
Od liste [100, 200, 150, 300] kreirajte Pandas Series sa indexom ['A', 'B', 'C', 'D'].

### Vježba 3: NaN Vrijednosti
Kreirajte array sa NaN i provjerite koliko NaN vrijednosti ima.""",
     "exercise_solution": """# Vježba 1
import numpy as np
lista = [15, 22, 8, 33, 12, 45]
arr = np.array(lista)
print(f"Array: {arr}")

# Vježba 2
import pandas as pd
s = pd.Series([100, 200, 150, 300], index=['A', 'B', 'C', 'D'])
print(s)

# Vježba 3
arr_nan = np.array([1, np.nan, 3, np.nan, 5])
nan_count = np.isnan(arr_nan).sum()
print(f"Broj NaN: {nan_count}")""",
     "quiz": """[
{"question": "Deskriptivna statistika služi za?", "options": ["Opisivanje i sumiranje podataka", "Predviđanje", "Klasifikaciju", "Treniranje modela"], "correct": 0},
{"question": "Šta je uzorak?", "options": ["Podskup populacije", "Cijela populacija", "Outlier", "Varijabla"], "correct": 0},
{"question": "NaN u NumPy predstavlja?", "options": ["Not a Number", "Negative", "Null", "None"], "correct": 0},
{"question": "Koja biblioteka je ugrađena u Python?", "options": ["statistics", "numpy", "pandas", "scipy"], "correct": 0},
{"question": "Outlier je?", "options": ["Ekstremna vrijednost", "Prosjek", "Medijan", "Modus"], "correct": 0}
]"""},

    {"title": "Mjere Centralne Tendencije", "order": 14, "duration_hours": 2,
     "content": """# 📍 Mjere Centralne Tendencije

## Aritmetička Sredina (Mean)
Suma svih vrijednosti podijeljena sa brojem vrijednosti.
```python
mean = sum(x) / len(x)
# Ili: statistics.mean(x), np.mean(x)
```

## Medijan (Median)
Srednja vrijednost sortiranog skupa podataka.
- Neparni broj elemenata: srednji element
- Parni broj: prosjek dva srednja elementa

## Modus (Mode)
Vrijednost koja se najčešće pojavljuje.

## Ponderisana Sredina
Sredina gdje svaki element ima svoju težinu (weight).
```python
weighted_mean = sum(w[i] * x[i]) / sum(w)
```

## Geometrijska Sredina
n-ti korijen proizvoda svih elemenata.

## Harmonijska Sredina
Recipročna vrijednost sredine recipročnih vrijednosti.
""",
     "code_example": """import numpy as np
import statistics
import pandas as pd

x = [8.0, 1, 2.5, 4, 28.0]
print(f"Podaci: {x}")

print("\\n=== MEAN (Aritmetička sredina) ===")
# Pure Python
mean_py = sum(x) / len(x)
print(f"Python: {mean_py}")

# statistics modul
mean_stat = statistics.mean(x)
print(f"statistics.mean: {mean_stat}")

# NumPy
mean_np = np.mean(x)
print(f"np.mean: {mean_np}")

print("\\n=== MEDIAN ===")
median_stat = statistics.median(x)
print(f"statistics.median: {median_stat}")
print(f"np.median: {np.median(x)}")

print("\\n=== MODE ===")
data = [2, 3, 2, 8, 12, 2, 5]
mode_stat = statistics.mode(data)
print(f"Podaci: {data}")
print(f"Mode: {mode_stat}")

print("\\n=== WEIGHTED MEAN ===")
values = [8.0, 1, 2.5, 4, 28.0]
weights = [0.1, 0.2, 0.3, 0.25, 0.15]
wmean = np.average(values, weights=weights)
print(f"Ponderisana sredina: {wmean:.2f}")

print("\\n=== Pandas ===")
s = pd.Series(x)
print(f"Series mean: {s.mean()}")
print(f"Series median: {s.median()}")""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Mean
Izračunajte aritmetičku sredinu za [85, 92, 78, 90, 88] na 3 načina.

### Vježba 2: Median
Pronađite medijan za [12, 5, 23, 8, 17, 31, 9].

### Vježba 3: Mode
Pronađite modus za [5, 2, 8, 2, 9, 2, 5, 8, 2].""",
     "exercise_solution": """# Vježba 1
import numpy as np
import statistics
ocjene = [85, 92, 78, 90, 88]
print(f"Python: {sum(ocjene)/len(ocjene)}")
print(f"statistics: {statistics.mean(ocjene)}")
print(f"numpy: {np.mean(ocjene)}")

# Vježba 2
podaci = [12, 5, 23, 8, 17, 31, 9]
print(f"Median: {statistics.median(podaci)}")

# Vježba 3
podaci = [5, 2, 8, 2, 9, 2, 5, 8, 2]
print(f"Mode: {statistics.mode(podaci)}")""",
     "quiz": """[
{"question": "Mean za [2, 4, 6, 8] je?", "options": ["5", "4", "6", "20"], "correct": 0},
{"question": "Median za [1, 3, 5, 7, 9] je?", "options": ["5", "3", "7", "25"], "correct": 0},
{"question": "Mode je vrijednost koja?", "options": ["Se najčešće pojavljuje", "Je u sredini", "Je najveća", "Je najmanja"], "correct": 0},
{"question": "np.average(x, weights=w) računa?", "options": ["Ponderisanu sredinu", "Medijan", "Modus", "Varijansu"], "correct": 0},
{"question": "Ako ima NaN, statistics.mean vraća?", "options": ["nan", "0", "Error", "Ignoriše NaN"], "correct": 0}
]"""},

    {"title": "Mjere Varijabilnosti", "order": 15, "duration_hours": 2,
     "content": """# 📏 Mjere Varijabilnosti

## Varijansa (Variance)
Prosječno kvadratno odstupanje od sredine.
```python
# Sample variance (n-1 u nazivniku)
var = sum((xi - mean)**2) / (n - 1)
```

## Standardna Devijacija (Std)
Korijen varijanse - ista jedinica kao podaci.
```python
std = var ** 0.5
```

## Raspon (Range)
Razlika između max i min vrijednosti.

## Interkvartilni Raspon (IQR)
Razlika između 3. i 1. kvartila.

## Percentili i Kvartili
- Q1 (25%) - prvi kvartil
- Q2 (50%) - medijan
- Q3 (75%) - treći kvartil

## Skewness (Asimetrija)
- Pozitivan: rep na desnoj strani
- Negativan: rep na lijevoj strani
- ~0: simetričan
""",
     "code_example": """import numpy as np
import statistics
import pandas as pd

x = [8.0, 1, 2.5, 4, 28.0]
print(f"Podaci: {x}")

print("\\n=== VARIANCE ===")
# statistics
var_stat = statistics.variance(x)
print(f"statistics.variance: {var_stat}")

# NumPy (ddof=1 za sample variance)
var_np = np.var(x, ddof=1)
print(f"np.var(ddof=1): {var_np}")

print("\\n=== STANDARD DEVIATION ===")
std_stat = statistics.stdev(x)
print(f"statistics.stdev: {std_stat:.2f}")

std_np = np.std(x, ddof=1)
print(f"np.std(ddof=1): {std_np:.2f}")

print("\\n=== RANGE ===")
raspon = max(x) - min(x)
print(f"Range: {raspon}")
print(f"np.ptp: {np.ptp(x)}")

print("\\n=== PERCENTILES ===")
arr = np.array([1, 5, 10, 15, 20, 25, 30, 35, 40])
print(f"25th percentile: {np.percentile(arr, 25)}")
print(f"50th percentile: {np.percentile(arr, 50)}")
print(f"75th percentile: {np.percentile(arr, 75)}")

print("\\n=== QUANTILES ===")
print(f"Kvartili: {np.quantile(arr, [0.25, 0.5, 0.75])}")

print("\\n=== Pandas describe ===")
s = pd.Series(x)
print(s.describe())""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Variance i Std
Za [10, 20, 30, 40, 50] izračunajte varijansu i std.

### Vježba 2: Percentili
Pronađite 25., 50. i 75. percentil za [5, 10, 15, 20, 25, 30, 35].

### Vježba 3: Describe
Kreirajte Pandas Series i prikažite describe() summary.""",
     "exercise_solution": """# Vježba 1
import numpy as np
x = [10, 20, 30, 40, 50]
print(f"Variance: {np.var(x, ddof=1)}")
print(f"Std: {np.std(x, ddof=1):.2f}")

# Vježba 2
arr = np.array([5, 10, 15, 20, 25, 30, 35])
print(f"Q1: {np.percentile(arr, 25)}")
print(f"Q2: {np.percentile(arr, 50)}")
print(f"Q3: {np.percentile(arr, 75)}")

# Vježba 3
import pandas as pd
s = pd.Series([15, 22, 8, 33, 12, 45])
print(s.describe())""",
     "quiz": """[
{"question": "ddof=1 u np.var znači?", "options": ["Sample variance (n-1)", "Population variance", "Degrees of freedom 0", "Error"], "correct": 0},
{"question": "Std je?", "options": ["Korijen varijanse", "Kvadrat varijanse", "Prosjek", "Medijan"], "correct": 0},
{"question": "np.ptp() vraća?", "options": ["Range (max-min)", "Percentil", "Prosjek", "Std"], "correct": 0},
{"question": "Q2 (50. percentil) je isto što i?", "options": ["Medijan", "Mean", "Mode", "Variance"], "correct": 0},
{"question": "Pozitivan skewness znači?", "options": ["Rep na desnoj strani", "Rep na lijevoj", "Simetričan", "Bez repa"], "correct": 0}
]"""},

    {"title": "Korelacija i Kovarijansa", "order": 16, "duration_hours": 2,
     "content": """# 🔗 Korelacija i Kovarijansa

## Tipovi Korelacije
- **Pozitivna**: veće x → veće y
- **Negativna**: veće x → manje y
- **Slaba/Nema**: nema jasne veze

## Kovarijansa
Mjeri smjer veze između dvije varijable.
```python
cov_xy = sum((xi - mean_x)(yi - mean_y)) / (n-1)
```

## Koeficijent Korelacije (Pearson r)
- r = 1: savršena pozitivna korelacija
- r = -1: savršena negativna korelacija  
- r ≈ 0: slaba ili nema korelacije
```python
r = cov_xy / (std_x * std_y)
```

## VAŽNO
**Korelacija ≠ Kauzalnost!**
Korelacija pokazuje vezu, ali ne dokazuje da jedna varijabla uzrokuje drugu.
""",
     "code_example": """import numpy as np
import scipy.stats
import pandas as pd

# Podaci sa pozitivnom korelacijom
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([2, 4, 5, 4, 5, 7, 8, 9, 10, 12])

print("=== COVARIANCE ===")
# NumPy covariance matrix
cov_matrix = np.cov(x, y)
print(f"Covariance matrix:\\n{cov_matrix}")
print(f"Cov(x,y): {cov_matrix[0,1]:.2f}")

# Pandas
sx, sy = pd.Series(x), pd.Series(y)
print(f"Pandas cov: {sx.cov(sy):.2f}")

print("\\n=== CORRELATION ===")
# NumPy correlation matrix
corr_matrix = np.corrcoef(x, y)
print(f"Correlation matrix:\\n{corr_matrix}")
print(f"Pearson r: {corr_matrix[0,1]:.4f}")

# SciPy (vraća r i p-value)
r, p_value = scipy.stats.pearsonr(x, y)
print(f"\\nSciPy pearsonr:")
print(f"r = {r:.4f}")
print(f"p-value = {p_value:.6f}")

# Pandas
print(f"\\nPandas corr: {sx.corr(sy):.4f}")

print("\\n=== Interpretacija ===")
if r > 0.7:
    print("Jaka pozitivna korelacija")
elif r > 0.3:
    print("Umjerena pozitivna korelacija")
elif r > -0.3:
    print("Slaba ili nema korelacije")
elif r > -0.7:
    print("Umjerena negativna korelacija")
else:
    print("Jaka negativna korelacija")""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Kovarijansa
Izračunajte kovarijansu između [1,2,3,4,5] i [2,4,6,8,10].

### Vježba 2: Korelacija
Izračunajte Pearsonov koeficijent korelacije za iste podatke.

### Vježba 3: Interpretacija
Za r = 0.85, šta možete zaključiti o vezi između varijabli?""",
     "exercise_solution": """# Vježba 1
import numpy as np
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
cov = np.cov(x, y)[0, 1]
print(f"Covariance: {cov}")

# Vježba 2
r = np.corrcoef(x, y)[0, 1]
print(f"Correlation: {r:.4f}")

# Vježba 3
r = 0.85
print(f"r = {r}")
print("Interpretacija: Jaka pozitivna korelacija")
print("Veće vrijednosti x su povezane sa većim y")""",
     "quiz": """[
{"question": "r = 1 znači?", "options": ["Savršena pozitivna korelacija", "Nema korelacije", "Negativna korelacija", "Error"], "correct": 0},
{"question": "r = -0.9 je?", "options": ["Jaka negativna korelacija", "Slaba korelacija", "Pozitivna korelacija", "Nema veze"], "correct": 0},
{"question": "Korelacija dokazuje kauzalnost?", "options": ["Ne", "Da", "Ponekad", "Uvijek"], "correct": 0},
{"question": "np.cov(x,y) vraća?", "options": ["Matricu kovarijanse", "Jedan broj", "Korelaciju", "Prosjek"], "correct": 0},
{"question": "Pearsonov r mjeri?", "options": ["Linearnu korelaciju", "Nelinearnu vezu", "Kauzalnost", "Varijansu"], "correct": 0}
]"""},

    {"title": "Vizualizacija Podataka", "order": 17, "duration_hours": 2,
     "content": """# 📈 Vizualizacija Podataka

## Matplotlib
```python
import matplotlib.pyplot as plt
```

## Box Plot
Prikazuje: min, Q1, median, Q3, max i outliere.

## Histogram
Distribucija frekvencija u binovima.

## Pie Chart
Relativne proporcije kategorija.

## Bar Chart
Frekvencije po kategorijama.

## Scatter Plot (X-Y Plot)
Odnos između dvije numeričke varijable.

## Heatmap
Vizualizacija matrica (korelacija, kovarijansa).

## Kada koristiti koji graf?
- **Distribucija**: Histogram, Box Plot
- **Proporcije**: Pie Chart, Bar Chart
- **Veze**: Scatter Plot, Heatmap
- **Trendovi**: Line Plot
""",
     "code_example": """import numpy as np
import pandas as pd

# Simulacija vizualizacije (bez matplotlib u web env)
np.random.seed(42)
data = np.random.randn(100)

print("=== Podaci za vizualizaciju ===")
print(f"Shape: {data.shape}")
print(f"Mean: {np.mean(data):.2f}")
print(f"Std: {np.std(data):.2f}")

print("\\n=== Histogram podaci ===")
hist, bin_edges = np.histogram(data, bins=10)
print(f"Frekvencije: {hist}")
print(f"Bin edges: {np.round(bin_edges, 2)}")

print("\\n=== Box plot statistike ===")
q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)
iqr = q3 - q1
print(f"Q1 (25%): {q1:.2f}")
print(f"Q2 (50%): {q2:.2f}")
print(f"Q3 (75%): {q3:.2f}")
print(f"IQR: {iqr:.2f}")
print(f"Min: {np.min(data):.2f}")
print(f"Max: {np.max(data):.2f}")

print("\\n=== Korelacijska matrica ===")
df = pd.DataFrame({
    'A': np.random.randn(50),
    'B': np.random.randn(50),
    'C': np.random.randn(50)
})
print(df.corr().round(2))

print("\\n=== describe() - brzi pregled ===")
print(df.describe().round(2))""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Histogram Podaci
Kreirajte histogram podatke za [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5] sa 5 binova.

### Vježba 2: Box Plot Statistike
Za podatke [10,15,20,25,30,35,40] izračunajte Q1, Q2, Q3 i IQR.

### Vježba 3: Korelacijska Matrica
Kreirajte DataFrame sa 3 kolone i prikažite korelacijsku matricu.""",
     "exercise_solution": """# Vježba 1
import numpy as np
data = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
hist, edges = np.histogram(data, bins=5)
print(f"Frekvencije: {hist}")
print(f"Edges: {edges}")

# Vježba 2
data = np.array([10, 15, 20, 25, 30, 35, 40])
q1, q2, q3 = np.percentile(data, [25, 50, 75])
print(f"Q1: {q1}, Q2: {q2}, Q3: {q3}")
print(f"IQR: {q3 - q1}")

# Vježba 3
import pandas as pd
df = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [2, 4, 5, 4, 5],
    'Z': [5, 4, 3, 2, 1]
})
print(df.corr())""",
     "quiz": """[
{"question": "Box plot prikazuje?", "options": ["Min, Q1, median, Q3, max", "Samo mean", "Samo std", "Frekvencije"], "correct": 0},
{"question": "Histogram prikazuje?", "options": ["Distribuciju frekvencija", "Korelaciju", "Srednju vrijednost", "Outliere"], "correct": 0},
{"question": "Scatter plot je za?", "options": ["Odnos 2 varijable", "Proporcije", "Distribuciju", "Kategorije"], "correct": 0},
{"question": "IQR je?", "options": ["Q3 - Q1", "Max - Min", "Mean - Median", "Std * 2"], "correct": 0},
{"question": "Heatmap je koristan za?", "options": ["Vizualizaciju matrica", "Pie chart", "Histogram", "Line plot"], "correct": 0}
]"""},

    {"title": "SciPy Stats - Napredna Statistika", "order": 18, "duration_hours": 2,
     "content": """# 🔬 SciPy Stats

## scipy.stats modul
Napredne statističke funkcije i distribucije.

## describe() - Kompletan Summary
```python
from scipy import stats
result = stats.describe(data)
# nobs, minmax, mean, variance, skewness, kurtosis
```

## Linearna Regresija
```python
slope, intercept, r, p, stderr = stats.linregress(x, y)
```

## Statističke Distribucije
- **norm**: normalna distribucija
- **t**: Student's t distribucija
- **chi2**: hi-kvadrat distribucija

## Statističko Testiranje
- **ttest_1samp**: t-test za jedan uzorak
- **ttest_ind**: t-test za nezavisne uzorke
- **pearsonr**: Pearsonova korelacija + p-value
""",
     "code_example": """import numpy as np
from scipy import stats

np.random.seed(42)
x = np.random.randn(100)

print("=== scipy.stats.describe ===")
result = stats.describe(x)
print(f"Broj obs: {result.nobs}")
print(f"Min, Max: {result.minmax}")
print(f"Mean: {result.mean:.4f}")
print(f"Variance: {result.variance:.4f}")
print(f"Skewness: {result.skewness:.4f}")
print(f"Kurtosis: {result.kurtosis:.4f}")

print("\\n=== Linearna regresija ===")
x_reg = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_reg = 2 * x_reg + 1 + np.random.randn(10) * 0.5
slope, intercept, r, p, stderr = stats.linregress(x_reg, y_reg)
print(f"y = {slope:.2f}x + {intercept:.2f}")
print(f"R-squared: {r**2:.4f}")
print(f"P-value: {p:.6f}")

print("\\n=== Pearson korelacija ===")
r, p_value = stats.pearsonr(x_reg, y_reg)
print(f"Pearson r: {r:.4f}")
print(f"P-value: {p_value:.6f}")

print("\\n=== Normalna distribucija ===")
# PDF (Probability Density Function) na x=0
pdf_0 = stats.norm.pdf(0)
print(f"PDF(0): {pdf_0:.4f}")

# CDF (Cumulative Distribution Function)
cdf_0 = stats.norm.cdf(0)
print(f"CDF(0): {cdf_0:.4f}")

# Generisanje random uzorka
sample = stats.norm.rvs(loc=0, scale=1, size=5)
print(f"Random sample: {sample.round(2)}")""",
     "exercise": """## 🎯 Vježbe

### Vježba 1: Describe
Koristite scipy.stats.describe za [10, 20, 30, 40, 50, 60].

### Vježba 2: Linearna Regresija
Za x=[1,2,3,4,5] i y=[2,4,5,4,5] pronađite jednačinu regresije.

### Vježba 3: Pearson
Izračunajte Pearsonovu korelaciju i p-value za iste podatke.""",
     "exercise_solution": """# Vježba 1
from scipy import stats
import numpy as np
data = [10, 20, 30, 40, 50, 60]
result = stats.describe(data)
print(f"Mean: {result.mean}")
print(f"Variance: {result.variance}")

# Vježba 2
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
slope, intercept, r, p, se = stats.linregress(x, y)
print(f"y = {slope:.2f}x + {intercept:.2f}")

# Vježba 3
r, p_val = stats.pearsonr(x, y)
print(f"r = {r:.4f}, p = {p_val:.4f}")""",
     "quiz": """[
{"question": "scipy.stats.describe vraća?", "options": ["nobs, minmax, mean, var, skew, kurtosis", "Samo mean", "Samo var", "DataFrame"], "correct": 0},
{"question": "linregress vraća slope, intercept i?", "options": ["r, p, stderr", "Samo r", "Variance", "Mean"], "correct": 0},
{"question": "R-squared blizu 1 znači?", "options": ["Dobar fit", "Loš fit", "Nema veze", "Error"], "correct": 0},
{"question": "p-value < 0.05 znači?", "options": ["Statistički značajno", "Nije značajno", "Error", "Nema veze"], "correct": 0},
{"question": "norm.pdf(0) vraća?", "options": ["Gustoću vjerovatnoće na 0", "Kumulativnu vjerovatnoću", "Random broj", "Mean"], "correct": 0}
]"""}
]
