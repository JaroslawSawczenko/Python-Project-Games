import sys

try:
    from core import menu
except ImportError as e:
    print(f"Błąd importu: {e}")
    print("Upewnij się, że wszystkie pliki są w odpowiednich katalogach.")
    sys.exit(1)


if __name__ == "__main__":   
    menu.run() # /core/menu.py










