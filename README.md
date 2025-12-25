# Python Learning Platform

Interaktivna web aplikacija za učenje Pythona kroz 7 modula i 40 časova, dizajnirana za IT profesionalce.

## 🚀 Brzi Start sa Dockerom

```bash
# Klonirajte repo i pokrenite
cd python-learning-platform
docker-compose up --build
```

Aplikacija će biti dostupna na:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Dokumentacija**: http://localhost:8000/docs

## 📚 Struktura Kursa

### DIO 1: Osnove i Skripting (18 časova)

| Modul | Naziv | Trajanje |
|-------|-------|----------|
| 1 | Osnove Python Ekosistema i Strukture Podataka | 4h |
| 2 | Funkcije, Modularnost i Rukovanje Greškama | 6h |
| 3 | Automatizacija i Rad sa Fajl Sistemom | 8h |

### DIO 2: Struktura i Napredne Tehnike (22 časa)

| Modul | Naziv | Trajanje |
|-------|-------|----------|
| 4 | Objektno-Orijentisano Programiranje (OOP) | 4h |
| 5 | Napredne Tehnike i Konkurentnost | 6h |
| 6 | Rad sa Bazama Podataka (ORM i SQL) | 6h |
| 7 | Web Razvoj i API (FastAPI) | 6h |

## 🛠️ Tehnologije

### Backend
- **FastAPI** - Moderni Python web framework
- **SQLAlchemy** - ORM za baze podataka
- **SQLite** - Ugrađena baza podataka
- **Pydantic** - Validacija podataka

### Frontend
- **React 18** - UI biblioteka
- **Vite** - Build tool
- **TailwindCSS** - CSS framework
- **React Router** - Routing
- **Lucide React** - Ikone

### DevOps
- **Docker** - Kontejnerizacija
- **Docker Compose** - Orchestracija
- **Nginx** - Web server za frontend

## 📁 Struktura Projekta

```
python-learning-platform/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI app
│   │   ├── database.py       # DB konfiguracija
│   │   ├── models.py         # SQLAlchemy modeli
│   │   ├── schemas.py        # Pydantic sheme
│   │   ├── seed_data.py      # Početni podaci
│   │   └── routers/
│   │       ├── modules.py
│   │       ├── lessons.py
│   │       ├── progress.py
│   │       └── code_runner.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── api.js
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   ├── Dockerfile
│   └── nginx.conf
├── docker-compose.yml
└── README.md
```

## 🔧 Lokalni Razvoj (bez Dockera)

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

pip install -r requirements.txt
python -c "from app.seed_data import seed_database; seed_database()"
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## 📝 API Endpoints

| Metoda | Endpoint | Opis |
|--------|----------|------|
| GET | `/api/modules/` | Lista svih modula |
| GET | `/api/modules/{id}` | Detalji modula |
| GET | `/api/lessons/module/{id}` | Lekcije po modulu |
| GET | `/api/lessons/{id}` | Detalji lekcije |
| POST | `/api/code/execute` | Izvršavanje Python koda |
| POST | `/api/progress/update` | Ažuriranje napretka |
| GET | `/api/progress/user/{id}/stats` | Statistika korisnika |

## ✨ Funkcionalnosti

- 📖 **Interaktivne lekcije** - Markdown sadržaj sa syntax highlightingom
- 💻 **Code Editor** - Pisanje i izvršavanje Python koda u browseru
- 📊 **Praćenje napretka** - Automatsko spremanje napretka po lekcijama
- 🎯 **Vježbe** - Praktične vježbe sa rješenjima
- 📱 **Responzivan dizajn** - Radi na desktop i mobilnim uređajima

## 🔐 Sigurnost Code Runnera

Code runner ima ugrađene sigurnosne mjere:
- Zabrana opasnih funkcija (`os.system`, `subprocess`, `eval`, itd.)
- Timeout od 5 sekundi
- Izolacija u sandboxu

## 📄 Licenca

MIT License
