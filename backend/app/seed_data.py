from app.database import SessionLocal, engine, Base
from app.models import Module, Lesson
from app.module12_data import MODULE_12_LESSONS

Base.metadata.create_all(bind=engine)

MODULES = [
    {"number": 1, "title": "Python Osnove", "description": "Instalacija, tipovi podataka, varijable, operatori i prvi programi.", "duration_hours": 8, "part": 1},
    {"number": 2, "title": "Strukture Podataka", "description": "Liste, tuple, rječnici, setovi i rad sa kolekcijama.", "duration_hours": 5, "part": 1},
    {"number": 3, "title": "Kontrola Toka i Petlje", "description": "If/else, for/while petlje, comprehensions.", "duration_hours": 5, "part": 1},
    {"number": 4, "title": "Funkcije", "description": "Definiranje funkcija, parametri, return, lambda.", "duration_hours": 5, "part": 1},
    {"number": 5, "title": "OOP Osnove", "description": "Klase, objekti, metode, nasljeđivanje.", "duration_hours": 6, "part": 2},
    {"number": 6, "title": "Rad sa Fajlovima", "description": "Čitanje/pisanje fajlova, JSON, CSV.", "duration_hours": 6, "part": 2},
    {"number": 7, "title": "Moduli i Paketi", "description": "Import, standardna biblioteka, pip.", "duration_hours": 6, "part": 2},
    {"number": 8, "title": "Error Handling", "description": "Try/except, custom exceptions, debugging.", "duration_hours": 6, "part": 2},
    {"number": 9, "title": "Napredni OOP", "description": "Dekorateri, property, magijske metode.", "duration_hours": 7, "part": 3},
    {"number": 10, "title": "Generatori i Iteratori", "description": "Yield, itertools, funkcionalno programiranje.", "duration_hours": 7, "part": 3},
    {"number": 11, "title": "Konkurentnost", "description": "Threading, multiprocessing, asyncio.", "duration_hours": 7, "part": 3},
    {"number": 12, "title": "Python u Statistici", "description": "NumPy, Pandas, deskriptivna statistika, korelacija, vizualizacija - 18 lekcija.", "duration_hours": 18, "part": 3},
]

