# tkinter-database-manager

# 🧾 System Zarządzania Hurtownią

Aplikacja stworzona w Pythonie z użyciem biblioteki `tkinter` oraz bazy danych MySQL. Pozwala na zarządzanie dostawcami, produktami, klientami, fakturami, zamówieniami do hurtowni oraz sprzedażą.

---

## 📦 Funkcje aplikacji

- Przeglądanie i edycja danych w bazie (dostawcy, klienci, produkty, itd.)
- Dodawanie i usuwanie rekordów z wybranych tabel
- Współpraca z bazą danych MySQL (relacje z kluczami obcymi i `ON DELETE CASCADE`)
- Interfejs graficzny zbudowany w `tkinter`

---

## 🛠️ Technologie

- **Python 3.x**
- **Tkinter** – GUI
- **MySQL** – baza danych
- **mysql-connector-python** – połączenie z bazą

---

---

## 💾 Wymagania

- **Python 3.7** lub nowszy
- **MySQL Server** – zainstalowany i skonfigurowany lokalnie lub na zdalnym serwerze
- Zainstalowane pakiety:
  - `mysql-connector-python`
  - `tkinter`

---

## 🚀 Jak uruchomić


1. Utwórz bazę danych w MySQL (np. hurtownia) i załaduj strukturę z pliku:

2. W pliku main.py wpisz dane odpowiadające twojej bazie danych:

db = sql.connect(
    host="localhost",
    user="twoj_user",
    password="twoje_haslo",
    database="hurtownia"
)

3. Uruchom aplikację

4. Aplikacja powinna teraz działać, umożliwiając Ci zarządzanie danymi hurtowni za pomocą interfejsu graficznego.# SQL-Tkinter-Data-Manager
