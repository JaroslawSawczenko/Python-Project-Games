# 🎮 Terminal Games

Kolekcja gier konsolowych napisanych w Pythonie z systemem użytkowników i rankingiem.

## 📋 Spis treści

- Opis
- Funkcje
- Struktura projektu
- Instalacja
- Uruchomienie
- Dostępne gry
- System punktacji
- Dokumentacja API
- Rozwój
- Licencja

## 🎯 Opis

Terminal Games to zbiór klasycznych gier dostępnych w terminalu/konsoli. Projekt zawiera system użytkowników, który zapisuje wyniki i pozwala śledzić postępy. Każda gra ma swój unikalny system punktacji.

## ✨ Funkcje

- 🎮 **4 różne gry** (Tic-Tac-Toe, 2048, Wordle, Zgadnij liczbę)
- 👤 **System użytkowników** z automatycznym zapisem
- 🏆 **Tracking najlepszych wyników**
- 📊 **Statystyki osobiste i globalne**
- 🎨 **Czytelny interfejs tekstowy**
- 💾 **Automatyczny zapis postępów**
- 🔧 **Modułowa architektura** (łatwe dodawanie nowych gier)

## 📁 Struktura projektu

```
Python-Project-Games/
├── 📄 main.py                    # Punkt wejścia aplikacji
├── 📄 README.md                  # Dokumentacja (ten plik)
├── 📄 LICENSE                    # Licencja MIT
├── 📄 requirements.txt           # Zależności Python
├── 📄 .gitignore                 # Pliki ignorowane przez Git
│
├── 📁 core/                      # Główna logika aplikacji
│   ├── 📄 __init__.py
│   ├── 📄 menu.py                # System menu i nawigacja
│   ├── 📄 user.py                # Zarządzanie użytkownikami
│   └── 📁 data/
│       └── 📄 user_data.json     # Baza danych użytkowników
│
├── 📁 games/                     # Katalog z grami
│   ├── 📄 __init__.py
│   ├── 📄 tic_tac_toe.py         # Kółko i krzyżyk
│   ├── 📄 game_2048.py           # Gra 2048
│   ├── 📄 wordle.py              # Wordle (zgadywanie słów)
│   ├── 📄 Guess_the_Number.py    # Zgadnij liczbę
│   └── 📄 [future_games].py      # Miejsce na nowe gry
│
├── 📁 data/                      # Dane aplikacji
│   ├── 📄 __init__.py
│   └── 📄 user_data.json         # Backup danych użytkowników
│
└── 📁 .venv/                     # Środowisko wirtualne Python
    └── ...
```

## 🚀 Instalacja

### Wymagania systemowe
- Python 3.7+
- System operacyjny: Windows, macOS, Linux

### Krok po kroku

1. **Sklonuj repozytorium:**
   ```bash
   git clone https://github.com/twoj-username/Python-Project-Games.git
   cd Python-Project-Games
   ```

2. **Utwórz środowisko wirtualne:**
   ```bash
   python -m venv .venv
   ```

3. **Aktywuj środowisko wirtualne:**
   
   **Windows (PowerShell):**
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   .venv\Scripts\Activate.ps1
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   .venv\Scripts\activate.bat
   ```
   
   **macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```

4. **Zainstaluj zależności (jeśli są):**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Uruchomienie

### Podstawowe uruchomienie:
```bash
python main.py
```

### Z środowiskiem wirtualnym:
```bash
# Windows
.venv\Scripts\python.exe main.py

# macOS/Linux
.venv/bin/python main.py
```

