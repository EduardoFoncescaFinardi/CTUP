"""

1. Oracle DB
2. Python lib(Bibliotecas Python)
3.DB detalis

PEP 249 - Python Database API Specification v2,0

Módulos:
cx_Oracle | oracledb - OracleDatabase
pyodbc - Microsft SQL Server
pymysql - MySQL
psycopg2 - PostGreSQL

Passos:
1. Estabelecer uma conexão entre Python com o BD
    Connection = cx_Oracle.connect(database connection string)

2. Obter um Cursor (objeto para exectuar queries e obter resultados após a execução)

cursor = connection.cursor()
"""

import cx_Oracle

#create connection
conn = cx_Oracle.connect(user = "rm123", password = "291002",
                         host = "oracle.fiap.com.br",
                         port = "1521",
                         service_name = "ORCL")

print(conn.version)

#create cursor
cursor = conn.cursor()

#create Table
sql_create = """
CREATE TABLE CEO_DETAILS
    FIRST_NAME VARCHAR2(50),
    LAST_NAME VARCHAR2(50),
    LAST_NAME VARCHAR2(50),
    COMPANY VARCHAR2(50),
    AGE NUMBER
"""

#execute query
cursor.execute(sql_create)
print('Tabela criada!')