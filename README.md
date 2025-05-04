# TaskFlow


## 📝 Opis aplikacije

**TaskFlow** je jednostavna i pregledna To-Do aplikacija izrađena u Django frameworku. Omogućuje korisnicima da:
- Kreiraju, uređuju i brišu zadatke
- Označavaju zadatke kao dovršene
- Postave rok za svaki zadatak
- Vlastite zadatke pregledno prate kroz intuitivno korisničko sučelje

## 🗂️ Struktura projekta

- `taskflow/` – glavni direktorij projekta
- `todo/` – Django aplikacija s modelima, pogledima i obrascima za upravljanje zadacima
- `templates/todo/` – HTML predlošci (login, registracija, to-do lista, uređivanje itd.)
- `static/` – statički sadržaji poput pozadinskih slika i CSS-a

## 🧱 Model baze podataka

```python
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    deadline = models.DateField(blank=True, null=True)
```

## 🔍 Funkcionalnosti

- ✅ Dodavanje novog zadatka
- ✏️ Uređivanje postojećeg zadatka
- 🗑️ Brisanje zadatka
- ✔️ Označavanje zadatka kao dovršenog
- ⏳ Rok za zadatke (s crvenim isticanjem ako je rok prošao)
- 🔐 Prijava i registracija korisnika

## 👤 Korisnički sustav

- Registracija korisnika putem obrasca
- Login / Logout funkcionalnost
- Svaki korisnik vidi samo vlastite zadatke

## 🖼️ Sučelje

- Moderan i responzivan dizajn
- Plava pozadina s bijelim komponentama
- Prikaz popisa zadataka, jasno označen status i rok

## ⚙️ Pokretanje projekta

```bash
# Kloniraj repozitorij
git clone <url>

# Kreiraj i aktiviraj virtualno okruženje
python -m venv env
source env/Scripts/activate  # Windows

# Instaliraj potrebne pakete
pip install -r requirements.txt

# Pokreni razvojni server
python manage.py runserver
```

## 🔐 Admin pristup

- URL: `http://127.0.0.1:8000/admin`
- Korisničko ime: admin
- Lozinka: admin

## 🛡️ Sigurnost i privatnost

- Zadaci su vidljivi samo vlasniku
- Autentifikacija korisnika preko Django auth sustava

## 📸 Izgled aplikacije

U aplikaciji se koristi atraktivan login ekran, jednostavna navigacija i responsive dizajn za bolje korisničko iskustvo.

---

© 2025 TaskFlow – Sva prava pridržana.