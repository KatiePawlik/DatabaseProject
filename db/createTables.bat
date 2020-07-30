del /Q "..\PawlikLabs.db"
sqlite3 ../PawlikLabs.db ""
sqlite3 ../PawlikLabs.db ".read createTables.sql"
pause