### Rozwiązywanie problemów:
- ❌ **Jeśli PowerShell blokuje skrypty:** uruchom `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- ❌ **ImportError:** Zawsze uruchamiaj przez `main.py`, nie przez pliki w podkatalogach
- ❌ **FileNotFoundError:** Upewnij się, że jesteś w głównym katalogu projektu

## 🎲 Dostępne gry

### 1. 🎯 Tic-Tac-Toe (Kółko i krzyżyk)
- **Opis:** Klasyczna gra dla dwóch graczy
- **Sterowanie:** Numery 1-9 wybierają pola
- **Punkty:** 100-180 pkt (zależnie od liczby ruchów)

### 2. 🔢 2048
- **Opis:** Łącz kafelki, aby osiągnąć 2048
- **Sterowanie:** W/A/S/D (góra/lewo/dół/prawo)
- **Punkty:** Wynik bazuje na wartościach połączonych kafelków
- **Dodatkowe:** R - restart, Q - wyjście

### 3. 🔤 Wordle
- **Opis:** Zgadnij ukryte słowo polskie
- **Mechanika:** Wskazówki o literach na właściwych miejscach
- **Punkty:** 1-10 pkt (zależnie od liczby prób)
- **Długość słów:** 5-10 liter

### 4. 🎯 Zgadnij liczbę
- **Opis:** Zgadnij liczbę wybraną przez komputer
- **Poziomy trudności:**
  - Łatwy: 1-50 (10 prób) - 100 pkt bazowych
  - Średni: 1-100 (8 prób) - 200 pkt bazowych  
  - Trudny: 1-200 (6 prób) - 300 pkt bazowych
- **Punkty:** Bonus za efektywność (mniej prób = więcej punktów)

## 🏆 System punktacji

### Zasady ogólne:
- ✅ **Zapisywane są tylko najlepsze wyniki** dla każdej gry
- 📈 **Punkty zależą od wydajności** (szybkość, liczba ruchów)
- 🎮 **Każda gra ma własny system punktacji**

### Przechowywanie danych:
- 📁 Dane w `core/data/user_data.json`
- 👤 Automatyczne tworzenie/ładowanie profili użytkowników
- 🔒 Bezpieczna serializacja JSON z obsługą polskich znaków

## 🛠️ Dokumentacja API

### Struktura User (core/user.py)

```python
class User:
    def __init__(self):
        self.user_info = {
            "id": int,           # Unikalny identyfikator
            "name": str,         # Imię użytkownika  
            "results": dict      # Wyniki gier {gra: najlepszy_wynik}
        }
    
    def create_user(self, name: str) -> User
    def add_results(self, game_name: str, score: int) -> None
```

### Dodawanie nowej gry

1. **Utwórz plik gry w `/games/`:**
   ```python
   # games/moja_gra.py
   def moja_gra():
       # Logika gry
       return wynik  # int lub None
   ```

2. **Dodaj import w `core/menu.py`:**
   ```python
   try:
       from games import moja_gra
       MOJA_GRA_AVAILABLE = True
   except ImportError:
       MOJA_GRA_AVAILABLE = False
   ```

3. **Dodaj opcję w menu i obsługę wywołania**

### Funkcje pomocnicze:

```python
# core/menu.py
def clear_screen()                    # Czyści terminal
def check_menu_choice(input, max)     # Walidacja wyboru menu
def display_main_menu()               # Wyświetla główne menu
def display_user_stats(user)          # Statystyki użytkownika
```

## 🔧 Rozwój

### Planowane funkcje:
- 🎮 **Więcej gier** (Snake, Tetris, Sudoku)
- 🏆 **Globalny ranking** użytkowników
- 💾 **Export/import** danych
- 🎨 **Kolorowy interfejs** (biblioteka colorama)
- ⏱️ **Pomiar czasu** gier
- 📊 **Rozszerzone statystyki** (średnie, trendy)

### Jak kontrybuować:
1. Fork projektu
2. Utwórz branch na feature (`git checkout -b feature/AmazingFeature`)
3. Commit zmian (`git commit -m 'Add some AmazingFeature'`)
4. Push do brancha (`git push origin feature/AmazingFeature`)
5. Otwórz Pull Request

### Standardy kodowania:
- 🐍 **PEP 8** compliance
- 📝 **Docstringi** dla wszystkich funkcji
- 🧪 **Obsługa błędów** try/except
- 🔧 **Modułowość** - każda gra w osobnym pliku

## 🐛 Rozwiązywanie problemów

### Częste błędy:

**ImportError: attempted relative import**
```bash
# ❌ Źle:
python core/menu.py

# ✅ Dobrze:
python main.py
```

**PowerShell ExecutionPolicy**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**FileNotFoundError przy zapisie danych**
- Sprawdź uprawnienia do zapisu w katalogu projektu
- Upewnij się, że `core/data/` istnieje

### Debug mode:
Odkomentuj linie z `# print(...)` w plikach gier, aby zobaczyć dodatkowe informacje debugowania.

## 📞 Kontakt i wsparcie

- 🐛 **Zgłaszanie błędów:** [GitHub Issues](link-do-issues)
- 💡 **Sugestie:** [GitHub Discussions](link-do-discussions)
- 📧 **Email:** twoj-email@example.com

## 📜 Licencja

Ten projekt jest licencjonowany na licencji MIT - zobacz plik [LICENSE](LICENSE) po szczegóły.

```
MIT License - możesz swobodnie używać, modyfikować i dystrybuować
```


**Miłej zabawy z Terminal Games! 🎮**

---

*Ostatnia aktualizacja: Sierpień 2025*




















