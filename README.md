# TaskFlow

## 📝 Opis aplikacije

**TaskFlow** je pregledna i funkcionalna To-Do aplikacija izrađena u Django frameworku. Omogućuje korisnicima da:
- Kreiraju, uređuju i brišu zadatke
- Označavaju zadatke kao dovršene
- Postave rok za svaki zadatak
- Organiziraju zadatke po listama
- Dijele liste zadataka s drugim korisnicima
- Vide tko je vlasnik liste i tko može uređivati
- Primaju obavijesti ako pokušaju mijenjati tuđe zadatke/liste 😅

## 🗂️ Struktura projekta

- `taskflow/` – glavni direktorij projekta
- `todo/` – Django aplikacija s modelima, pogledima i obrascima
- `templates/todo/` – HTML predlošci za prikaz sučelja
- `static/` – statički sadržaji poput CSS-a i slika

## 🧱 Model baze podataka (osnovni primjer)

```python
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    deadline = models.DateField(blank=True, null=True)
    list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

class TaskList(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name="shared_lists", blank=True)
```

## 🔍 Funkcionalnosti

- ✅ Dodavanje novog zadatka
- ✏️ Uređivanje i brisanje zadatka
- ✔️ Označavanje zadatka kao dovršenog
- ⏳ Rok za zadatke s isticanjem (crveno ako je prošao)
- 📋 Organizacija po task listama
- 🔗 Dijeljenje lista s drugim korisnicima
- 🚫 Modal upozorenje ako korisnik pokušava mijenjati tuđe zadatke/liste
- 🎨 Intuitivno korisničko sučelje s animacijama i modernim dizajnom

## 👤 Korisnički sustav

- Registracija i login/logout funkcionalnosti
- Svaki korisnik vidi svoje liste i zadatke ili one koje su mu podijeljene
- Prava uređivanja samo ako je korisnik vlasnik liste/zadatka

## 🖼️ Sučelje

- Moderno, responzivno i prilagođeno korisniku
- Pozadina s efektom zamućenja
- Karte s listama i zadacima
- Animirani hover efekti
- Modal prozori za uređivanje i upozorenja

## ⚙️ Pokretanje projekta

```bash
# Kloniraj repozitorij
git clone <url>

# Kreiraj virtualno okruženje i aktiviraj ga
python -m venv env
source env/Scripts/activate  # na Windowsu

# Instaliraj ovisnosti
pip install -r requirements.txt

# Pokreni razvojni server
python manage.py runserver
```

## 🔐 Admin pristup (lokalno)

- URL: `http://127.0.0.1:8000/admin`
- Korisničko ime: adminSlava
- Lozinka: admin

## 🛡️ Sigurnost i ograničenja

- Zadaci i liste vidljivi samo vlasnicima ili korisnicima s kojima su podijeljeni
- Ako korisnik pokuša uređivati nešto što ne posjeduje, dobiva jasnu obavijest putem modal prozora
- Provjere vlasništva u svakom view-u

## 📸 Izgled aplikacije

Aplikacija koristi jednostavan i pregledan dizajn, uz podršku za uređivanje putem modal prozora, upozorenja za pokušaje uređivanja tuđih sadržaja, te intuitivne kontrole za sve osnovne zadatke.

---

© 2025 TaskFlow – Sva prava pridržana.