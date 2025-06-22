import sys
import os

# Dodaj katalog główny do ścieżki, aby Python mógł znaleźć moduły
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from core import menu
except ImportError as e:
    print(f"Błąd importu: {e}")
    print("Upewnij się, że wszystkie pliki są w odpowiednich katalogach.")
    sys.exit(1)


if __name__ == "__main__":
       # Sprawdź wersję Pythona
    if sys.version_info < (3, 6):
        print("Błąd: Wymagany Python 3.6 lub nowszy")
        print(f"Twoja wersja: {sys.version}")
        sys.exit(1)
   
   
   
    menu.run() # /core/menu.py










