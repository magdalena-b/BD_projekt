Projekt z przedmiotu Bazy danych.
- Magdalena Badura, Jadwiga Uljasz

Aplikacja dla klientów siłowni.
- Framework: Django, Boostrap4
- Baza danych: Oracle

## Opis projektu
Aplikacja pozwala na autentykację klientów siłowni. Klient może zapisywać się na zajęcia, wyświetlić listę zajęć i przeglądać strony z informacjami na temat zajęć i trenerów.

Dodawanie zajęć możliwe jest po wejściu na [stronę_admina](./users/admin.py) i zalogowaniu się jako superuser.


## Struktura:

[models.py](./gym/models.py) - modele Trainer, Classes, Profile

[urls.py](.urls.py) - nawigacja aplikacji

[gym.views](./gym/views.py) - widoki dotyczące wyświetlania zajęć i trenerów, strona główna

[users.views.py](./users/views.py) - widoki dotyczące rejestracji, logowania, strona z profilem użytkownika

[gym.templates](./gym/templates) - szablony HTML stron dotyczących wyświetlania zajęć i trenerów i strony głównej

[users.templates](./users/templates) - szablony HTML stron dotyczących rejestracji, logowania i strony z profilem użytkownika