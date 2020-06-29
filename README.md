Projekt z przedmiotu Bazy danych.
- Magdalena Badura, Jadwiga Uljasz

Aplikacja dla klientów siłowni.
- Framework: Django, Boostrap4
- Baza danych: Oracle

## Opis projektu
Aplikacja pozwala na autentykację klientów siłowni. Klient może zapisywać się na zajęcia, wyświetlić listę zajęć i przeglądać strony z informacjami na temat zajęć i trenerów.

Dodawanie zajęć możliwe jest po wejściu na podstronę /admin i zalogowaniu się jako superuser.


## Struktura:

[models.py](./gym/models.py) - modele Trainer, Classes, Profile

[urls.py](.urls.py) - nawigacja aplikacji

[gym.views](./gym/views.py) - widoki dotyczące wyświetlania zajęć i trenerów, strona główna

[users.views.py](./users/views.py) - widoki dotyczące rejestracji, logowania, strona z profilem użytkownika

[gym.templates](./gym/templates) - szablony HTML stron dotyczących wyświetlania zajęć i trenerów i strony głównej

[users.templates](./users/templates) - szablony HTML stron dotyczących rejestracji, logowania i strony z profilem użytkownika


## Instrukcja do łączenia się z Oraclem przez Dockera

Należy stworzyć konto w Docker Hub:
https://hub.docker.com/ i uzyskać dostęp [Docker Image](https://hub.docker.com/_/oracle-database-enterprise-edition)



```docker login
docker run -d -it --name lol store/oracle/database-enterprise:12.2.0.1
sudo alien -i oracle-instantclient*-basic*.rpm
docker exec -it lol bash -c "source /home/oracle/.bashrc; sqlplus /nolog"
sqlplus sys/Oradoc_db1@localhost/ORCLCDB.localdomain as sysdba```


W konsoli sqlplusa:

```SQL> ALTER SESSION SET CONTAINER=ORCLPDB1;
SQL> ALTER SESSION SET "_ORACLE_SCRIPT"=true;
SQL> CREATE USER django IDENTIFIED BY django;
SQL> GRANT DBA TO django;
SQL> QUIT```


## Łączenie się z bazą przez DataGripa