LESSONS = {
    1: [
        {"title": "Instalacija i Prvi Program", "order": 1, "duration_hours": 1,
         "content": """# 🚀 Instalacija Pythona i Prvi Program

## 📚 Šta je Python?

Python je visoko-nivojski programski jezik koji je:
- 🎯 **Jednostavan za učenje** - čitljiv kao engleski
- 🔧 **Svestran** - web, data science, AI, automatizacija
- 🌍 **Popularan** - koriste ga Google, Netflix, NASA

---

## 🛠️ Instalacija Pythona

### Windows
1. Posjetite **python.org/downloads**
2. Preuzmite najnoviju verziju (3.11+)
3. ⚠️ **VAŽNO**: Označite ✅ "Add Python to PATH"
4. Kliknite "Install Now"

### Mac
```bash
brew install python3
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Provjera Instalacije
```bash
python --version
# Python 3.11.0
```

---

## 💻 Vaš Prvi Program

```python
print("Hello, World!")
```

### Pokretanje
```bash
# Interaktivni mod
python
>>> print("Hello")
Hello
>>> exit()

# Iz fajla
python hello.py
```

---

## 📝 Komentari

```python
# Jednolinjski komentar
x = 5  # Komentar na kraju

\"\"\"
Višelinijski
komentar
\"\"\"
```

---

## 🎯 Primjene Pythona

| Oblast | Biblioteke |
|--------|-----------|
| Web | Django, Flask, FastAPI |
| Data Science | Pandas, NumPy |
| ML/AI | TensorFlow, PyTorch |
| Automatizacija | Scripting |
""",
         "code_example": """# ==========================================
# PRVI PYTHON PROGRAM
# ==========================================

print("Hello, World!")
print("Dobrodošli u Python!")

print("=" * 50)

# Print sa više argumenata
print("Python", "je", "super!")

# Separator
print("2024", "01", "15", sep="-")

# Bez nove linije
print("Linija 1", end=" -> ")
print("Linija 2")

# Brojevi i tekst
print("\\nBroj:", 42)
print("Decimalni:", 3.14)

# Escape karakteri
print("\\nNova linija:\\nDruga linija")
print("Tab:\\tUvučeno")

print("\\n" + "=" * 50)
print("✅ Program završen!")""",
         "exercise": """## 🎯 Vježbe

### Vježba 1: Pozdrav
Ispišite "Zdravo" i vaše korisničko ime. Npr. ako ste "admin", ispišite: Zdravo admin!

### Vježba 2: ASCII Art
Nacrtajte kuću koristeći print():
```
   /\\
  /  \\
 |    |
 |____|
```

### Vježba 3: Vizit Karta
Napravite formatiranu vizit kartu sa okvirom.""",
         "exercise_solution": """# Vježba 1
print("Zdravo admin!")

# Vježba 2
print("   /\\\\")
print("  /  \\\\")
print(" |    |")
print(" |____|")

# Vježba 3
print("╔══════════════════════════╗")
print("║     MARKO MARKOVIĆ       ║")
print("║   Software Developer     ║")
print("╠══════════════════════════╣")
print("║  📧 marko@email.com      ║")
print("║  📱 +387 61 123 456      ║")
print("╚══════════════════════════╝")""",
         "quiz": """[
{"question": "Kako pokrenuti Python fajl?", "options": ["run program.py", "python program.py", "execute program.py", "start program.py"], "correct": 1},
{"question": "Šta radi print()?", "options": ["Čita input", "Ispisuje na ekran", "Sprema u fajl", "Briše tekst"], "correct": 1},
{"question": "Koji simbol označava komentar?", "options": ["#", "$", "/*", "--"], "correct": 1},
{"question": "Koja komanda provjerava verziju?", "options": ["python -v", "python --version", "python ver", "version python"], "correct": 1},
{"question": "Koja ekstenzija za Python fajlove?", "options": [".py", ".pyt", ".python", ".pt"], "correct": 0}
]"""},

        {"title": "Integer i Float - Brojevi", "order": 2, "duration_hours": 1,
         "content": """# 🔢 Integer i Float

## 📊 Integer (int) - Cijeli Brojevi
```python
godine = 25
negativni = -10
veliki = 1_000_000  # _ za čitljivost

print(type(godine))  # <class 'int'>
```

## 📐 Float - Decimalni Brojevi
```python
pi = 3.14159
cijena = 99.99
znanstveni = 2.5e6  # 2500000

print(type(pi))  # <class 'float'>
```

---

## 🧮 Aritmetički Operatori

| Op | Opis | Primjer | Rezultat |
|----|------|---------|----------|
| `+` | Sabiranje | `5 + 3` | `8` |
| `-` | Oduzimanje | `5 - 3` | `2` |
| `*` | Množenje | `5 * 3` | `15` |
| `/` | Dijeljenje | `5 / 2` | `2.5` |
| `//` | Cjelobrojno | `5 // 2` | `2` |
| `%` | Modulo | `5 % 2` | `1` |
| `**` | Potencija | `2 ** 3` | `8` |

---

## 🔄 Konverzija
```python
int(3.7)      # 3
float(5)      # 5.0
int("42")     # 42
float("3.14") # 3.14
```

## 📏 Korisne Funkcije
```python
abs(-5)         # 5
round(3.7)      # 4
round(3.14159, 2)  # 3.14
pow(2, 3)       # 8
min(1, 5, 3)    # 1
max(1, 5, 3)    # 5
```
""",
         "code_example": """# ==========================================
# BROJEVI - INT I FLOAT
# ==========================================

print("=" * 50)
print("🔢 INTEGER")
print("=" * 50)

godine = 25
veliki = 1_000_000
print(f"godine = {godine}, tip: {type(godine).__name__}")
print(f"veliki = {veliki}")

print("\\n" + "=" * 50)
print("📐 FLOAT")
print("=" * 50)

pi = 3.14159
cijena = 99.99
print(f"pi = {pi}, tip: {type(pi).__name__}")
print(f"cijena = {cijena}")

print("\\n" + "=" * 50)
print("🧮 OPERACIJE")
print("=" * 50)

a, b = 17, 5
print(f"a={a}, b={b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")

print("\\n" + "=" * 50)
print("📏 FUNKCIJE")
print("=" * 50)

print(f"abs(-15) = {abs(-15)}")
print(f"round(3.7) = {round(3.7)}")
print(f"round(3.14159, 2) = {round(3.14159, 2)}")
print(f"pow(2, 10) = {pow(2, 10)}")
print(f"min(5,2,8) = {min(5,2,8)}")
print(f"max(5,2,8) = {max(5,2,8)}")

print("\\n✅ Lekcija završena!")""",
         "exercise": """## 🎯 Vježbe

### Vježba 1: Kalkulator
Za a=20, b=7 ispišite sve operacije.

### Vježba 2: Temperatura
Pretvorite 25°C u Fahrenheit (F = C × 9/5 + 32).

### Vježba 3: Krug
Za r=7, izračunajte površinu (π×r²) i obim (2×π×r).

### Vježba 4: Vrijeme
157 minuta pretvorite u sate i minute.""",
         "exercise_solution": """# Vježba 1
a, b = 20, 7
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b:.2f}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")

# Vježba 2
celsius = 25
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Vježba 3
pi = 3.14159
r = 7
povrsina = pi * r ** 2
obim = 2 * pi * r
print(f"Površina: {povrsina:.2f}")
print(f"Obim: {obim:.2f}")

# Vježba 4
minuta = 157
sati = minuta // 60
ostatak = minuta % 60
print(f"{minuta} min = {sati}h {ostatak}min")""",
         "quiz": """[
{"question": "Šta vraća 10 // 3?", "options": ["3.33", "3", "4", "3.0"], "correct": 1},
{"question": "Tip broja 3.14?", "options": ["int", "float", "decimal", "number"], "correct": 1},
{"question": "Šta vraća 17 % 5?", "options": ["3", "2", "3.4", "12"], "correct": 1},
{"question": "2 na 10 u Pythonu?", "options": ["2^10", "2**10", "2*10", "pow(2)"], "correct": 1},
{"question": "round(3.7) vraća?", "options": ["3", "4", "3.7", "3.0"], "correct": 1}
]"""},

        {"title": "String - Rad sa Tekstom", "order": 3, "duration_hours": 1,
         "content": """# 📝 String - Tekst

## 📚 Kreiranje Stringa
```python
ime = "Python"
prezime = 'Programer'
dugacak = \"\"\"Višelinijski
string\"\"\"
```

## 📍 Indeksiranje
```python
tekst = "Python"
#        012345
tekst[0]   # 'P'
tekst[-1]  # 'n' (zadnji)
```

## ✂️ Slicing
```python
s = "Python"
s[0:3]   # "Pyt"
s[:3]    # "Pyt"
s[3:]    # "hon"
s[::2]   # "Pto" (svaki drugi)
s[::-1]  # "nohtyP" (obrnuto)
```

---

## 🔧 String Metode

| Metoda | Opis |
|--------|------|
| `upper()` | Velika slova |
| `lower()` | Mala slova |
| `strip()` | Ukloni razmake |
| `split()` | Razdvoji u listu |
| `join()` | Spoji listu |
| `replace()` | Zamijeni |
| `find()` | Nađi poziciju |
| `count()` | Prebroji |
| `startswith()` | Počinje sa |
| `endswith()` | Završava sa |

---

## 🔗 Konkatenacija
```python
ime = "Hello" + " " + "World"
linija = "=" * 20
```

## 📊 Provjere
```python
"123".isdigit()  # True
"abc".isalpha()  # True
"ABC".isupper()  # True
```
""",
         "code_example": """# ==========================================
# STRING - RAD SA TEKSTOM
# ==========================================

print("=" * 50)
print("📍 INDEKSIRANJE")
print("=" * 50)

tekst = "Python"
print(f"tekst = '{tekst}'")
print(f"tekst[0] = '{tekst[0]}'")
print(f"tekst[-1] = '{tekst[-1]}'")

print("\\n" + "=" * 50)
print("✂️ SLICING")
print("=" * 50)

s = "Python Programming"
print(f"s = '{s}'")
print(f"s[0:6] = '{s[0:6]}'")
print(f"s[7:] = '{s[7:]}'")
print(f"s[::2] = '{s[::2]}'")
print(f"s[::-1] = '{s[::-1]}'")

print("\\n" + "=" * 50)
print("🔧 METODE")
print("=" * 50)

ime = "  Python  "
print(f"Original: '{ime}'")
print(f"strip(): '{ime.strip()}'")
print(f"upper(): '{ime.upper()}'")
print(f"lower(): '{ime.lower()}'")

csv = "a,b,c"
print(f"\\n'{csv}'.split(',') = {csv.split(',')}")
print(f"'-'.join(['a','b','c']) = {'-'.join(['a','b','c'])}")

print("\\n" + "=" * 50)
print("🔍 PRETRAGA")
print("=" * 50)

tekst = "Hello World"
print(f"'World' in tekst: {'World' in tekst}")
print(f"tekst.find('o'): {tekst.find('o')}")
print(f"tekst.count('o'): {tekst.count('o')}")

print("\\n✅ Lekcija završena!")""",
         "exercise": """## 🎯 Vježbe

### Vježba 1: Manipulacija
Za "  Python Programming  ": strip, upper, count 'P'.

### Vježba 2: Email Parser
Iz "user@example.com" izvucite username i domain.

### Vježba 3: Obrnuti String
Obrnite "Hello World".

### Vježba 4: Cenzura
Zamijenite "password" sa "****" u tekstu.""",
         "exercise_solution": """# Vježba 1
s = "  Python Programming  "
print(f"Strip: '{s.strip()}'")
print(f"Upper: '{s.upper()}'")
print(f"Count P: {s.count('P')}")

# Vježba 2
email = "user@example.com"
username = email.split("@")[0]
domain = email.split("@")[1]
print(f"Username: {username}, Domain: {domain}")

# Vježba 3
tekst = "Hello World"
print(f"Obrnuto: {tekst[::-1]}")

# Vježba 4
original = "My password is secret"
cenzura = original.replace("password", "****")
print(cenzura)""",
         "quiz": """[
{"question": "'Python'[0] vraća?", "options": ["'Python'", "'P'", "0", "'n'"], "correct": 1},
{"question": "'Hello'[-1] vraća?", "options": ["'H'", "'e'", "'o'", "Error"], "correct": 2},
{"question": "Kako obrnuti string s?", "options": ["s.reverse()", "reverse(s)", "s[::-1]", "s[-1:0]"], "correct": 2},
{"question": "'a,b,c'.split(',') vraća?", "options": ["'abc'", "['a','b','c']", "('a','b','c')", "'a b c'"], "correct": 1},
{"question": "'hello'.upper() vraća?", "options": ["'hello'", "'HELLO'", "'Hello'", "Error"], "correct": 1}
]"""},

        {"title": "Boolean i Logički Operatori", "order": 4, "duration_hours": 1,
         "content": """# ✅ Boolean i Logički Operatori

## 📚 Boolean Tip
```python
aktivan = True
obrisan = False
print(type(aktivan))  # <class 'bool'>
```

## 🔗 Logički Operatori

| Op | Opis | Primjer |
|----|------|---------|
| `and` | Oba True | `True and False` → `False` |
| `or` | Bar jedan | `True or False` → `True` |
| `not` | Suprotno | `not True` → `False` |

---

## ⚖️ Operatori Usporedbe
```python
x = 10
x == 10   # True
x != 5    # True
x > 5     # True
x < 20    # True
x >= 10   # True
x <= 10   # True
5 < x < 15  # True (ulančavanje)
```

---

## 🔄 Truthy / Falsy

**Falsy vrijednosti:**
```python
bool(0)      # False
bool("")     # False
bool([])     # False
bool(None)   # False
```

**Truthy (sve ostalo):**
```python
bool(1)       # True
bool("hello") # True
bool([1,2])   # True
```

---

## 🚫 None
```python
rezultat = None
if rezultat is None:
    print("Nema rezultata")
```
""",
         "code_example": """# ==========================================
# BOOLEAN I LOGIČKI OPERATORI
# ==========================================

print("=" * 50)
print("✅ BOOLEAN")
print("=" * 50)

aktivan = True
obrisan = False
print(f"aktivan = {aktivan}")
print(f"obrisan = {obrisan}")
print(f"Tip: {type(aktivan)}")

print("\\n" + "=" * 50)
print("🔗 LOGIČKI OPERATORI")
print("=" * 50)

print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")

print("\\n" + "=" * 50)
print("⚖️ USPOREDBA")
print("=" * 50)

x = 10
print(f"x = {x}")
print(f"x == 10: {x == 10}")
print(f"x != 5: {x != 5}")
print(f"x > 5: {x > 5}")
print(f"5 < x < 15: {5 < x < 15}")

print("\\n" + "=" * 50)
print("🔄 TRUTHY / FALSY")
print("=" * 50)

print("Falsy:")
print(f"  bool(0) = {bool(0)}")
print(f"  bool('') = {bool('')}")
print(f"  bool([]) = {bool([])}")
print(f"  bool(None) = {bool(None)}")

print("\\nTruthy:")
print(f"  bool(1) = {bool(1)}")
print(f"  bool('hi') = {bool('hi')}")

print("\\n" + "=" * 50)
print("🚫 NONE")
print("=" * 50)

rezultat = None
print(f"rezultat is None: {rezultat is None}")

print("\\n✅ Lekcija završena!")""",
         "exercise": """## 🎯 Vježbe

### Vježba 1: Logički Operatori
Izračunajte: True and True, True and False, not False.

### Vježba 2: Provjera
Za godine=25, plata=3500: Da li je punoljetan i ima platu > 3000?

### Vježba 3: Truthy/Falsy
Provjerite bool() za: 0, 1, "", "hello", [].

### Vježba 4: None Check
Provjerite da li je varijabla None.""",
         "exercise_solution": """# Vježba 1
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"not False = {not False}")

# Vježba 2
godine = 25
plata = 3500
punoljetan = godine >= 18
dobra_plata = plata > 3000
print(f"Punoljetan i dobra plata: {punoljetan and dobra_plata}")

# Vježba 3
print(f"bool(0) = {bool(0)}")
print(f"bool(1) = {bool(1)}")
print(f"bool('') = {bool('')}")
print(f"bool('hello') = {bool('hello')}")
print(f"bool([]) = {bool([])}")

# Vježba 4
x = None
if x is None:
    print("x je None")
else:
    print(f"x = {x}")""",
         "quiz": """[
{"question": "True and False vraća?", "options": ["True", "False", "None", "Error"], "correct": 1},
{"question": "not True vraća?", "options": ["True", "False", "None", "1"], "correct": 1},
{"question": "Koja vrijednost je falsy?", "options": ["1", "'hello'", "[]", "[0]"], "correct": 2},
{"question": "Kako provjeriti None?", "options": ["x == None", "x is None", "x = None", "B je preporučeno"], "correct": 3},
{"question": "True or False vraća?", "options": ["True", "False", "None", "Error"], "correct": 0}
]"""},

        {"title": "Varijable i Imenovanje", "order": 5, "duration_hours": 1,
         "content": """# 📦 Varijable i Imenovanje

## 📚 Šta je Varijabla?
```python
ime = "Ana"     # ime pokazuje na "Ana"
godine = 25     # godine pokazuje na 25
```

## 📝 Pravila Imenovanja

✅ **Ispravno:**
```python
ime = "Ana"
broj_studenata = 30
_privatno = "secret"
MAX_SIZE = 100
```

❌ **Neispravno:**
```python
2broj = 10       # Ne može početi brojem
moj-broj = 5     # Ne može imati crticu
class = "A"      # Rezervirana riječ
```

---

## 🎨 Konvencije (PEP 8)

| Tip | Stil | Primjer |
|-----|------|---------|
| Varijable | snake_case | `user_name` |
| Konstante | SCREAMING | `MAX_SIZE` |
| Klase | PascalCase | `UserProfile` |
| Privatno | _prefix | `_internal` |

---

## 🔀 Višestruko Dodjeljivanje
```python
x = y = z = 0
a, b, c = 1, 2, 3
a, b = b, a  # Swap!
```

## 🔍 Dinamičko Tipiziranje
```python
x = 10        # int
x = "hello"   # sad je string!
```
""",
         "code_example": """# ==========================================
# VARIJABLE I IMENOVANJE
# ==========================================

print("=" * 50)
print("📦 KREIRANJE VARIJABLI")
print("=" * 50)

ime = "Marko"
godine = 28
visina = 1.82
student = True

print(f"ime = {ime}")
print(f"godine = {godine}")
print(f"visina = {visina}")
print(f"student = {student}")

print("\\n" + "=" * 50)
print("🔀 VIŠESTRUKO DODJELJIVANJE")
print("=" * 50)

x = y = z = 0
print(f"x = y = z = 0: {x}, {y}, {z}")

a, b, c = 1, 2, 3
print(f"a, b, c = 1, 2, 3: {a}, {b}, {c}")

# Swap
print(f"\\nPrije swap: a={a}, b={b}")
a, b = b, a
print(f"Poslije swap: a={a}, b={b}")

print("\\n" + "=" * 50)
print("🔍 DINAMIČKO TIPIZIRANJE")
print("=" * 50)

x = 42
print(f"x = 42, tip: {type(x).__name__}")
x = "hello"
print(f"x = 'hello', tip: {type(x).__name__}")
x = [1, 2]
print(f"x = [1,2], tip: {type(x).__name__}")

print("\\n✅ Lekcija završena!")""",
         "exercise": """## 🎯 Vježbe

### Vježba 1: Varijable
Kreirajte varijable za ime, godine, visinu. Ispišite sa tipovima.

### Vježba 2: Swap
Zamijenite a=10 i b=20 bez treće varijable.

### Vježba 3: Unpacking
Za podaci = ("Ana", 25, "Zagreb"), unpack u ime, godine, grad.

### Vježba 4: Dinamički Tip
Dodijelite x redom: int, float, string, list. Ispišite tip.""",
         "exercise_solution": """# Vježba 1
ime = "Ana"
godine = 22
visina = 1.68
print(f"ime: {ime} ({type(ime).__name__})")
print(f"godine: {godine} ({type(godine).__name__})")
print(f"visina: {visina} ({type(visina).__name__})")

# Vježba 2
a, b = 10, 20
print(f"Prije: a={a}, b={b}")
a, b = b, a
print(f"Poslije: a={a}, b={b}")

# Vježba 3
podaci = ("Ana", 25, "Zagreb")
ime, godine, grad = podaci
print(f"{ime}, {godine}, {grad}")

# Vježba 4
x = 42
print(f"x = {x}, tip: {type(x).__name__}")
x = 3.14
print(f"x = {x}, tip: {type(x).__name__}")
x = "hi"
print(f"x = {x}, tip: {type(x).__name__}")""",
         "quiz": """[
{"question": "Koje ime je neispravno?", "options": ["user_name", "_private", "2nd_value", "MAX"], "correct": 2},
{"question": "a, b = b, a radi?", "options": ["Kopiranje", "Swap", "Brisanje", "Error"], "correct": 1},
{"question": "Python je?", "options": ["Statički tipiziran", "Dinamički tipiziran", "Netipiziran", "Oba"], "correct": 1},
{"question": "Konvencija za konstante?", "options": ["camelCase", "snake_case", "SCREAMING_CASE", "PascalCase"], "correct": 2},
{"question": "x = 5; x = 'hi' je?", "options": ["Error", "Validno", "Warning", "Nemoguće"], "correct": 1}
]"""},

        {"title": "Input i Output", "order": 6, "duration_hours": 1,
         "content": """# 💬 Input i Output

## 📤 Print Funkcija
```python
print("Hello")
print("A", "B", "C")           # A B C
print("A", "B", sep="-")       # A-B
print("Hi", end=" ")           # Bez nove linije
```

## 📥 Input Funkcija
```python
ime = input("Ime: ")
godine = int(input("Godine: "))  # Konverzija!
```

⚠️ **input() uvijek vraća STRING!**

---

## 🎨 F-Strings (Formatiranje)
```python
ime = "Ana"
godine = 25

print(f"Ime: {ime}")
print(f"Za 10 god: {godine + 10}")
print(f"Pi: {3.14159:.2f}")  # 3.14
```

## 📊 Formatiranje
```python
# Poravnanje
print(f"{'lijevo':<10}|")
print(f"{'desno':>10}|")
print(f"{'centar':^10}|")

# Brojevi
print(f"{1234567:,}")    # 1,234,567
print(f"{0.856:.1%}")    # 85.6%
```
""",
         "code_example": """# ==========================================
# INPUT I OUTPUT
# ==========================================

print("=" * 50)
print("📤 PRINT FUNKCIJA")
print("=" * 50)

print("Hello, World!")
print("Python", "je", "super")
print("A", "B", "C", sep="-")
print("Linija 1", end=" | ")
print("Linija 2")

print("\\n" + "=" * 50)
print("🎨 F-STRINGS")
print("=" * 50)

ime = "Ana"
godine = 25
visina = 1.756

print(f"Ime: {ime}")
print(f"Godine: {godine}")
print(f"Visina: {visina:.2f}m")
print(f"Za 10 god: {godine + 10}")

print("\\n" + "=" * 50)
print("📊 FORMATIRANJE")
print("=" * 50)

print(f"{'lijevo':<10}|")
print(f"{'desno':>10}|")
print(f"{'centar':^10}|")

broj = 1234567.89
print(f"\\nBroj: {broj:,.2f}")
print(f"Postotak: {0.856:.1%}")

print("\\n" + "=" * 50)
print("📋 TABLICA")
print("=" * 50)

print(f"{'Proizvod':<12}{'Cijena':>10}")
print("-" * 22)
print(f"{'Jabuka':<12}{'2.50':>10}")
print(f"{'Banana':<12}{'1.80':>10}")
print(f"{'Narandža':<12}{'3.20':>10}")

print("\\n✅ Lekcija završena!")""",
         "exercise": """## 🎯 Vježbe

### Vježba 1: Print
Ispišite A-B-C koristeći sep parametar.

### Vježba 2: F-String
Formatirajte: ime, godine, visina (2 decimale).

### Vježba 3: Tablica
Napravite formatiranu tablicu 3 proizvoda sa cijenama.

### Vježba 4: Kalkulator
Simulirajte input i ispišite rezultate operacija.""",
         "exercise_solution": """# Vježba 1
print("A", "B", "C", sep="-")

# Vježba 2
ime = "Marko"
godine = 28
visina = 1.856
print(f"Ime: {ime}")
print(f"Godine: {godine}")
print(f"Visina: {visina:.2f}m")

# Vježba 3
print(f"{'Artikal':<12}{'Qty':^8}{'Cijena':>10}")
print("=" * 30)
print(f"{'Laptop':<12}{'2':^8}{'2500.00':>10}")
print(f"{'Miš':<12}{'5':^8}{'25.00':>10}")
print(f"{'Monitor':<12}{'1':^8}{'450.00':>10}")

# Vježba 4
a, b = 15, 4
print(f"a={a}, b={b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b:.2f}")""",
         "quiz": """[
{"question": "input() vraća?", "options": ["int", "float", "string", "bool"], "correct": 2},
{"question": "print('A','B',sep='-') ispisuje?", "options": ["A B", "A-B", "AB", "A, B"], "correct": 1},
{"question": "f'{3.14159:.2f}' ispisuje?", "options": ["3.14159", "3.14", "3.1", "3"], "correct": 1},
{"question": "f'{x:>10}' radi?", "options": ["Lijevo poravnanje", "Desno poravnanje", "Centar", "Error"], "correct": 1},
{"question": "print('Hi', end='') radi?", "options": ["Nova linija", "Bez nove linije", "Error", "Razmak"], "correct": 1}
]"""},

        {"title": "Type Conversion - Konverzija", "order": 7, "duration_hours": 1,
         "content": """# 🔄 Type Conversion

## 📚 Zašto Konverzija?
```python
# input() vraća string
godine = input("Godine: ")  # "25"
godine + 1  # Error! String + Int

# Rješenje: konverzija
godine = int(input("Godine: "))
godine + 1  # 26 ✓
```

---

## 🔢 U Broj
```python
# String u Int
int("42")      # 42
int("3.14")    # Error!
int(3.14)      # 3 (odsijeca decimale)

# String u Float
float("3.14")  # 3.14
float("42")    # 42.0
float(42)      # 42.0
```

## 📝 U String
```python
str(42)        # "42"
str(3.14)      # "3.14"
str(True)      # "True"
str([1, 2])    # "[1, 2]"
```

## ✅ U Boolean
```python
bool(1)        # True
bool(0)        # False
bool("hello")  # True
bool("")       # False
```

---

## 📋 U Liste/Tuple
```python
list("abc")      # ['a', 'b', 'c']
tuple([1,2,3])   # (1, 2, 3)
list((1,2,3))    # [1, 2, 3]
```

## ⚠️ Česte Greške
```python
int("hello")    # ValueError!
int("3.14")     # ValueError!
float("abc")    # ValueError!
```
""",
         "code_example": """# ==========================================
# TYPE CONVERSION
# ==========================================

print("=" * 50)
print("🔢 U BROJ")
print("=" * 50)

# String u Int
s = "42"
i = int(s)
print(f"int('{s}') = {i}, tip: {type(i).__name__}")

# String u Float
s = "3.14"
f = float(s)
print(f"float('{s}') = {f}, tip: {type(f).__name__}")

# Float u Int (odsijeca)
pi = 3.99
print(f"int({pi}) = {int(pi)}")

print("\\n" + "=" * 50)
print("📝 U STRING")
print("=" * 50)

print(f"str(42) = '{str(42)}'")
print(f"str(3.14) = '{str(3.14)}'")
print(f"str(True) = '{str(True)}'")
print(f"str([1,2,3]) = '{str([1,2,3])}'")

print("\\n" + "=" * 50)
print("✅ U BOOLEAN")
print("=" * 50)

print(f"bool(1) = {bool(1)}")
print(f"bool(0) = {bool(0)}")
print(f"bool('hello') = {bool('hello')}")
print(f"bool('') = {bool('')}")
print(f"bool([1,2]) = {bool([1,2])}")
print(f"bool([]) = {bool([])}")

print("\\n" + "=" * 50)
print("📋 LISTE / TUPLE")
print("=" * 50)

print(f"list('abc') = {list('abc')}")
print(f"tuple([1,2,3]) = {tuple([1,2,3])}")
print(f"list((1,2,3)) = {list((1,2,3))}")

print("\\n" + "=" * 50)
print("🔄 PRAKTIČNI PRIMJER")
print("=" * 50)

# Simulacija input
godine_str = "25"
godine_int = int(godine_str)
za_10_god = godine_int + 10
print(f"Input: '{godine_str}'")
print(f"Konvertirano: {godine_int}")
print(f"Za 10 godina: {za_10_god}")

print("\\n✅ Lekcija završena!")""",
         "exercise": """## 🎯 Vježbe

### Vježba 1: String u Broj
Konvertujte "123" u int i "45.67" u float.

### Vježba 2: Kalkulator
Simulirajte input dva broja (stringovi), konvertujte i saberite.

### Vježba 3: Bool Konverzija
Provjerite bool() za: 0, 1, "", "0", [], [0].

### Vježba 4: String Split
Razdvojte "10,20,30" i konvertujte u listu intova.""",
         "exercise_solution": """# Vježba 1
s1 = "123"
s2 = "45.67"
print(f"int('{s1}') = {int(s1)}")
print(f"float('{s2}') = {float(s2)}")

# Vježba 2
a_str = "15"
b_str = "25"
a = int(a_str)
b = int(b_str)
print(f"{a} + {b} = {a + b}")

# Vježba 3
print(f"bool(0) = {bool(0)}")
print(f"bool(1) = {bool(1)}")
print(f"bool('') = {bool('')}")
print(f"bool('0') = {bool('0')}")  # True! String nije prazan
print(f"bool([]) = {bool([])}")
print(f"bool([0]) = {bool([0])}")  # True! Lista nije prazna

# Vježba 4
s = "10,20,30"
lista_str = s.split(",")
lista_int = [int(x) for x in lista_str]
print(f"Original: '{s}'")
print(f"Lista int: {lista_int}")
print(f"Suma: {sum(lista_int)}")""",
         "quiz": """[
{"question": "int('3.14') vraća?", "options": ["3", "3.14", "ValueError", "0"], "correct": 2},
{"question": "str([1,2,3]) vraća?", "options": ["123", "'[1,2,3]'", "[1,2,3]", "Error"], "correct": 1},
{"question": "bool('0') vraća?", "options": ["True", "False", "0", "Error"], "correct": 0},
{"question": "int(3.99) vraća?", "options": ["4", "3", "3.99", "Error"], "correct": 1},
{"question": "float('abc') vraća?", "options": ["0.0", "abc", "ValueError", "None"], "correct": 2}
]"""},

        {"title": "Mini Projekt: Kalkulator", "order": 8, "duration_hours": 1,
         "content": """# 🎯 Mini Projekt: Kalkulator

## 📋 Zadatak
Napravite program koji:
1. Definiše dva broja
2. Izvršava sve operacije
3. Prikazuje formatirane rezultate

---

## 🧮 Operacije
- Sabiranje (+)
- Oduzimanje (-)
- Množenje (*)
- Dijeljenje (/)
- Cjelobrojno dijeljenje (//)
- Modulo (%)
- Potenciranje (**)

---

## 📊 Bonus Izazovi
1. **BMI Kalkulator** - visina i težina
2. **Pretvarač Temperature** - C ↔ F ↔ K
3. **Kalkulator Kamata** - jednostavna i složena
4. **Konverter Valuta**

---

## 💡 Savjeti
- Koristite f-stringove za formatiranje
- Zaokružite decimale na 2 mjesta
- Dodajte separatore za čitljivost
- Provjerite dijeljenje sa nulom
""",
         "code_example": """# ==========================================
# MINI PROJEKT: KALKULATOR
# ==========================================

print("╔══════════════════════════════════════════╗")
print("║           🧮 PYTHON KALKULATOR           ║")
print("╚══════════════════════════════════════════╝")

# Input (simulirano)
a = 25
b = 7

print(f"\\n📊 Operacije za a={a}, b={b}")
print("=" * 42)

# Osnovne operacije
print(f"  a + b  = {a + b}")
print(f"  a - b  = {a - b}")
print(f"  a × b  = {a * b}")
print(f"  a ÷ b  = {a / b:.4f}")
print(f"  a // b = {a // b}")
print(f"  a % b  = {a % b}")
print(f"  a ** b = {a ** b:,}")

print("\\n" + "=" * 42)
print("📐 BMI KALKULATOR")
print("=" * 42)

visina_cm = 175
tezina = 70
visina_m = visina_cm / 100
bmi = tezina / (visina_m ** 2)

if bmi < 18.5:
    kat = "Pothranjenost"
elif bmi < 25:
    kat = "Normalno"
elif bmi < 30:
    kat = "Prekomjerna"
else:
    kat = "Pretilost"

print(f"  Visina: {visina_cm} cm")
print(f"  Težina: {tezina} kg")
print(f"  BMI: {bmi:.1f} ({kat})")

print("\\n" + "=" * 42)
print("🌡️ TEMPERATURA")
print("=" * 42)

c = 25
f = c * 9/5 + 32
k = c + 273.15

print(f"  {c}°C = {f}°F = {k}K")

print("\\n" + "=" * 42)
print("💰 KAMATE")
print("=" * 42)

principal = 1000
rate = 0.05
years = 5

simple = principal * (1 + rate * years)
compound = principal * (1 + rate) ** years

print(f"  Glavnica: {principal} KM")
print(f"  Stopa: {rate:.0%}")
print(f"  Period: {years} godina")
print(f"  Jednostavna: {simple:.2f} KM")
print(f"  Složena: {compound:.2f} KM")

print("\\n╔══════════════════════════════════════════╗")
print("║           ✅ KRAJ KALKULATORA            ║")
print("╚══════════════════════════════════════════╝")""",
         "exercise": """## 🎯 Završne Vježbe

### Vježba 1: Prošireni Kalkulator
Dodajte: sqrt (korijen), abs (apsolutna vrijednost).

### Vježba 2: Konverter Jedinica
- km ↔ milje (1 km = 0.621371 milja)
- kg ↔ funte (1 kg = 2.20462 lb)

### Vježba 3: Vremenski Kalkulator
- Sekunde u sate:minute:sekunde
- Dani u sedmice i dane

### Vježba 4: Ocjena Kalkulator
- Unesi 5 ocjena
- Izračunaj prosjek
- Odredi slovo (A/B/C/D/F)""",
         "exercise_solution": """# Vježba 1: Prošireni Kalkulator
import math
x = 16
print(f"sqrt({x}) = {math.sqrt(x)}")
print(f"abs(-15) = {abs(-15)}")

# Vježba 2: Konverter
km = 100
milje = km * 0.621371
print(f"{km} km = {milje:.2f} milja")

kg = 70
lb = kg * 2.20462
print(f"{kg} kg = {lb:.2f} lb")

# Vježba 3: Vrijeme
sekunde = 3725
sati = sekunde // 3600
minuta = (sekunde % 3600) // 60
sek = sekunde % 60
print(f"{sekunde}s = {sati}h {minuta}m {sek}s")

dani = 45
sedmice = dani // 7
ostatak = dani % 7
print(f"{dani} dana = {sedmice} sedmica i {ostatak} dana")

# Vježba 4: Ocjene
ocjene = [85, 92, 78, 90, 88]
prosjek = sum(ocjene) / len(ocjene)

if prosjek >= 90:
    slovo = "A"
elif prosjek >= 80:
    slovo = "B"
elif prosjek >= 70:
    slovo = "C"
elif prosjek >= 60:
    slovo = "D"
else:
    slovo = "F"

print(f"Ocjene: {ocjene}")
print(f"Prosjek: {prosjek:.1f}")
print(f"Slovo: {slovo}")""",
         "quiz": """[
{"question": "Koja formula za BMI?", "options": ["težina * visina²", "težina / visina²", "visina / težina", "težina + visina"], "correct": 1},
{"question": "25°C u Fahrenheit?", "options": ["57°F", "77°F", "97°F", "45°F"], "correct": 1},
{"question": "125 sekundi u minute:sekunde?", "options": ["1:25", "2:05", "2:5", "1:65"], "correct": 1},
{"question": "Složena kamata koristi?", "options": ["(1 + r * n)", "(1 + r)^n", "r * n", "r^n"], "correct": 1},
{"question": "1 km = ? milja?", "options": ["1.6", "0.62", "1.0", "0.5"], "correct": 1}
]"""}
    ],
    2: [
        {"title": "Liste - Kreiranje i Indeksiranje", "order": 1, "duration_hours": 1,
         "content": """# 📋 Liste u Pythonu

## 📚 Šta je Lista?

Lista je **uređena, promjenjiva** kolekcija koja može sadržavati različite tipove podataka.

```python
# Prazna lista
prazna = []
prazna = list()

# Lista brojeva
brojevi = [1, 2, 3, 4, 5]

# Miješani tipovi
mix = [1, "hello", 3.14, True, None]
```

---

## 📍 Indeksiranje

```python
voce = ["jabuka", "banana", "narandža", "mango", "kivi"]
#        0          1          2          3        4
#       -5         -4         -3         -2       -1
```

| Izraz | Rezultat | Objašnjenje |
|-------|----------|-------------|
| `voce[0]` | "jabuka" | Prvi element |
| `voce[-1]` | "kivi" | Zadnji element |
| `voce[2]` | "narandža" | Treći element |
| `voce[-2]` | "mango" | Predzadnji |

---

## ✂️ Slicing (Rezanje)

```python
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#        lista[start:stop:step]
```

| Slice | Rezultat | Objašnjenje |
|-------|----------|-------------|
| `lista[2:5]` | [2,3,4] | Od 2 do 5 (ne uključuje 5) |
| `lista[:4]` | [0,1,2,3] | Od početka do 4 |
| `lista[6:]` | [6,7,8,9] | Od 6 do kraja |
| `lista[::2]` | [0,2,4,6,8] | Svaki drugi |
| `lista[::-1]` | [9,8,7...0] | Obrnuto |
| `lista[1:8:2]` | [1,3,5,7] | Od 1 do 8, korak 2 |

---

## 📏 Korisne Funkcije

```python
len(lista)    # Dužina
min(lista)    # Minimum
max(lista)    # Maximum
sum(lista)    # Suma
sorted(lista) # Sortirana kopija
```
""",
         "code_example": """# ==========================================
# LISTE - KREIRANJE I INDEKSIRANJE
# ==========================================

print("=" * 50)
print("📋 KREIRANJE LISTI")
print("=" * 50)

# Različiti načini kreiranja
brojevi = [1, 2, 3, 4, 5]
rijeci = ["Python", "Java", "C++"]
mix = [1, "hello", 3.14, True]
prazna = []

print(f"brojevi: {brojevi}")
print(f"rijeci: {rijeci}")
print(f"mix: {mix}")
print(f"prazna: {prazna}")

# Lista od range
od_range = list(range(1, 11))
print(f"\\nod_range: {od_range}")

print("\\n" + "=" * 50)
print("📍 INDEKSIRANJE")
print("=" * 50)

voce = ["jabuka", "banana", "narandža", "mango", "kivi"]
print(f"voce = {voce}")
print(f"voce[0] = '{voce[0]}'")
print(f"voce[2] = '{voce[2]}'")
print(f"voce[-1] = '{voce[-1]}'")
print(f"voce[-2] = '{voce[-2]}'")

print("\\n" + "=" * 50)
print("✂️ SLICING")
print("=" * 50)

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"nums = {nums}")
print(f"nums[2:6] = {nums[2:6]}")
print(f"nums[:4] = {nums[:4]}")
print(f"nums[6:] = {nums[6:]}")
print(f"nums[::2] = {nums[::2]}")
print(f"nums[::-1] = {nums[::-1]}")
print(f"nums[1:8:2] = {nums[1:8:2]}")

print("\\n" + "=" * 50)
print("📏 FUNKCIJE")
print("=" * 50)

print(f"len(nums) = {len(nums)}")
print(f"min(nums) = {min(nums)}")
print(f"max(nums) = {max(nums)}")
print(f"sum(nums) = {sum(nums)}")

print("\\n✅ Lekcija završena!")""",
         "exercise": """## 🎯 Vježbe

### Vježba 1: Osnovne Operacije
Za listu `brojevi = [10, 20, 30, 40, 50]`:
- Ispišite prvi i zadnji element
- Ispišite elemente od indeksa 1 do 3

### Vježba 2: Obrnuta Lista
Kreirajte listu [1,2,3,4,5] i ispišite je obrnutu.

### Vježba 3: Svaki Treći
Za listu 0-20, ispišite svaki treći element.

### Vježba 4: Statistika
Za listu ocjena [85, 92, 78, 90, 88], izračunajte min, max, prosjek.""",
         "exercise_solution": """# Vježba 1
brojevi = [10, 20, 30, 40, 50]
print(f"Prvi: {brojevi[0]}")
print(f"Zadnji: {brojevi[-1]}")
print(f"[1:4]: {brojevi[1:4]}")

# Vježba 2
lista = [1, 2, 3, 4, 5]
print(f"Obrnuto: {lista[::-1]}")

# Vježba 3
nums = list(range(21))
print(f"Svaki treći: {nums[::3]}")

# Vježba 4
ocjene = [85, 92, 78, 90, 88]
print(f"Min: {min(ocjene)}")
print(f"Max: {max(ocjene)}")
print(f"Prosjek: {sum(ocjene)/len(ocjene):.2f}")""",
         "quiz": """[
{"question": "lista[-1] vraća?", "options": ["Prvi element", "Zadnji element", "Error", "None"], "correct": 1},
{"question": "lista[2:5] uključuje indeks 5?", "options": ["Da", "Ne", "Zavisi", "Error"], "correct": 1},
{"question": "Kako obrnuti listu?", "options": ["lista.reverse()", "lista[::-1]", "reversed(lista)", "Svi odgovori"], "correct": 3},
{"question": "len([1, [2, 3], 4]) vraća?", "options": ["3", "4", "5", "Error"], "correct": 0},
{"question": "lista[::2] vraća?", "options": ["Svaki drugi element", "Zadnja 2", "Prva 2", "Error"], "correct": 0}
]"""},

        {"title": "Liste - Metode i Operacije", "order": 2, "duration_hours": 1,
         "content": """# 🔧 Liste - Metode i Operacije

## ➕ Dodavanje Elemenata

| Metoda | Opis | Primjer |
|--------|------|---------|
| `append(x)` | Dodaj na kraj | `lista.append(5)` |
| `insert(i, x)` | Umetni na poziciju | `lista.insert(0, "prvi")` |
| `extend(lista2)` | Dodaj sve elemente | `lista.extend([4,5,6])` |

---

## ➖ Uklanjanje Elemenata

| Metoda | Opis | Primjer |
|--------|------|---------|
| `remove(x)` | Ukloni prvu pojavu | `lista.remove("a")` |
| `pop()` | Ukloni i vrati zadnji | `zadnji = lista.pop()` |
| `pop(i)` | Ukloni na indeksu | `lista.pop(0)` |
| `clear()` | Ukloni sve | `lista.clear()` |
| `del lista[i]` | Obriši element | `del lista[2]` |

---

## 🔍 Pretraživanje

```python
lista = [1, 2, 3, 2, 4]

2 in lista          # True - provjera
lista.index(2)      # 1 - prva pozicija
lista.count(2)      # 2 - broj pojava
```

---

## 🔄 Sortiranje i Obrtanje

```python
# Na mjestu (mutira listu)
lista.sort()              # Uzlazno
lista.sort(reverse=True)  # Silazno
lista.reverse()           # Obrni

# Vraća novu listu
sorted(lista)
list(reversed(lista))
```

---

## 📋 Kopiranje

```python
# Plitka kopija
kopija = lista.copy()
kopija = lista[:]
kopija = list(lista)

# ⚠️ Ovo NIJE kopija!
ne_kopija = lista  # Ista referenca
```
""",
         "code_example": """# ==========================================
# LISTE - METODE I OPERACIJE
# ==========================================

print("=" * 50)
print("➕ DODAVANJE")
print("=" * 50)

voce = ["jabuka", "banana"]
print(f"Početno: {voce}")

voce.append("narandža")
print(f"+ append: {voce}")

voce.insert(0, "jagoda")
print(f"+ insert(0): {voce}")

voce.extend(["mango", "kivi"])
print(f"+ extend: {voce}")

print("\\n" + "=" * 50)
print("➖ UKLANJANJE")
print("=" * 50)

nums = [1, 2, 3, 4, 5, 3, 6]
print(f"Početno: {nums}")

nums.remove(3)  # Prva pojava
print(f"- remove(3): {nums}")

zadnji = nums.pop()
print(f"- pop(): {nums}, vraćeno: {zadnji}")

prvi = nums.pop(0)
print(f"- pop(0): {nums}, vraćeno: {prvi}")

print("\\n" + "=" * 50)
print("🔍 PRETRAŽIVANJE")
print("=" * 50)

lista = [10, 20, 30, 20, 40, 20]
print(f"lista = {lista}")
print(f"20 in lista: {20 in lista}")
print(f"99 in lista: {99 in lista}")
print(f"lista.index(20): {lista.index(20)}")
print(f"lista.count(20): {lista.count(20)}")

print("\\n" + "=" * 50)
print("🔄 SORTIRANJE")
print("=" * 50)

nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {nums}")

nums_sorted = sorted(nums)
print(f"sorted(): {nums_sorted}")

nums.sort()
print(f"sort(): {nums}")

nums.reverse()
print(f"reverse(): {nums}")

print("\\n✅ Lekcija završena!")""",
         "exercise": """## 🎯 Vježbe

### Vježba 1: Stack (LIFO)
Implementirajte stack koristeći append() i pop().

### Vježba 2: Queue (FIFO)
Implementirajte queue koristeći append() i pop(0).

### Vježba 3: Ukloni Duplikate
Uklonite sve duplikate iz liste [1,2,2,3,3,3,4].

### Vježba 4: Sortiranje
Sortirajte listu riječi po dužini.""",
         "exercise_solution": """# Vježba 1: Stack
stack = []
stack.append("A")
stack.append("B")
stack.append("C")
print(f"Stack: {stack}")
print(f"Pop: {stack.pop()}")
print(f"Stack: {stack}")

# Vježba 2: Queue
queue = []
queue.append("prvi")
queue.append("drugi")
queue.append("treći")
print(f"\\nQueue: {queue}")
print(f"Dequeue: {queue.pop(0)}")
print(f"Queue: {queue}")

# Vježba 3: Duplikati
lista = [1, 2, 2, 3, 3, 3, 4]
unique = list(dict.fromkeys(lista))
print(f"\\nBez duplikata: {unique}")

# Vježba 4: Sort po dužini
rijeci = ["Python", "C", "JavaScript", "Go"]
rijeci.sort(key=len)
print(f"Po dužini: {rijeci}")""",
         "quiz": """[
{"question": "append() vs extend()?", "options": ["Isto", "append dodaje 1, extend više", "extend dodaje 1", "Error"], "correct": 1},
{"question": "pop() bez argumenta uklanja?", "options": ["Prvi", "Zadnji", "Random", "Sve"], "correct": 1},
{"question": "lista.sort() vraća?", "options": ["Novu listu", "None", "Sortiranu listu", "Error"], "correct": 1},
{"question": "Kako napraviti kopiju liste?", "options": ["b = a", "b = a.copy()", "b = a[:]", "B i C"], "correct": 3},
{"question": "lista.insert(0, 'x') dodaje?", "options": ["Na kraj", "Na početak", "Random", "Error"], "correct": 1}
]"""},

        {"title": "Tuple - Nepromjenjive Sekvence", "order": 3, "duration_hours": 1,
         "content": """# 📦 Tuple - Nepromjenjive Sekvence

## 📚 Šta je Tuple?

Tuple je **uređena, nepromjenjiva** kolekcija.

```python
# Kreiranje
koordinate = (10, 20)
rgb = (255, 128, 0)
singleton = (42,)  # ⚠️ Zarez obavezan!
prazan = ()

# Bez zagrada
tacka = 10, 20, 30
```

---

## 🔒 Zašto Tuple?

| Tuple | Lista |
|-------|-------|
| Nepromjenjiv | Promjenjiv |
| Hashable (može biti ključ) | Ne može biti ključ |
| Brži | Sporiji |
| Sigurniji | Fleksibilniji |

---

## 📍 Operacije

```python
t = (1, 2, 3, 2, 4)

# Indeksiranje i slicing - isto kao lista
t[0]      # 1
t[-1]     # 4
t[1:3]    # (2, 3)

# Metode
t.count(2)  # 2
t.index(3)  # 2
len(t)      # 5
```

---

## 🔄 Unpacking

```python
# Osnovni unpacking
x, y, z = (1, 2, 3)

# Sa * operator
prvi, *srednji, zadnji = (1, 2, 3, 4, 5)
# prvi=1, srednji=[2,3,4], zadnji=5

# Swap vrijednosti
a, b = b, a

# Funkcija vraća tuple
def minmax(nums):
    return min(nums), max(nums)
```

---

## 🔗 Named Tuples

```python
from collections import namedtuple

Tacka = namedtuple('Tacka', ['x', 'y'])
p = Tacka(10, 20)
print(p.x, p.y)  # 10 20
```
""",
         "code_example": """# ==========================================
# TUPLE - NEPROMJENJIVE SEKVENCE
# ==========================================

print("=" * 50)
print("📦 KREIRANJE TUPLE")
print("=" * 50)

koordinate = (10, 20)
rgb = (255, 128, 0)
mix = (1, "hello", 3.14)
singleton = (42,)  # Jedan element

print(f"koordinate: {koordinate}")
print(f"rgb: {rgb}")
print(f"mix: {mix}")
print(f"singleton: {singleton}")
print(f"type: {type(koordinate)}")

print("\\n" + "=" * 50)
print("📍 OPERACIJE")
print("=" * 50)

t = (10, 20, 30, 20, 40, 50)
print(f"t = {t}")
print(f"t[0] = {t[0]}")
print(f"t[-1] = {t[-1]}")
print(f"t[1:4] = {t[1:4]}")
print(f"t.count(20) = {t.count(20)}")
print(f"t.index(30) = {t.index(30)}")
print(f"len(t) = {len(t)}")

print("\\n" + "=" * 50)
print("🔄 UNPACKING")
print("=" * 50)

# Osnovni
x, y, z = (1, 2, 3)
print(f"x, y, z = (1, 2, 3): x={x}, y={y}, z={z}")

# Sa * operator
prvi, *srednji, zadnji = (1, 2, 3, 4, 5)
print(f"prvi={prvi}, srednji={srednji}, zadnji={zadnji}")

# Swap
a, b = 10, 20
print(f"\\nPrije swap: a={a}, b={b}")
a, b = b, a
print(f"Poslije swap: a={a}, b={b}")

print("\\n" + "=" * 50)
print("🔗 PRAKTIČNI PRIMJERI")
print("=" * 50)

# Funkcija vraća tuple
def stats(nums):
    return min(nums), max(nums), sum(nums)/len(nums)

mn, mx, avg = stats([10, 20, 30, 40, 50])
print(f"min={mn}, max={mx}, avg={avg}")

# Tuple kao ključ rječnika
lokacije = {
    (45.8, 16.0): "Zagreb",
    (43.5, 16.4): "Split"
}
print(f"\\nLokacije: {lokacije[(45.8, 16.0)]}")

print("\\n✅ Lekcija završena!")""",
         "exercise": """## 🎯 Vježbe

### Vježba 1: Koordinate
Kreirajte tuple za 3D koordinate (x, y, z) i unpack ih.

### Vježba 2: RGB
Definirajte tuple za RGB boju i izračunajte prosjek.

### Vježba 3: Multi Return
Napišite funkciju koja vraća (min, max, sum, avg) za listu.

### Vježba 4: Swap
Zamijenite 3 varijable: a→b→c→a""",
         "exercise_solution": """# Vježba 1
tacka = (10, 20, 30)
x, y, z = tacka
print(f"x={x}, y={y}, z={z}")

# Vježba 2
rgb = (128, 64, 255)
prosjek = sum(rgb) / len(rgb)
print(f"RGB prosjek: {prosjek:.2f}")

# Vježba 3
def full_stats(nums):
    return min(nums), max(nums), sum(nums), sum(nums)/len(nums)

mn, mx, total, avg = full_stats([10, 20, 30])
print(f"min={mn}, max={mx}, sum={total}, avg={avg}")

# Vježba 4
a, b, c = 1, 2, 3
print(f"Prije: a={a}, b={b}, c={c}")
a, b, c = c, a, b
print(f"Poslije: a={a}, b={b}, c={c}")""",
         "quiz": """[
{"question": "Tuple je?", "options": ["Promjenjiv", "Nepromjenjiv", "Djelimično", "Zavisi"], "correct": 1},
{"question": "(42) je tuple?", "options": ["Da", "Ne, to je int", "Error", "Prazan tuple"], "correct": 1},
{"question": "Može li tuple biti dict ključ?", "options": ["Da", "Ne", "Samo prazan", "Samo brojevi"], "correct": 0},
{"question": "a, b = b, a radi?", "options": ["Swap", "Error", "Kopija", "Ništa"], "correct": 0},
{"question": "Kako kreirati tuple sa 1 elementom?", "options": ["(1)", "(1,)", "tuple(1)", "[1]"], "correct": 1}
]"""},

        {"title": "Set - Skupovi", "order": 4, "duration_hours": 1,
         "content": """# 🎯 Set - Skupovi

## 📚 Šta je Set?

Set je **neuređena** kolekcija **jedinstvenih** elemenata.

```python
# Kreiranje
skup = {1, 2, 3}
skup = set([1, 2, 2, 3])  # {1, 2, 3}
prazan = set()  # ⚠️ {} je prazan dict!
```

---

## ⚡ Karakteristike

- ✅ Brza pretraga O(1)
- ✅ Automatski uklanja duplikate
- ❌ Neuređen (bez indeksa)
- ❌ Elementi moraju biti hashable

---

## 🔧 Metode

| Metoda | Opis |
|--------|------|
| `add(x)` | Dodaj element |
| `remove(x)` | Ukloni (error ako nema) |
| `discard(x)` | Ukloni (bez error-a) |
| `pop()` | Ukloni random |
| `clear()` | Obriši sve |

---

## 🔗 Operacije Skupova

```python
A = {1, 2, 3}
B = {2, 3, 4}
```

| Operacija | Simbol | Rezultat |
|-----------|--------|----------|
| Unija | `A \\| B` | {1,2,3,4} |
| Presjek | `A & B` | {2,3} |
| Razlika | `A - B` | {1} |
| Sim. razlika | `A ^ B` | {1,4} |

---

## 🔍 Provjere

```python
A.issubset(B)      # A ⊆ B
A.issuperset(B)    # A ⊇ B
A.isdisjoint(B)    # A ∩ B = ∅
```
""",
         "code_example": """# ==========================================
# SET - SKUPOVI
# ==========================================

print("=" * 50)
print("🎯 KREIRANJE SETA")
print("=" * 50)

# Različiti načini
skup1 = {1, 2, 3, 4, 5}
skup2 = set([1, 2, 2, 3, 3, 3])  # Duplikati uklonjeni
slova = set("hello")  # Jedinstvena slova

print(f"skup1: {skup1}")
print(f"skup2: {skup2}")
print(f"set('hello'): {slova}")

print("\\n" + "=" * 50)
print("🔧 METODE")
print("=" * 50)

s = {1, 2, 3}
print(f"Početni: {s}")

s.add(4)
print(f"+ add(4): {s}")

s.add(2)  # Već postoji
print(f"+ add(2): {s} (bez promjene)")

s.remove(1)
print(f"- remove(1): {s}")

s.discard(99)  # Nema greške
print(f"- discard(99): {s}")

print("\\n" + "=" * 50)
print("🔗 OPERACIJE SKUPOVA")
print("=" * 50)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"A = {A}")
print(f"B = {B}")
print(f"A | B (unija): {A | B}")
print(f"A & B (presjek): {A & B}")
print(f"A - B (razlika): {A - B}")
print(f"B - A (razlika): {B - A}")
print(f"A ^ B (sim. razlika): {A ^ B}")

print("\\n" + "=" * 50)
print("🔍 PROVJERE")
print("=" * 50)

X = {1, 2}
Y = {1, 2, 3, 4}

print(f"X = {X}")
print(f"Y = {Y}")
print(f"X.issubset(Y): {X.issubset(Y)}")
print(f"Y.issuperset(X): {Y.issuperset(X)}")
print(f"3 in Y: {3 in Y}")

print("\\n" + "=" * 50)
print("💡 PRAKTIČNI PRIMJER")
print("=" * 50)

# Uklanjanje duplikata
lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(lista))
print(f"Original: {lista}")
print(f"Unique: {unique}")

print("\\n✅ Lekcija završena!")""",
         "exercise": """## 🎯 Vježbe

### Vježba 1: Ukloni Duplikate
Uklonite duplikate iz [5, 2, 8, 2, 5, 1, 8, 1].

### Vježba 2: Zajednički Elementi
Nađite zajedničke elemente: A={1,2,3,4,5}, B={4,5,6,7,8}.

### Vježba 3: Jedinstvena Slova
Nađite sva jedinstvena slova u "abracadabra".

### Vježba 4: Razlika
Korisnici sa pretplatom={Ana,Marko,Ivana}, Premium={Marko,Luka}.
Ko ima samo osnovnu pretplatu?""",
         "exercise_solution": """# Vježba 1
lista = [5, 2, 8, 2, 5, 1, 8, 1]
unique = list(set(lista))
print(f"Unique: {unique}")

# Vježba 2
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
zajednicko = A & B
print(f"Zajedničko: {zajednicko}")

# Vježba 3
rijec = "abracadabra"
slova = set(rijec)
print(f"Jedinstvena slova: {slova}")
print(f"Broj: {len(slova)}")

# Vježba 4
pretplata = {"Ana", "Marko", "Ivana"}
premium = {"Marko", "Luka"}
samo_osnovna = pretplata - premium
print(f"Samo osnovna: {samo_osnovna}")""",
         "quiz": """[
{"question": "{1, 1, 2, 2} postaje?", "options": ["{1, 1, 2, 2}", "{1, 2}", "[1, 2]", "Error"], "correct": 1},
{"question": "Prazan set se kreira?", "options": ["{}", "set()", "[]", "None"], "correct": 1},
{"question": "A & B je?", "options": ["Unija", "Presjek", "Razlika", "Komplement"], "correct": 1},
{"question": "Set elementi moraju biti?", "options": ["Brojevi", "Stringovi", "Hashable", "Bilo šta"], "correct": 2},
{"question": "A | B je?", "options": ["Unija", "Presjek", "Razlika", "XOR"], "correct": 0}
]"""},

        {"title": "Rječnici - Dict", "order": 5, "duration_hours": 1,
         "content": """# 📖 Rječnici (Dictionary)

## 📚 Šta je Dict?

Dict je **neuređena** kolekcija **ključ:vrijednost** parova.

```python
osoba = {
    "ime": "Ana",
    "godine": 25,
    "grad": "Zagreb"
}
```

---

## 📍 Pristup Vrijednostima

```python
# Pristup
osoba["ime"]       # "Ana"
osoba.get("ime")   # "Ana"
osoba.get("tel")   # None (bez greške)
osoba.get("tel", "N/A")  # "N/A" (default)

# Modifikacija
osoba["godine"] = 26
osoba["email"] = "ana@mail.com"
```

---

## 🔧 Metode

| Metoda | Opis |
|--------|------|
| `keys()` | Svi ključevi |
| `values()` | Sve vrijednosti |
| `items()` | Svi parovi |
| `pop(key)` | Ukloni i vrati |
| `update(dict2)` | Spoji rječnike |
| `setdefault(k, v)` | Postavi ako ne postoji |

---

## 🔄 Iteracija

```python
# Po ključevima
for key in d:
    print(key)

# Po vrijednostima
for val in d.values():
    print(val)

# Po parovima
for key, val in d.items():
    print(f"{key}: {val}")
```

---

## ⚡ Dict Comprehension

```python
# Kvadrati
kv = {x: x**2 for x in range(5)}
# {0:0, 1:1, 2:4, 3:9, 4:16}

# Sa filterom
parni = {x: x**2 for x in range(10) if x % 2 == 0}
```
""",
         "code_example": """# ==========================================
# RJEČNICI - DICTIONARY
# ==========================================

print("=" * 50)
print("📖 KREIRANJE")
print("=" * 50)

osoba = {
    "ime": "Marko",
    "godine": 28,
    "grad": "Split",
    "hobiji": ["programiranje", "gaming"]
}

print(f"osoba = {osoba}")
print(f"Tip: {type(osoba)}")

print("\\n" + "=" * 50)
print("📍 PRISTUP")
print("=" * 50)

print(f"osoba['ime'] = {osoba['ime']}")
print(f"osoba.get('godine') = {osoba.get('godine')}")
print(f"osoba.get('tel') = {osoba.get('tel')}")
print(f"osoba.get('tel', 'N/A') = {osoba.get('tel', 'N/A')}")

print("\\n" + "=" * 50)
print("🔧 MODIFIKACIJA")
print("=" * 50)

osoba["godine"] = 29
osoba["email"] = "marko@mail.com"
print(f"+ dodano/izmijenjeno: {osoba}")

del osoba["grad"]
print(f"- del 'grad': {osoba}")

print("\\n" + "=" * 50)
print("🔄 ITERACIJA")
print("=" * 50)

podaci = {"a": 1, "b": 2, "c": 3}

print("Ključevi:", list(podaci.keys()))
print("Vrijednosti:", list(podaci.values()))

print("\\nItems:")
for k, v in podaci.items():
    print(f"  {k} -> {v}")

print("\\n" + "=" * 50)
print("⚡ DICT COMPREHENSION")
print("=" * 50)

# Kvadrati
kvadrati = {x: x**2 for x in range(1, 6)}
print(f"Kvadrati: {kvadrati}")

# Iz dvije liste
kljucevi = ["a", "b", "c"]
vrijednosti = [1, 2, 3]
spojeno = dict(zip(kljucevi, vrijednosti))
print(f"Spojeno: {spojeno}")

print("\\n✅ Lekcija završena!")""",
         "exercise": """## 🎯 Vježbe

### Vježba 1: Kreiranje
Kreirajte dict za auto (marka, model, godina, cijena).

### Vježba 2: Iteracija
Za dict ocjena {Ana:5, Marko:4, Ivana:5}, ispišite sve.

### Vježba 3: Comprehension
Kreirajte dict gdje su ključevi 1-10, vrijednosti kubovi.

### Vježba 4: Brojanje
Prebrojite pojavljivanja slova u "abracadabra".""",
         "exercise_solution": """# Vježba 1
auto = {
    "marka": "BMW",
    "model": "X5",
    "godina": 2023,
    "cijena": 75000
}
for k, v in auto.items():
    print(f"{k}: {v}")

# Vježba 2
ocjene = {"Ana": 5, "Marko": 4, "Ivana": 5}
for ime, ocjena in ocjene.items():
    print(f"{ime}: {ocjena}")

# Vježba 3
kubovi = {x: x**3 for x in range(1, 11)}
print(f"\\nKubovi: {kubovi}")

# Vježba 4
tekst = "abracadabra"
brojac = {}
for slovo in tekst:
    brojac[slovo] = brojac.get(slovo, 0) + 1
print(f"\\nBrojač: {brojac}")""",
         "quiz": """[
{"question": "dict['key'] vs dict.get('key')?", "options": ["Isto", "[] baca error ako nema", ".get() baca error", "Oba bacaju error"], "correct": 1},
{"question": "Dict ključevi moraju biti?", "options": ["Stringovi", "Brojevi", "Hashable", "Bilo šta"], "correct": 2},
{"question": "dict.items() vraća?", "options": ["Liste ključeva", "Liste vrijednosti", "Parove (key, value)", "Dict"], "correct": 2},
{"question": "{x: x**2 for x in range(3)} vraća?", "options": ["{0, 1, 4}", "{0:0, 1:1, 2:4}", "[0, 1, 4]", "Error"], "correct": 1},
{"question": "dict.keys() vraća?", "options": ["Listu", "Set", "dict_keys view", "Tuple"], "correct": 2}
]"""},

        {"title": "Nested Strukture i JSON", "order": 6, "duration_hours": 1,
         "content": """# 🔄 Nested Strukture i JSON

## 📚 Lista Rječnika

```python
studenti = [
    {"ime": "Ana", "ocjena": 5},
    {"ime": "Marko", "ocjena": 4},
    {"ime": "Ivana", "ocjena": 5}
]

# Pristup
studenti[0]["ime"]  # "Ana"
```

---

## 📖 Rječnik sa Listama

```python
razred = {
    "naziv": "3A",
    "ucenici": ["Ana", "Marko", "Ivana"],
    "ocjene": [5, 4, 5]
}
```

---

## 🏗️ Duboko Ugnježdavanje

```python
skola = {
    "naziv": "Gimnazija",
    "razredi": [
        {
            "naziv": "3A",
            "ucenici": [
                {"ime": "Ana", "prosjek": 4.8},
                {"ime": "Marko", "prosjek": 4.2}
            ]
        }
    ]
}

# Pristup
skola["razredi"][0]["ucenici"][0]["ime"]  # "Ana"
```

---

## 📋 JSON Format

```python
import json

# Python -> JSON string
json_str = json.dumps(data, indent=2)

# JSON string -> Python
data = json.loads(json_str)

# Sa fajlom
with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json") as f:
    data = json.load(f)
```
""",
         "code_example": """# ==========================================
# NESTED STRUKTURE I JSON
# ==========================================
import json

print("=" * 50)
print("📚 LISTA RJEČNIKA")
print("=" * 50)

studenti = [
    {"ime": "Ana", "prosjek": 4.8, "predmeti": ["Math", "Fizika"]},
    {"ime": "Marko", "prosjek": 4.2, "predmeti": ["Hemija", "Bio"]},
    {"ime": "Ivana", "prosjek": 4.9, "predmeti": ["Math", "Info"]}
]

for s in studenti:
    print(f"{s['ime']}: {s['prosjek']}")

# Nađi najboljeg
najbolji = max(studenti, key=lambda x: x['prosjek'])
print(f"\\nNajbolji: {najbolji['ime']} ({najbolji['prosjek']})")

print("\\n" + "=" * 50)
print("🏗️ DUBOKO UGNJEŽDAVANJE")
print("=" * 50)

firma = {
    "naziv": "TechCorp",
    "odjeli": [
        {
            "naziv": "Development",
            "zaposlenici": [
                {"ime": "Ana", "pozicija": "Senior Dev"},
                {"ime": "Marko", "pozicija": "Junior Dev"}
            ]
        },
        {
            "naziv": "Marketing",
            "zaposlenici": [
                {"ime": "Ivana", "pozicija": "Manager"}
            ]
        }
    ]
}

print(f"Firma: {firma['naziv']}")
for odjel in firma["odjeli"]:
    print(f"\\n  Odjel: {odjel['naziv']}")
    for z in odjel["zaposlenici"]:
        print(f"    - {z['ime']} ({z['pozicija']})")

print("\\n" + "=" * 50)
print("📋 JSON")
print("=" * 50)

data = {"ime": "Test", "vrijednosti": [1, 2, 3]}

# To JSON string
json_str = json.dumps(data, indent=2)
print("JSON string:")
print(json_str)

# From JSON string
parsed = json.loads(json_str)
print(f"\\nParsed: {parsed}")
print(f"Tip: {type(parsed)}")

print("\\n✅ Lekcija završena!")""",
         "exercise": """## 🎯 Vježbe

### Vježba 1: Lista Proizvoda
Kreirajte listu od 3 proizvoda (naziv, cijena, količina).
Izračunajte ukupnu vrijednost.

### Vježba 2: Pretraga
U listi studenata, nađite sve sa prosjekom > 4.5.

### Vježba 3: JSON
Pretvorite Python dict u JSON i nazad.

### Vježba 4: Nested Update
Ažurirajte platu zaposlenika u nested strukturi.""",
         "exercise_solution": """# Vježba 1
proizvodi = [
    {"naziv": "Laptop", "cijena": 2500, "kol": 2},
    {"naziv": "Monitor", "cijena": 450, "kol": 5},
    {"naziv": "Tastatura", "cijena": 80, "kol": 10}
]
ukupno = sum(p["cijena"] * p["kol"] for p in proizvodi)
print(f"Ukupna vrijednost: {ukupno} KM")

# Vježba 2
studenti = [
    {"ime": "Ana", "prosjek": 4.8},
    {"ime": "Marko", "prosjek": 4.2},
    {"ime": "Ivana", "prosjek": 4.9}
]
odlicni = [s for s in studenti if s["prosjek"] > 4.5]
print(f"\\nOdlični: {[s['ime'] for s in odlicni]}")

# Vježba 3
import json
data = {"user": "test", "scores": [85, 90, 95]}
json_str = json.dumps(data)
print(f"\\nJSON: {json_str}")
back = json.loads(json_str)
print(f"Back: {back}")

# Vježba 4
firma = {"zaposlenici": [{"ime": "Ana", "plata": 3000}]}
firma["zaposlenici"][0]["plata"] = 3500
print(f"\\nNova plata: {firma['zaposlenici'][0]['plata']}")""",
         "quiz": """[
{"question": "studenti[0]['ime'] pristupa?", "options": ["Listi", "Prvom studentu", "Imenu prvog", "Error"], "correct": 2},
{"question": "json.dumps() vraća?", "options": ["Dict", "Lista", "String", "File"], "correct": 2},
{"question": "json.loads() prima?", "options": ["File", "Dict", "JSON string", "Lista"], "correct": 2},
{"question": "Nested struktura može imati?", "options": ["Samo 2 nivoa", "Samo 3 nivoa", "Neograničeno nivoa", "Max 5"], "correct": 2},
{"question": "json.dump() vs json.dumps()?", "options": ["Isto", "dump piše u file", "dumps piše u file", "Error"], "correct": 1}
]"""},

        {"title": "Mini Projekt: Inventar Sistema", "order": 7, "duration_hours": 1,
         "content": """# 🎯 Mini Projekt: Inventar Sistema

## 📋 Zadatak

Napravite sistem za upravljanje inventarom koji podržava:
- Dodavanje proizvoda
- Pretraga po nazivu
- Ažuriranje količine
- Statistike (ukupna vrijednost, najprodavaniji)

---

## 📊 Struktura Podataka

```python
inventar = [
    {
        "id": 1,
        "naziv": "Laptop",
        "kategorija": "Elektronika",
        "cijena": 2500.00,
        "kolicina": 10,
        "prodano": 25
    },
    ...
]
```

---

## 🔧 Funkcije

1. `dodaj_proizvod(naziv, kategorija, cijena, kolicina)`
2. `pretrazi(naziv)`
3. `azuriraj_kolicinu(id, nova_kolicina)`
4. `ukupna_vrijednost()`
5. `najprodavaniji(n=3)`

---

## 💡 Bonus

- Sortiranje po različitim kriterijima
- Export u JSON
- Filtriranje po kategoriji
""",
         "code_example": """# ==========================================
# MINI PROJEKT: INVENTAR SISTEMA
# ==========================================
import json

print("╔══════════════════════════════════════════╗")
print("║         📦 INVENTAR SISTEMA              ║")
print("╚══════════════════════════════════════════╝")

# Podaci
inventar = [
    {"id": 1, "naziv": "Laptop", "kategorija": "Elektronika", 
     "cijena": 2500, "kolicina": 10, "prodano": 25},
    {"id": 2, "naziv": "Monitor", "kategorija": "Elektronika", 
     "cijena": 450, "kolicina": 15, "prodano": 40},
    {"id": 3, "naziv": "Tastatura", "kategorija": "Periferija", 
     "cijena": 80, "kolicina": 50, "prodano": 120},
    {"id": 4, "naziv": "Miš", "kategorija": "Periferija", 
     "cijena": 40, "kolicina": 100, "prodano": 200},
    {"id": 5, "naziv": "Slušalice", "kategorija": "Audio", 
     "cijena": 150, "kolicina": 30, "prodano": 60}
]

# Funkcije
def prikazi_sve():
    print(f"\\n{'ID':<4}{'Naziv':<15}{'Kategorija':<12}{'Cijena':>10}{'Količina':>10}")
    print("-" * 55)
    for p in inventar:
        print(f"{p['id']:<4}{p['naziv']:<15}{p['kategorija']:<12}{p['cijena']:>10}{p['kolicina']:>10}")

def pretrazi(naziv):
    return [p for p in inventar if naziv.lower() in p['naziv'].lower()]

def ukupna_vrijednost():
    return sum(p['cijena'] * p['kolicina'] for p in inventar)

def najprodavaniji(n=3):
    return sorted(inventar, key=lambda x: x['prodano'], reverse=True)[:n]

def po_kategoriji():
    kategorije = {}
    for p in inventar:
        kat = p['kategorija']
        if kat not in kategorije:
            kategorije[kat] = []
        kategorije[kat].append(p['naziv'])
    return kategorije

# Demo
print("\\n📋 SVI PROIZVODI:")
prikazi_sve()

print("\\n🔍 PRETRAGA 'lap':")
rezultati = pretrazi("lap")
for r in rezultati:
    print(f"  - {r['naziv']}: {r['cijena']} KM")

print(f"\\n💰 UKUPNA VRIJEDNOST: {ukupna_vrijednost():,} KM")

print("\\n🏆 TOP 3 NAJPRODAVANIJI:")
for i, p in enumerate(najprodavaniji(3), 1):
    print(f"  {i}. {p['naziv']} ({p['prodano']} kom)")

print("\\n📂 PO KATEGORIJAMA:")
for kat, proizvodi in po_kategoriji().items():
    print(f"  {kat}: {', '.join(proizvodi)}")

print("\\n📋 JSON EXPORT:")
print(json.dumps(inventar[0], indent=2))

print("\\n✅ Projekt završen!")""",
         "exercise": """## 🎯 Proširite Projekt

### Vježba 1: Dodavanje
Implementirajte funkciju za dodavanje novog proizvoda.

### Vježba 2: Brisanje
Implementirajte funkciju za brisanje proizvoda po ID.

### Vježba 3: Ažuriranje
Funkcija za ažuriranje cijene i količine.

### Vježba 4: Statistike
Dodajte: prosječna cijena, najskuplji/najjeftiniji proizvod.""",
         "exercise_solution": """# Vježba 1: Dodavanje
def dodaj(naziv, kategorija, cijena, kolicina):
    novi_id = max(p['id'] for p in inventar) + 1
    inventar.append({
        "id": novi_id,
        "naziv": naziv,
        "kategorija": kategorija,
        "cijena": cijena,
        "kolicina": kolicina,
        "prodano": 0
    })
    print(f"Dodano: {naziv} (ID: {novi_id})")

# Vježba 2: Brisanje
def obrisi(id):
    global inventar
    inventar = [p for p in inventar if p['id'] != id]
    print(f"Obrisano ID: {id}")

# Vježba 3: Ažuriranje
def azuriraj(id, cijena=None, kolicina=None):
    for p in inventar:
        if p['id'] == id:
            if cijena: p['cijena'] = cijena
            if kolicina: p['kolicina'] = kolicina
            print(f"Ažurirano: {p['naziv']}")
            return

# Vježba 4: Statistike
def statistike():
    cijene = [p['cijena'] for p in inventar]
    print(f"Prosječna cijena: {sum(cijene)/len(cijene):.2f}")
    najskuplji = max(inventar, key=lambda x: x['cijena'])
    najjeftiniji = min(inventar, key=lambda x: x['cijena'])
    print(f"Najskuplji: {najskuplji['naziv']}")
    print(f"Najjeftiniji: {najjeftiniji['naziv']}")

statistike()""",
         "quiz": """[
{"question": "Kako sortirati po cijeni silazno?", "options": ["sort(key=cijena)", "sorted(lst, key=lambda x: x['cijena'], reverse=True)", "lst.sort(reverse)", "sorted(lst)"], "correct": 1},
{"question": "sum(p['cijena'] for p in lst) je?", "options": ["List comprehension", "Generator expression", "Lambda", "Map"], "correct": 1},
{"question": "Kako grupirati po kategoriji?", "options": ["group()", "Dict sa listama", "Set", "Tuple"], "correct": 1},
{"question": "max(lst, key=lambda x: x['prodano']) vraća?", "options": ["Broj", "Dict", "Listu", "Index"], "correct": 1},
{"question": "min(lst, key=len) radi?", "options": ["Min po vrijednosti", "Min po dužini", "Error", "Prvi element"], "correct": 1}
]"""}
    ],
    3: [
        {"title": "If/Elif/Else", "order": 1, "duration_hours": 1, "content": "# 🔀 If/Elif/Else\n\n```python\nif uvjet:\n    # True\nelif drugi:\n    # drugi True\nelse:\n    # False\n```\n\n## Operatori\n==, !=, <, >, <=, >=, and, or, not", "code_example": "ocjena = 85\n\nif ocjena >= 90:\n    rez = 'A'\nelif ocjena >= 80:\n    rez = 'B'\nelif ocjena >= 70:\n    rez = 'C'\nelse:\n    rez = 'F'\n\nprint(f'{ocjena} -> {rez}')\n\n# Ternary\nstatus = 'Prolaz' if ocjena >= 60 else 'Pad'\nprint(status)", "exercise": "Klasificirajte godine (dijete/tinejdžer/odrasli/senior).", "exercise_solution": "godine = 25\nif godine < 13:\n    kat = 'Dijete'\nelif godine < 20:\n    kat = 'Tinejdžer'\nelif godine < 60:\n    kat = 'Odrasli'\nelse:\n    kat = 'Senior'\nprint(kat)", "quiz": """[{"question": "5 < x < 10 je validno?", "options": ["Da", "Ne", "Error", "Zavisi"], "correct": 0}, {"question": "Ternary operator sintaksa?", "options": ["if x then y", "x if cond else y", "cond ? x : y", "x ? y"], "correct": 1}, {"question": "elif je skraćeno za?", "options": ["else if", "elseif", "el if", "elsif"], "correct": 0}, {"question": "Koliko elif može biti?", "options": ["1", "2", "Neograničeno", "Max 5"], "correct": 2}, {"question": "if bez else je?", "options": ["Error", "Validno", "Warning", "Nedefinirano"], "correct": 1}]"""},
        {"title": "For Petlja", "order": 2, "duration_hours": 1, "content": "# 🔄 For Petlja\n\n```python\nfor x in [1, 2, 3]:\n    print(x)\n\nfor i in range(5):\n    print(i)\n\nfor i, val in enumerate(lista):\n    print(f'{i}: {val}')\n```", "code_example": "voce = ['jabuka', 'banana', 'narandža']\n\nfor v in voce:\n    print(f'- {v}')\n\nprint('\\nSa enumerate:')\nfor i, v in enumerate(voce, 1):\n    print(f'{i}. {v}')\n\nprint('\\nRange:')\nfor i in range(1, 6):\n    print(f'{i}² = {i**2}')", "exercise": "Ispišite tablicu množenja za 7.", "exercise_solution": "for i in range(1, 11):\n    print(f'7 x {i} = {7*i}')", "quiz": """[{"question": "range(5) generira?", "options": ["1-5", "0-4", "0-5", "1-4"], "correct": 1}, {"question": "range(2, 10, 2) generira?", "options": ["2,4,6,8", "2,4,6,8,10", "0,2,4,6,8", "2,3,4...10"], "correct": 0}, {"question": "enumerate() vraća?", "options": ["Index", "Vrijednost", "Index i vrijednost", "Listu"], "correct": 2}, {"question": "for else se izvršava?", "options": ["Uvijek", "Ako nema break", "Ako ima break", "Nikad"], "correct": 1}, {"question": "Iteracija kroz dict iterira?", "options": ["Ključeve", "Vrijednosti", "Parove", "Indekse"], "correct": 0}]"""},
        {"title": "While Petlja", "order": 3, "duration_hours": 1, "content": "# 🔁 While\n\n```python\nwhile uvjet:\n    # kod\n    if nesto:\n        break     # izlaz\n    if drugo:\n        continue  # preskoči\n```", "code_example": "count = 5\nwhile count > 0:\n    print(f'{count}...')\n    count -= 1\nprint('Lansiranje!')\n\n# Sa break\nfor b in [1, 5, 3, 8, 2]:\n    if b == 8:\n        print('Pronađen!')\n        break", "exercise": "Napišite pogađanje broja.", "exercise_solution": "tajni = 7\npogodci = [3, 5, 7]\nfor p in pogodci:\n    if p == tajni:\n        print('Pogodak!')\n        break\n    elif p < tajni:\n        print('Više!')\n    else:\n        print('Manje!')", "quiz": """[{"question": "break radi?", "options": ["Izlaz iz petlje", "Nastavlja", "Pauzira", "Error"], "correct": 0}, {"question": "continue radi?", "options": ["Izlaz", "Preskače iteraciju", "Pauzira", "Restartuje"], "correct": 1}, {"question": "while True stvara?", "options": ["Error", "Beskonačnu petlju", "Ništa", "False"], "correct": 1}, {"question": "while else se izvršava?", "options": ["Uvijek", "Ako nema break", "Ako ima break", "Nikad"], "correct": 1}, {"question": "pass u petlji radi?", "options": ["Izlazi", "Preskače", "Ništa", "Error"], "correct": 2}]"""},
        {"title": "Comprehensions", "order": 4, "duration_hours": 1, "content": "# ⚡ Comprehensions\n\n```python\n# List\nkvadrati = [x**2 for x in range(5)]\n\n# Sa filterom\nparni = [x for x in range(10) if x % 2 == 0]\n\n# Dict\nd = {x: x**2 for x in range(5)}\n```", "code_example": "brojevi = [1, 2, 3, 4, 5]\n\nkvadrati = [x**2 for x in brojevi]\nprint(f'Kvadrati: {kvadrati}')\n\nparni = [x for x in brojevi if x % 2 == 0]\nprint(f'Parni: {parni}')\n\n# Dict comprehension\nkv_dict = {x: x**2 for x in range(1, 6)}\nprint(f'Dict: {kv_dict}')", "exercise": "Lista parnih kvadrata 1-20.", "exercise_solution": "parni_kv = [x**2 for x in range(1, 21) if x % 2 == 0]\nprint(parni_kv)", "quiz": """[{"question": "[x for x in lst if x>0] je?", "options": ["Map", "Filter", "Reduce", "Sort"], "correct": 1}, {"question": "[x*2 for x in lst] je?", "options": ["Map", "Filter", "Reduce", "Copy"], "correct": 0}, {"question": "{x:x**2} je?", "options": ["List comp", "Dict comp", "Set comp", "Generator"], "correct": 1}, {"question": "(x for x in lst) je?", "options": ["Tuple", "Lista", "Generator", "Error"], "correct": 2}, {"question": "Set comprehension sintaksa?", "options": ["{x}", "[x]", "(x)", "<x>"], "correct": 0}]"""},
        {"title": "Vježbe - FizzBuzz", "order": 5, "duration_hours": 1, "content": "# 🎯 FizzBuzz\n\nZa 1-30:\n- %3: Fizz\n- %5: Buzz\n- %3 i %5: FizzBuzz\n- Inače: broj", "code_example": "for i in range(1, 21):\n    if i % 3 == 0 and i % 5 == 0:\n        print('FizzBuzz', end=' ')\n    elif i % 3 == 0:\n        print('Fizz', end=' ')\n    elif i % 5 == 0:\n        print('Buzz', end=' ')\n    else:\n        print(i, end=' ')\n\nprint('\\n')\n\n# Statistike\nnums = [23, 45, 12, 67, 34]\nprint(f'Min: {min(nums)}')\nprint(f'Max: {max(nums)}')\nprint(f'Avg: {sum(nums)/len(nums):.2f}')", "exercise": "Brojanje samoglasnika u tekstu.", "exercise_solution": "tekst = 'Python programiranje'\nsamogl = 'aeiouAEIOU'\ncount = sum(1 for c in tekst if c in samogl)\nprint(f'Samoglasnika: {count}')", "quiz": """[{"question": "15 % 3 == 0 and 15 % 5 == 0?", "options": ["True", "False", "Error", "None"], "correct": 0}, {"question": "FizzBuzz za 15?", "options": ["Fizz", "Buzz", "FizzBuzz", "15"], "correct": 2}, {"question": "% operator vraća?", "options": ["Količnik", "Ostatak", "Dijeljenje", "Množenje"], "correct": 1}, {"question": "12 % 5 = ?", "options": ["2", "2.4", "7", "0"], "correct": 0}, {"question": "range(1, 31) uključuje 31?", "options": ["Da", "Ne", "Zavisi", "Error"], "correct": 1}]"""}
    ],
    4: [
        {"title": "Definiranje Funkcija", "order": 1, "duration_hours": 1, "content": "# 📦 Funkcije\n\n```python\ndef ime(parametri):\n    # kod\n    return rezultat\n```", "code_example": "def pozdrav(ime):\n    return f'Pozdrav, {ime}!'\n\ndef saberi(a, b):\n    return a + b\n\nprint(pozdrav('Ana'))\nprint(saberi(5, 3))", "exercise": "Funkcija za prosjek liste.", "exercise_solution": "def prosjek(brojevi):\n    return sum(brojevi) / len(brojevi)\n\nprint(prosjek([10, 20, 30]))", "quiz": """[{"question": "return radi?", "options": ["Ispisuje", "Vraća vrijednost", "Briše", "Pauzira"], "correct": 1}, {"question": "def označava?", "options": ["Definiciju funkcije", "Varijablu", "Klasu", "Import"], "correct": 0}, {"question": "Funkcija bez return vraća?", "options": ["0", "None", "Error", "False"], "correct": 1}, {"question": "Poziv funkcije f()?", "options": ["Definira", "Izvršava", "Briše", "Kopira"], "correct": 1}, {"question": "Funkcije su?", "options": ["First-class objekti", "Samo kod", "Samo brojevi", "Klase"], "correct": 0}]"""},
        {"title": "Parametri", "order": 2, "duration_hours": 1, "content": "# 🎯 Parametri\n\n```python\ndef f(a, b=10):  # default\n    pass\n\ndef suma(*args):  # variadic\n    return sum(args)\n\ndef info(**kwargs):  # keyword\n    pass\n```", "code_example": "def pozdrav(ime, poruka='Zdravo'):\n    return f'{poruka}, {ime}!'\n\nprint(pozdrav('Ana'))\nprint(pozdrav('Marko', 'Bok'))\n\ndef suma(*args):\n    return sum(args)\n\nprint(suma(1, 2, 3, 4, 5))", "exercise": "Funkcija *args za max.", "exercise_solution": "def maximum(*args):\n    return max(args)\n\nprint(maximum(5, 2, 8, 1))", "quiz": """[{"question": "*args prima?", "options": ["Listu", "Tuple", "Dict", "String"], "correct": 1}, {"question": "**kwargs prima?", "options": ["Listu", "Tuple", "Dict", "Set"], "correct": 2}, {"question": "Default parametar mora biti?", "options": ["Prvi", "Zadnji", "Bilo gdje", "Bez vrijednosti"], "correct": 1}, {"question": "f(1, b=2) koristi?", "options": ["Pozicijski i keyword", "Samo pozicijski", "Samo keyword", "Error"], "correct": 0}, {"question": "def f(a, *args, **kw) je?", "options": ["Validno", "Error", "Warning", "Deprecated"], "correct": 0}]"""},
        {"title": "Scope", "order": 3, "duration_hours": 1, "content": "# 🔍 Scope\n\n```python\nx = 10  # globalni\n\ndef f():\n    x = 5  # lokalni\n    return x\n\nprint(f())  # 5\nprint(x)    # 10\n```", "code_example": "x = 'globalni'\n\ndef test():\n    x = 'lokalni'\n    print(f'Unutar: {x}')\n\ntest()\nprint(f'Vani: {x}')\n\n# Višestruki return\ndef stats(nums):\n    return min(nums), max(nums), sum(nums)\n\nmn, mx, total = stats([5, 2, 8, 1])\nprint(f'Min: {mn}, Max: {mx}')", "exercise": "Funkcija vraća min, max, prosjek.", "exercise_solution": "def analiza(nums):\n    return min(nums), max(nums), sum(nums)/len(nums)\n\nmn, mx, avg = analiza([10, 20, 30])\nprint(f'{mn}, {mx}, {avg}')", "quiz": """[{"question": "LEGB znači?", "options": ["Local,Enclosing,Global,Builtin", "List,Element,Get,Bool", "Loop,Else,Go,Break", "Ništa"], "correct": 0}, {"question": "global keyword radi?", "options": ["Pristup globalnoj varijabli", "Kreira novu", "Briše", "Import"], "correct": 0}, {"question": "nonlocal koristi se za?", "options": ["Enclosing scope", "Global", "Builtin", "Local"], "correct": 0}, {"question": "Lokalna varijabla postoji?", "options": ["Samo u funkciji", "Svuda", "U modulu", "Nigdje"], "correct": 0}, {"question": "Višestruki return vraća?", "options": ["Tuple", "Listu", "Dict", "Error"], "correct": 0}]"""},
        {"title": "Lambda", "order": 4, "duration_hours": 1, "content": "# ⚡ Lambda\n\n```python\nkvadrat = lambda x: x ** 2\n\n# Sa sorted\nsorted(lst, key=lambda x: x[1])\n\n# Filter/Map\nfilter(lambda x: x>0, lst)\nmap(lambda x: x**2, lst)\n```", "code_example": "kvadrat = lambda x: x ** 2\nprint(f'kvadrat(5) = {kvadrat(5)}')\n\n# Sortiranje\nstudenti = [('Ana', 85), ('Marko', 92)]\npo_ocjeni = sorted(studenti, key=lambda x: x[1], reverse=True)\nprint(po_ocjeni)\n\n# Map/Filter\nbrojevi = [1, 2, 3, 4, 5]\nkvadrati = list(map(lambda x: x**2, brojevi))\nparni = list(filter(lambda x: x%2==0, brojevi))\nprint(f'Kvadrati: {kvadrati}')\nprint(f'Parni: {parni}')", "exercise": "Sortirajte dict listu po 'godine'.", "exercise_solution": "osobe = [{'ime': 'Ana', 'godine': 25}, {'ime': 'Marko', 'godine': 30}]\nsort = sorted(osobe, key=lambda x: x['godine'])\nprint(sort)", "quiz": """[{"question": "lambda x: x*2 je?", "options": ["Anonimna funkcija", "Klasa", "Modul", "Error"], "correct": 0}, {"question": "Lambda može imati?", "options": ["Jedan izraz", "Više izraza", "Petlje", "Klase"], "correct": 0}, {"question": "map(lambda x: x*2, lst) vraća?", "options": ["Map objekt", "Listu", "Tuple", "Dict"], "correct": 0}, {"question": "filter vraća elemente gdje?", "options": ["Lambda vraća True", "Lambda vraća False", "Sve", "Ništa"], "correct": 0}, {"question": "sorted(lst, key=len) sortira po?", "options": ["Dužini", "Vrijednosti", "Abecedi", "Random"], "correct": 0}]"""},
        {"title": "Projekt - Kalkulator", "order": 5, "duration_hours": 1, "content": "# 🎯 Kalkulator\n\nFunkcije: add, subtract, multiply, divide\ncalculate(op, a, b)", "code_example": "def add(a, b): return a + b\ndef sub(a, b): return a - b\ndef mul(a, b): return a * b\ndef div(a, b): return a / b if b != 0 else 'Error'\n\ndef calc(op, a, b):\n    ops = {'+': add, '-': sub, '*': mul, '/': div}\n    return ops.get(op, lambda a,b: 'Invalid')(a, b)\n\nprint(calc('+', 10, 5))\nprint(calc('*', 4, 3))\nprint(calc('/', 20, 4))", "exercise": "Dodajte power i modulo.", "exercise_solution": "def power(a, b): return a ** b\ndef mod(a, b): return a % b\n\nprint(power(2, 10))\nprint(mod(17, 5))", "quiz": """[{"question": "dict.get(key, default) radi?", "options": ["Vraća key ili default", "Error ako nema", "None uvijek", "Briše key"], "correct": 0}, {"question": "Funkcija kao dict vrijednost?", "options": ["Moguće", "Nemoguće", "Error", "Warning"], "correct": 0}, {"question": "Dijeljenje sa 0?", "options": ["ZeroDivisionError", "0", "Infinity", "None"], "correct": 0}, {"question": "Higher-order funkcija prima?", "options": ["Funkciju kao argument", "Samo brojeve", "Samo stringove", "Ništa"], "correct": 0}, {"question": "Callback je?", "options": ["Funkcija proslijeđena drugoj", "Klasa", "Modul", "Varijabla"], "correct": 0}]"""}
    ],
    5: [
        {"title": "Klase i Objekti", "order": 1, "duration_hours": 1, "content": "# 🏛️ OOP\n\n```python\nclass Osoba:\n    def __init__(self, ime):\n        self.ime = ime\n    \n    def pozdrav(self):\n        return f'Ja sam {self.ime}'\n```", "code_example": "class Osoba:\n    def __init__(self, ime, godine):\n        self.ime = ime\n        self.godine = godine\n    \n    def info(self):\n        return f'{self.ime}, {self.godine} god'\n\nana = Osoba('Ana', 25)\nprint(ana.info())", "exercise": "Klasa Auto sa marka, model.", "exercise_solution": "class Auto:\n    def __init__(self, marka, model):\n        self.marka = marka\n        self.model = model\n    \n    def info(self):\n        return f'{self.marka} {self.model}'\n\na = Auto('BMW', 'X5')\nprint(a.info())", "quiz": """[{"question": "__init__ je?", "options": ["Konstruktor", "Destruktor", "Metoda", "Atribut"], "correct": 0}, {"question": "self predstavlja?", "options": ["Instancu objekta", "Klasu", "Modul", "Funkciju"], "correct": 0}, {"question": "Klasa je?", "options": ["Nacrt za objekte", "Funkcija", "Modul", "Varijabla"], "correct": 0}, {"question": "obj.metoda() poziva?", "options": ["Instance metodu", "Class metodu", "Static", "Globalnu"], "correct": 0}, {"question": "Atribut instance je?", "options": ["self.var", "cls.var", "var", "@var"], "correct": 0}]"""},
        {"title": "Metode", "order": 2, "duration_hours": 1, "content": "# 🔧 Metode\n\nInstance, Class, Static metode.", "code_example": "class Krug:\n    pi = 3.14159\n    \n    def __init__(self, r):\n        self.r = r\n    \n    def povrsina(self):\n        return Krug.pi * self.r ** 2\n    \n    @classmethod\n    def from_diameter(cls, d):\n        return cls(d / 2)\n\nk = Krug(5)\nprint(f'Površina: {k.povrsina():.2f}')", "exercise": "Dodajte obim() metodu.", "exercise_solution": "def obim(self):\n    return 2 * Krug.pi * self.r", "quiz": """[{"question": "self je?", "options": ["Referenca na instancu", "Klasa", "Modul", "Funkcija"], "correct": 0}, {"question": "@classmethod prima?", "options": ["cls", "self", "this", "Ništa"], "correct": 0}, {"question": "@staticmethod prima?", "options": ["Ništa automatski", "self", "cls", "this"], "correct": 0}, {"question": "Class atribut se dijeli?", "options": ["Među svim instancama", "Samo jednoj", "Nikome", "Modulu"], "correct": 0}, {"question": "Instance metoda može pristupiti?", "options": ["self i cls", "Samo self", "Samo cls", "Ničemu"], "correct": 0}]"""},
        {"title": "Nasljeđivanje", "order": 3, "duration_hours": 2, "content": "# 🧬 Nasljeđivanje\n\n```python\nclass Student(Osoba):\n    def __init__(self, ime, fakultet):\n        super().__init__(ime)\n        self.fakultet = fakultet\n```", "code_example": "class Zivotinja:\n    def __init__(self, ime):\n        self.ime = ime\n    def zvuk(self):\n        pass\n\nclass Pas(Zivotinja):\n    def zvuk(self):\n        return 'Av!'\n\nclass Macka(Zivotinja):\n    def zvuk(self):\n        return 'Mjau!'\n\nzivotinje = [Pas('Rex'), Macka('Mica')]\nfor z in zivotinje:\n    print(f'{z.ime}: {z.zvuk()}')", "exercise": "Hijerarhija vozila.", "exercise_solution": "class Vozilo:\n    def __init__(self, marka):\n        self.marka = marka\n\nclass Auto(Vozilo):\n    def tip(self):\n        return 'Auto'\n\na = Auto('BMW')\nprint(a.tip())", "quiz": """[{"question": "super() poziva?", "options": ["Parent klasu", "Child klasu", "Self", "None"], "correct": 0}, {"question": "Python podržava?", "options": ["Višestruko nasljeđivanje", "Samo jednostruko", "Ni jedno", "Samo interfaces"], "correct": 0}, {"question": "Method overriding je?", "options": ["Redefiniranje parent metode", "Brisanje", "Kopiranje", "Import"], "correct": 0}, {"question": "isinstance(obj, Class) provjerava?", "options": ["Da li je obj instanca Class", "Tip", "Vrijednost", "Ime"], "correct": 0}, {"question": "MRO znači?", "options": ["Method Resolution Order", "Module Run Order", "Main Return Object", "Ništa"], "correct": 0}]"""},
        {"title": "Enkapsulacija", "order": 4, "duration_hours": 2, "content": "# 🔒 Enkapsulacija\n\n_protected, __private", "code_example": "class BankAccount:\n    def __init__(self, balance=0):\n        self.__balance = balance\n    \n    def deposit(self, amount):\n        if amount > 0:\n            self.__balance += amount\n    \n    def get_balance(self):\n        return self.__balance\n\nacc = BankAccount(100)\nacc.deposit(50)\nprint(acc.get_balance())", "exercise": "Dodajte withdraw.", "exercise_solution": "def withdraw(self, amount):\n    if 0 < amount <= self.__balance:\n        self.__balance -= amount\n        return True\n    return False", "quiz": """[{"question": "__var je?", "options": ["Name mangled private", "Public", "Protected", "Static"], "correct": 0}, {"question": "_var konvencija znači?", "options": ["Protected", "Private", "Public", "Static"], "correct": 0}, {"question": "Getter metoda služi za?", "options": ["Čitanje privatnog atributa", "Pisanje", "Brisanje", "Kreiranje"], "correct": 0}, {"question": "Setter metoda služi za?", "options": ["Postavljanje vrijednosti", "Čitanje", "Brisanje", "Return"], "correct": 0}, {"question": "Enkapsulacija štiti?", "options": ["Interne podatke", "Javne metode", "Module", "Funkcije"], "correct": 0}]"""}
    ],
    6: [
        {"title": "Čitanje Fajlova", "order": 1, "duration_hours": 1, "content": "# 📖 Čitanje\n\n```python\nwith open('file.txt', 'r') as f:\n    content = f.read()\n    # ili\n    lines = f.readlines()\n```", "code_example": "# Simulacija\ncontent = '''Linija 1\nLinija 2\nLinija 3'''\n\nfor line in content.split('\\n'):\n    print(line)", "exercise": "Pročitajte fajl liniju po liniju.", "exercise_solution": "for line in content.split('\\n'):\n    print(line.strip())", "quiz": """[{"question": "'r' mode je?", "options": ["Read", "Write", "Append", "Binary"], "correct": 0}, {"question": "with open() automatski?", "options": ["Zatvara fajl", "Otvara fajl", "Briše fajl", "Kreira fajl"], "correct": 0}, {"question": "f.read() vraća?", "options": ["Cijeli sadržaj", "Jednu liniju", "Listu", "Dict"], "correct": 0}, {"question": "f.readlines() vraća?", "options": ["Listu linija", "String", "Tuple", "Dict"], "correct": 0}, {"question": "'rb' mode čita?", "options": ["Binarno", "Reverse", "Random", "Read-back"], "correct": 0}]"""},
        {"title": "Pisanje Fajlova", "order": 2, "duration_hours": 1, "content": "# ✏️ Pisanje\n\n```python\nwith open('file.txt', 'w') as f:\n    f.write('Hello')\n```", "code_example": "data = ['Line 1', 'Line 2', 'Line 3']\nprint('\\n'.join(data))", "exercise": "Napišite listu u fajl.", "exercise_solution": "# with open('test.txt', 'w') as f:\n#     f.write('\\n'.join(data))\nprint('\\n'.join(data))", "quiz": """[{"question": "'w' mode?", "options": ["Overwrite fajl", "Append", "Read", "Error ako postoji"], "correct": 0}, {"question": "'a' mode?", "options": ["Append na kraj", "Overwrite", "Read", "Error"], "correct": 0}, {"question": "f.write() vraća?", "options": ["Broj zapisanih karaktera", "None", "True", "String"], "correct": 0}, {"question": "f.writelines() prima?", "options": ["Listu stringova", "Jedan string", "Int", "Dict"], "correct": 0}, {"question": "'x' mode?", "options": ["Exclusive create", "Execute", "Exit", "Extra"], "correct": 0}]"""},
        {"title": "JSON", "order": 3, "duration_hours": 2, "content": "# 📋 JSON\n\n```python\nimport json\ndata = json.loads(json_str)\njson_str = json.dumps(data)\n```", "code_example": "import json\n\ndata = {'ime': 'Ana', 'godine': 25}\njson_str = json.dumps(data, indent=2)\nprint(json_str)\n\nparsed = json.loads(json_str)\nprint(parsed['ime'])", "exercise": "Parse JSON string.", "exercise_solution": "import json\ndata = json.loads('{\"a\": 1, \"b\": 2}')\nprint(data)", "quiz": """[{"question": "json.dumps() vraća?", "options": ["JSON string", "Dict", "List", "File"], "correct": 0}, {"question": "json.loads() vraća?", "options": ["Python objekt", "String", "File", "None"], "correct": 0}, {"question": "json.dump() piše u?", "options": ["File", "String", "Console", "Memory"], "correct": 0}, {"question": "indent parametar?", "options": ["Formatiranje", "Sortiranje", "Filter", "Validacija"], "correct": 0}, {"question": "JSON podržava?", "options": ["Dict, list, str, int, float, bool, null", "Sve Python tipove", "Samo stringove", "Samo brojeve"], "correct": 0}]"""},
        {"title": "CSV", "order": 4, "duration_hours": 2, "content": "# 📊 CSV\n\n```python\nimport csv\nreader = csv.DictReader(f)\nwriter = csv.writer(f)\n```", "code_example": "import csv\nfrom io import StringIO\n\ncsv_data = 'ime,godine\\nAna,25\\nMarko,30'\nreader = csv.DictReader(StringIO(csv_data))\nfor row in reader:\n    print(row)", "exercise": "Kreirajte CSV.", "exercise_solution": "# with open('data.csv', 'w') as f:\n#     writer = csv.writer(f)\n#     writer.writerow(['ime', 'godine'])", "quiz": """[{"question": "DictReader vraća?", "options": ["Dict po redu", "Lista", "Tuple", "String"], "correct": 0}, {"question": "csv.reader vraća?", "options": ["Iterator lista", "Dict", "String", "File"], "correct": 0}, {"question": "writerow() piše?", "options": ["Jedan red", "Sve redove", "Header", "Footer"], "correct": 0}, {"question": "delimiter parametar?", "options": ["Separator polja", "Novi red", "Quote", "Escape"], "correct": 0}, {"question": "CSV header je?", "options": ["Prvi red", "Zadnji red", "Svaki red", "Ništa"], "correct": 0}]"""}
    ],
    7: [
        {"title": "Import", "order": 1, "duration_hours": 1, "content": "# 📦 Import\n\n```python\nimport modul\nfrom modul import func\nfrom modul import *\nimport modul as m\n```", "code_example": "import math\nprint(math.sqrt(16))\n\nfrom math import pi, sqrt\nprint(pi)\nprint(sqrt(25))", "exercise": "Importujte random.", "exercise_solution": "import random\nprint(random.randint(1, 10))", "quiz": """[{"question": "from x import * je?", "options": ["Import sve iz x", "Import x", "Error", "Alias"], "correct": 0}, {"question": "import x as y?", "options": ["Alias", "Kopija", "Brisanje", "Error"], "correct": 0}, {"question": "__name__ == '__main__'?", "options": ["Direktno pokretanje", "Import", "Error", "Uvijek True"], "correct": 0}, {"question": "from . import x je?", "options": ["Relativni import", "Apsolutni", "Error", "Globalni"], "correct": 0}, {"question": "sys.path sadrži?", "options": ["Putanje za module", "Sistemske putanje", "Env varijable", "Ništa"], "correct": 0}]"""},
        {"title": "Std Biblioteka", "order": 2, "duration_hours": 2, "content": "# 📚 Standardna Biblioteka\n\nos, sys, datetime, collections, itertools", "code_example": "from datetime import datetime, date\n\nnow = datetime.now()\nprint(now.strftime('%Y-%m-%d %H:%M'))\n\ntoday = date.today()\nprint(f'Danas: {today}')", "exercise": "Koristite datetime.", "exercise_solution": "from datetime import date\ntoday = date.today()\nprint(today.year)", "quiz": """[{"question": "datetime.now() vraća?", "options": ["Trenutno vrijeme", "Samo datum", "String", "Timestamp"], "correct": 0}, {"question": "os.path.join() radi?", "options": ["Spaja putanje", "Briše", "Kreira folder", "Čita fajl"], "correct": 0}, {"question": "collections.Counter broji?", "options": ["Pojavljivanja", "Elemente", "Indekse", "Tipove"], "correct": 0}, {"question": "random.choice() vraća?", "options": ["Random element", "Index", "Listu", "Boolean"], "correct": 0}, {"question": "sys.argv sadrži?", "options": ["Argumente komandne linije", "Env varijable", "Sistemske putanje", "Ništa"], "correct": 0}]"""},
        {"title": "pip", "order": 3, "duration_hours": 1, "content": "# 📥 pip\n\n```bash\npip install package\npip freeze > requirements.txt\npip install -r requirements.txt\n```", "code_example": "# requirements.txt\nprint('requests>=2.28.0')\nprint('flask>=2.0.0')\nprint('pandas>=1.5.0')", "exercise": "Napišite requirements.txt.", "exercise_solution": "print('fastapi\\nuvicorn\\npydantic')", "quiz": """[{"question": "pip freeze radi?", "options": ["Lista instaliranih paketa", "Instalira", "Briše", "Update"], "correct": 0}, {"question": "pip install -r?", "options": ["Iz requirements fajla", "Rekurzivno", "Remote", "Random"], "correct": 0}, {"question": "pip uninstall?", "options": ["Briše paket", "Instalira", "Update", "Freeze"], "correct": 0}, {"question": "pip show package?", "options": ["Info o paketu", "Instalira", "Briše", "Lista"], "correct": 0}, {"question": "pip upgrade?", "options": ["pip install --upgrade", "pip update", "pip refresh", "pip new"], "correct": 0}]"""},
        {"title": "venv", "order": 4, "duration_hours": 2, "content": "# 🔒 Virtual Environment\n\n```bash\npython -m venv venv\nsource venv/bin/activate\npip install -r requirements.txt\n```", "code_example": "print('Koraci:')\nprint('1. python -m venv venv')\nprint('2. source venv/bin/activate  # Linux/Mac')\nprint('   venv\\\\Scripts\\\\activate  # Windows')\nprint('3. pip install -r requirements.txt')", "exercise": "Napišite korake.", "exercise_solution": "print('python -m venv myenv')\nprint('source myenv/bin/activate')", "quiz": """[{"question": "venv izolira?", "options": ["Python pakete", "Sistemske fajlove", "OS", "Hardware"], "correct": 0}, {"question": "Aktivacija na Windows?", "options": ["Scripts/activate", "bin/activate", "activate.sh", "run.bat"], "correct": 0}, {"question": "deactivate radi?", "options": ["Izlaz iz venv", "Briše venv", "Kreira novi", "Ništa"], "correct": 0}, {"question": "venv folder sadrži?", "options": ["Python i pakete", "Samo pakete", "Samo Python", "Ništa"], "correct": 0}, {"question": "Zašto koristiti venv?", "options": ["Izolacija projekata", "Brže", "Obavezno", "Ljepše"], "correct": 0}]"""}
    ],
    8: [
        {"title": "Try/Except", "order": 1, "duration_hours": 1, "content": "# ⚠️ Try/Except\n\n```python\ntry:\n    risky()\nexcept Exception as e:\n    handle(e)\nfinally:\n    cleanup()\n```", "code_example": "try:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print('Ne može se dijeliti sa 0!')\nexcept Exception as e:\n    print(f'Greška: {e}')\nfinally:\n    print('Cleanup')", "exercise": "Handle ValueError.", "exercise_solution": "try:\n    x = int('abc')\nexcept ValueError:\n    print('Nije broj!')", "quiz": """[{"question": "finally se izvršava?", "options": ["Uvijek", "Samo kod error", "Nikad", "Samo kod success"], "correct": 0}, {"question": "except Exception hvata?", "options": ["Sve uobičajene greške", "Samo ValueError", "Ništa", "SystemExit"], "correct": 0}, {"question": "Redoslijed except?", "options": ["Specifični prvo", "Generalni prvo", "Bilo koji", "Abecedno"], "correct": 0}, {"question": "else u try bloku?", "options": ["Ako nema greške", "Uvijek", "Kod greške", "Nikad"], "correct": 0}, {"question": "as e u except?", "options": ["Hvata exception objekt", "Alias", "Tip", "Ništa"], "correct": 0}]"""},
        {"title": "Raise", "order": 2, "duration_hours": 1, "content": "# 🚨 Raise\n\n```python\nraise ValueError('Poruka')\n```", "code_example": "def check_age(age):\n    if age < 0:\n        raise ValueError('Negative age!')\n    return age\n\ntry:\n    check_age(-5)\nexcept ValueError as e:\n    print(e)", "exercise": "Raise za prazan string.", "exercise_solution": "def check(s):\n    if not s:\n        raise ValueError('Empty!')\n    return s", "quiz": """[{"question": "raise kreira?", "options": ["Exception", "Error poruku", "Return", "Print"], "correct": 0}, {"question": "raise bez argumenta?", "options": ["Re-raise trenutni", "Error", "None", "Pass"], "correct": 0}, {"question": "raise from e?", "options": ["Chain exceptions", "Replace", "Delete", "Copy"], "correct": 0}, {"question": "Kada koristiti raise?", "options": ["Signalizacija greške", "Return", "Print", "Exit"], "correct": 0}, {"question": "raise Exception('msg')?", "options": ["Kreira sa porukom", "Print msg", "Return msg", "Log msg"], "correct": 0}]"""},
        {"title": "Custom Exceptions", "order": 3, "duration_hours": 2, "content": "# 🎯 Custom Exception\n\n```python\nclass MyError(Exception):\n    pass\n```", "code_example": "class ValidationError(Exception):\n    pass\n\ndef validate(x):\n    if x < 0:\n        raise ValidationError('Must be positive')\n\ntry:\n    validate(-1)\nexcept ValidationError as e:\n    print(e)", "exercise": "AuthError klasa.", "exercise_solution": "class AuthError(Exception):\n    pass\n\nraise AuthError('Unauthorized')", "quiz": """[{"question": "Custom exc nasljeđuje?", "options": ["Exception", "Error", "Object", "BaseException"], "correct": 0}, {"question": "Zašto custom exceptions?", "options": ["Specifične greške", "Brže", "Obavezno", "Ljepše"], "correct": 0}, {"question": "__init__ u custom exc?", "options": ["Dodatni atributi", "Obavezno", "Zabranjeno", "Automatski"], "correct": 0}, {"question": "__str__ u custom exc?", "options": ["Custom poruka", "Obavezno", "Error", "Ništa"], "correct": 0}, {"question": "Hijerarhija custom exc?", "options": ["Moguća", "Nemoguća", "Error", "Deprecated"], "correct": 0}]"""},
        {"title": "Debugging", "order": 4, "duration_hours": 2, "content": "# 🔍 Debugging\n\nprint, logging, pdb", "code_example": "import logging\n\nlogging.basicConfig(level=logging.DEBUG)\n\nlogging.debug('Debug poruka')\nlogging.info('Info')\nlogging.warning('Warning!')\nlogging.error('Error!')", "exercise": "Koristite logging.", "exercise_solution": "import logging\nlogging.info('Starting...')\nlogging.warning('Check this')", "quiz": """[{"question": "logging.DEBUG je?", "options": ["Najniži level", "Najviši level", "Srednji", "Error only"], "correct": 0}, {"question": "logging vs print?", "options": ["Levels i formatiranje", "Isto", "Print bolje", "Logging sporije"], "correct": 0}, {"question": "pdb.set_trace()?", "options": ["Breakpoint", "Print", "Exit", "Continue"], "correct": 0}, {"question": "Level redoslijed?", "options": ["DEBUG<INFO<WARNING<ERROR", "ERROR<WARNING<INFO<DEBUG", "Svi isti", "Random"], "correct": 0}, {"question": "breakpoint() u Python 3.7+?", "options": ["Ugrađeni debugger", "Print", "Exit", "Pass"], "correct": 0}]"""}
    ],
    9: [
        {"title": "Dekorateri", "order": 1, "duration_hours": 2, "content": "# 🎀 Dekorateri\n\n```python\nfrom functools import wraps\ndef decorator(func):\n    @wraps(func)\n    def wrapper(*args):\n        return func(*args)\n    return wrapper\n\n@decorator\ndef my_func():\n    pass\n```", "code_example": "def timer(func):\n    import time\n    def wrapper(*args):\n        start = time.time()\n        result = func(*args)\n        print(f'Time: {time.time()-start:.4f}s')\n        return result\n    return wrapper\n\n@timer\ndef slow():\n    import time\n    time.sleep(0.1)\n    return 'Done'\n\nprint(slow())", "exercise": "Logger dekorator.", "exercise_solution": "def logger(func):\n    def wrapper(*args):\n        print(f'Calling {func.__name__}')\n        return func(*args)\n    return wrapper", "quiz": """[{"question": "@decorator je?", "options": ["Syntax sugar za wrapper", "Klasa", "Import", "Error"], "correct": 0}, {"question": "functools.wraps čuva?", "options": ["Metadata originalne funkcije", "Tip", "Vrijednost", "Ništa"], "correct": 0}, {"question": "Dekorator prima?", "options": ["Funkciju", "String", "Int", "Listu"], "correct": 0}, {"question": "Dekorator vraća?", "options": ["Novu funkciju", "String", "None", "Original"], "correct": 0}, {"question": "Više dekoratora?", "options": ["Moguće, donji prvo", "Nemoguće", "Gornji prvo", "Error"], "correct": 0}]"""},
        {"title": "Property", "order": 2, "duration_hours": 1, "content": "# 🏠 Property\n\n```python\n@property\ndef name(self):\n    return self._name\n\n@name.setter\ndef name(self, value):\n    self._name = value\n```", "code_example": "class Circle:\n    def __init__(self, r):\n        self._r = r\n    \n    @property\n    def radius(self):\n        return self._r\n    \n    @property\n    def area(self):\n        return 3.14 * self._r ** 2\n\nc = Circle(5)\nprint(f'R: {c.radius}')\nprint(f'Area: {c.area}')", "exercise": "Diameter property.", "exercise_solution": "@property\ndef diameter(self):\n    return self._r * 2", "quiz": """[{"question": "@property je?", "options": ["Getter dekorator", "Setter", "Deleter", "Konstruktor"], "correct": 0}, {"question": "@name.setter definira?", "options": ["Setter za property", "Novi property", "Getter", "Deleter"], "correct": 0}, {"question": "Property pristup?", "options": ["Kao atribut", "Kao metoda", "Kao klasa", "Kao modul"], "correct": 0}, {"question": "Computed property?", "options": ["Izračunata vrijednost", "Cached", "Static", "Const"], "correct": 0}, {"question": "@property bez setter?", "options": ["Read-only", "Write-only", "Error", "Ništa"], "correct": 0}]"""},
        {"title": "Magic Methods", "order": 3, "duration_hours": 2, "content": "# ✨ Dunder Methods\n\n__str__, __repr__, __eq__, __len__, __getitem__", "code_example": "class Vector:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    \n    def __str__(self):\n        return f'({self.x}, {self.y})'\n    \n    def __add__(self, other):\n        return Vector(self.x+other.x, self.y+other.y)\n\nv1 = Vector(1, 2)\nv2 = Vector(3, 4)\nprint(v1 + v2)", "exercise": "__eq__ metoda.", "exercise_solution": "def __eq__(self, other):\n    return self.x == other.x and self.y == other.y", "quiz": """[{"question": "__str__ za?", "options": ["print() i str()", "__repr__", "len()", "[]"], "correct": 0}, {"question": "__repr__ za?", "options": ["Developer prikaz", "User prikaz", "Print", "Len"], "correct": 0}, {"question": "__len__ za?", "options": ["len()", "str()", "print()", "=="], "correct": 0}, {"question": "__getitem__ za?", "options": ["obj[key]", "obj.key", "obj()", "obj+"], "correct": 0}, {"question": "__call__ za?", "options": ["obj()", "obj[]", "obj.", "obj+"], "correct": 0}]"""},
        {"title": "ABC", "order": 4, "duration_hours": 2, "content": "# 🎯 Abstract Base Class\n\n```python\nfrom abc import ABC, abstractmethod\n\nclass Shape(ABC):\n    @abstractmethod\n    def area(self):\n        pass\n```", "code_example": "from abc import ABC, abstractmethod\n\nclass Shape(ABC):\n    @abstractmethod\n    def area(self):\n        pass\n\nclass Rectangle(Shape):\n    def __init__(self, w, h):\n        self.w, self.h = w, h\n    \n    def area(self):\n        return self.w * self.h\n\nr = Rectangle(5, 3)\nprint(r.area())", "exercise": "Vehicle ABC.", "exercise_solution": "class Vehicle(ABC):\n    @abstractmethod\n    def drive(self):\n        pass", "quiz": """[{"question": "ABC ne može?", "options": ["Instancirati direktno", "Imati metode", "Nasljeđivati", "Definirati atribute"], "correct": 0}, {"question": "@abstractmethod znači?", "options": ["Mora se implementirati", "Opcionalno", "Static", "Private"], "correct": 0}, {"question": "ABC nasljeđuje?", "options": ["abc.ABC", "object", "Base", "Abstract"], "correct": 0}, {"question": "Zašto ABC?", "options": ["Definira interface", "Brže", "Manje koda", "Ljepše"], "correct": 0}, {"question": "ABC može imati?", "options": ["I abstract i konkretne metode", "Samo abstract", "Samo konkretne", "Ništa"], "correct": 0}]"""}
    ],
    10: [
        {"title": "Iteratori", "order": 1, "duration_hours": 1, "content": "# 🔄 Iteratori\n\n__iter__ i __next__", "code_example": "class Counter:\n    def __init__(self, max):\n        self.max = max\n        self.n = 0\n    \n    def __iter__(self):\n        return self\n    \n    def __next__(self):\n        if self.n >= self.max:\n            raise StopIteration\n        self.n += 1\n        return self.n\n\nfor i in Counter(5):\n    print(i)", "exercise": "Countdown iterator.", "exercise_solution": "class Countdown:\n    def __init__(self, start):\n        self.n = start\n    def __iter__(self):\n        return self\n    def __next__(self):\n        if self.n <= 0:\n            raise StopIteration\n        self.n -= 1\n        return self.n + 1", "quiz": """[{"question": "StopIteration znači?", "options": ["Kraj iteracije", "Error", "Pauza", "Restart"], "correct": 0}, {"question": "__iter__ vraća?", "options": ["Iterator objekt", "Listu", "Tuple", "Dict"], "correct": 0}, {"question": "__next__ vraća?", "options": ["Sljedeći element", "Prethodni", "Sve", "Ništa"], "correct": 0}, {"question": "iter(lista) vraća?", "options": ["Iterator", "Listu", "Kopiju", "None"], "correct": 0}, {"question": "next(it) bez elemenata?", "options": ["StopIteration", "None", "Error", "0"], "correct": 0}]"""},
        {"title": "Generatori", "order": 2, "duration_hours": 2, "content": "# ⚡ Generatori\n\n```python\ndef gen():\n    yield 1\n    yield 2\n```", "code_example": "def fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        yield a\n        a, b = b, a + b\n\nprint(list(fibonacci(10)))", "exercise": "Generator parnih.", "exercise_solution": "def evens(n):\n    for i in range(0, n, 2):\n        yield i\n\nprint(list(evens(20)))", "quiz": """[{"question": "yield vs return?", "options": ["Pauzira funkciju", "Završava", "Isto", "Error"], "correct": 0}, {"question": "Generator je?", "options": ["Lazy iterator", "Lista", "Tuple", "Dict"], "correct": 0}, {"question": "Generator expression?", "options": ["(x for x in lst)", "[x for x in lst]", "{x for x in lst}", "x for x in lst"], "correct": 0}, {"question": "Generator prednost?", "options": ["Memory efikasnost", "Brzina", "Čitljivost", "Ništa"], "correct": 0}, {"question": "send() u generator?", "options": ["Šalje vrijednost", "Prima", "Briše", "Restart"], "correct": 0}]"""},
        {"title": "itertools", "order": 3, "duration_hours": 2, "content": "# 🧰 itertools\n\ncount, cycle, chain, combinations, permutations", "code_example": "from itertools import count, islice, combinations\n\n# Beskonačni count\ncounter = count(1)\nprint(list(islice(counter, 5)))\n\n# Kombinacije\nprint(list(combinations([1,2,3], 2)))", "exercise": "Permutacije.", "exercise_solution": "from itertools import permutations\nprint(list(permutations([1,2,3], 2)))", "quiz": """[{"question": "count() je?", "options": ["Beskonačan iterator", "Konačan", "Error", "Lista"], "correct": 0}, {"question": "cycle() radi?", "options": ["Beskonačno ponavlja", "Jednom", "Broji", "Sortira"], "correct": 0}, {"question": "chain() radi?", "options": ["Spaja iteratore", "Filtrira", "Mapira", "Sortira"], "correct": 0}, {"question": "combinations(lst, 2)?", "options": ["Sve kombinacije po 2", "Permutacije", "Product", "Zip"], "correct": 0}, {"question": "islice() radi?", "options": ["Slicing na iterator", "Filter", "Map", "Sort"], "correct": 0}]"""},
        {"title": "FP", "order": 4, "duration_hours": 2, "content": "# 🎯 Funkcionalno\n\nmap, filter, reduce", "code_example": "from functools import reduce\n\nnums = [1, 2, 3, 4, 5]\n\nproduct = reduce(lambda x, y: x * y, nums)\nprint(f'Product: {product}')\n\nsquares = list(map(lambda x: x**2, nums))\nprint(f'Squares: {squares}')", "exercise": "Reduce za sumu.", "exercise_solution": "total = reduce(lambda x, y: x + y, [1,2,3,4,5])\nprint(total)", "quiz": """[{"question": "reduce() vraća?", "options": ["Jednu vrijednost", "Listu", "Iterator", "Dict"], "correct": 0}, {"question": "map() vraća?", "options": ["Map objekt", "Listu", "Tuple", "Dict"], "correct": 0}, {"question": "filter() vraća?", "options": ["Filter objekt", "Listu", "Bool", "Int"], "correct": 0}, {"question": "functools.partial?", "options": ["Fiksira argumente", "Filtrira", "Mapira", "Reduce"], "correct": 0}, {"question": "Pure function?", "options": ["Bez side effects", "Sa side effects", "Async", "Generator"], "correct": 0}]"""}
    ],
    11: [
        {"title": "Threading", "order": 1, "duration_hours": 2, "content": "# 🧵 Threading\n\n```python\nimport threading\nt = threading.Thread(target=func)\nt.start()\nt.join()\n```", "code_example": "import threading\nimport time\n\ndef task(name):\n    print(f'{name} starting')\n    time.sleep(0.1)\n    print(f'{name} done')\n\nt1 = threading.Thread(target=task, args=('A',))\nt2 = threading.Thread(target=task, args=('B',))\n\nt1.start()\nt2.start()\nt1.join()\nt2.join()\nprint('All done')", "exercise": "3 threada.", "exercise_solution": "threads = []\nfor i in range(3):\n    t = threading.Thread(target=task, args=(f'T{i}',))\n    threads.append(t)\n    t.start()\nfor t in threads:\n    t.join()", "quiz": """[{"question": "join() čeka?", "options": ["Da thread završi", "Start thread", "Stop thread", "Kill thread"], "correct": 0}, {"question": "GIL u Pythonu?", "options": ["Global Interpreter Lock", "Global Int Lock", "Get Int Lock", "Ništa"], "correct": 0}, {"question": "Threading za?", "options": ["I/O bound zadatke", "CPU bound", "Sve", "Ništa"], "correct": 0}, {"question": "daemon thread?", "options": ["Završava sa main", "Nikad ne završava", "Prioritetan", "Sporiji"], "correct": 0}, {"question": "Lock() služi za?", "options": ["Sinkronizaciju", "Start", "Stop", "Join"], "correct": 0}]"""},
        {"title": "Multiprocessing", "order": 2, "duration_hours": 2, "content": "# 🔀 Multiprocessing\n\n```python\nfrom multiprocessing import Pool\nwith Pool(4) as p:\n    results = p.map(func, data)\n```", "code_example": "def square(x):\n    return x ** 2\n\n# Simulacija (bez multiprocessing u web env)\nnums = [1, 2, 3, 4, 5]\nresults = list(map(square, nums))\nprint(results)", "exercise": "Pool map.", "exercise_solution": "# with Pool(4) as p:\n#     results = p.map(square, range(10))\nresults = list(map(square, range(10)))\nprint(results)", "quiz": """[{"question": "Pool koristi?", "options": ["Procese", "Threadove", "Async", "Coroutines"], "correct": 0}, {"question": "Multiprocessing za?", "options": ["CPU bound", "I/O bound", "Ništa", "Samo threading"], "correct": 0}, {"question": "Pool.map() vraća?", "options": ["Listu rezultata", "Iterator", "Process", "Thread"], "correct": 0}, {"question": "Process vs Thread?", "options": ["Odvojeni memory", "Dijeljeni memory", "Isto", "Ništa"], "correct": 0}, {"question": "Pool(4) kreira?", "options": ["4 worker procesa", "4 threada", "4 taska", "4 coroutine"], "correct": 0}]"""},
        {"title": "Asyncio", "order": 3, "duration_hours": 2, "content": "# ⚡ Asyncio\n\n```python\nasync def main():\n    await asyncio.sleep(1)\n\nasyncio.run(main())\n```", "code_example": "import asyncio\n\nasync def greet(name, delay):\n    await asyncio.sleep(delay)\n    return f'Hello, {name}'\n\n# async def main():\n#     result = await greet('World', 1)\n#     print(result)\n\nprint('Asyncio primer (ne radi u web env)')", "exercise": "Async funkcija.", "exercise_solution": "async def fetch():\n    await asyncio.sleep(1)\n    return 'data'", "quiz": """[{"question": "await čeka?", "options": ["Async operaciju", "Thread", "Process", "Sync funkciju"], "correct": 0}, {"question": "async def kreira?", "options": ["Coroutine", "Thread", "Process", "Generator"], "correct": 0}, {"question": "asyncio.run() radi?", "options": ["Pokreće event loop", "Kreira thread", "Kreira process", "Return"], "correct": 0}, {"question": "Asyncio za?", "options": ["I/O bound sa mnogo konekcija", "CPU bound", "Threading", "Multiprocessing"], "correct": 0}, {"question": "Event loop je?", "options": ["Upravljač coroutina", "Thread pool", "Process pool", "Memory"], "correct": 0}]"""},
        {"title": "Async Patterns", "order": 4, "duration_hours": 1, "content": "# 🎯 Patterns\n\ngather, create_task, wait", "code_example": "# async def main():\n#     tasks = [greet(f'User{i}', 0.1) for i in range(3)]\n#     results = await asyncio.gather(*tasks)\n#     print(results)\n\nprint('Async gather primer')", "exercise": "gather primjer.", "exercise_solution": "# results = await asyncio.gather(task1(), task2())", "quiz": """[{"question": "gather() radi?", "options": ["Paralelno izvršava", "Sekvencijalno", "Random", "Blokira"], "correct": 0}, {"question": "create_task() vraća?", "options": ["Task objekt", "Coroutine", "Result", "None"], "correct": 0}, {"question": "asyncio.wait() vs gather?", "options": ["Više kontrole", "Isto", "Manje kontrole", "Deprecated"], "correct": 0}, {"question": "Task.cancel() radi?", "options": ["Otkazuje task", "Pauzira", "Restartuje", "Join"], "correct": 0}, {"question": "async with za?", "options": ["Async context manager", "Sync CM", "Loop", "Error"], "correct": 0}]"""}
    ],
    12: MODULE_12_LESSONS
}

def seed_database():
    db = SessionLocal()
    try:
        if db.query(Module).count() > 0:
            print("Database already seeded!")
            return
        for mod_data in MODULES:
            module = Module(**mod_data)
            db.add(module)
        db.commit()
        for mod in db.query(Module).all():
            if mod.number in LESSONS:
                for lesson_data in LESSONS[mod.number]:
                    lesson = Lesson(module_id=mod.id, **lesson_data)
                    db.add(lesson)
        db.commit()
        print(f"Seeded {len(MODULES)} modules!")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
