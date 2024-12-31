A not so simple SQL/python project.
Database includes three tables: chess players, tournaments and partitipations(names are pretty self-explanatory).
Framework: FastAPI
Library: SQLalchemy

Everything needed is in requirements.txt

Usage:
Run the postgre server: sudo systemctl start postgresql
check if running: pg_isready

run the webserver: python3 main.py(in app directory)
link: http://127.0.0.1:8080/

enter server manually: psql -h localhost -U postgres
