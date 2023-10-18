#importar o driver
import cx_Oracle
#importa oracledb

#create table
def create_table(name):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql_query = """ CREATE TABLE CEO_DETAILS(
        FIRST_NAME VARCHAR2(50)
        LAST_NAME VARCHAR2(50)
        COMPANY VARCHAR2(50)
        AGE NUMBER
        )"""
        cursor.execute(sql_query)
        print("Table created sucessfully")
    
    except Exception as e:
        print("Error occurred while creating the table", e)

    finally:
        if (conn):
            cursor.close()
            conn.close()
        

#criar uma conexão com o BD Oracle 
def getConnection():
    try:
        connection = cx_Oracle.connect('rm123', '123456', 'oracle.fiap.com.br/orcl')
        #connection = cx_Oracle.connect(user = 'rm123', password = '123456', host = 'oracle.fiap.com.br', port = '1521', service = 'orcl')
        print('Conexão: ', connection.version)

    except Exception as e:
        print(f'Erro ao obter a conexão: {e}')
        return connection
    
def insert():
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "ISERT INTO CEO_DETAILS values('Steve', 'Jobs','Apple', '50')"

    try:
        cursor.execute(sql_query)
        conn.commit()
        print("Registro inserido")
    
    except Exception as e:
        print('Erro ao inserir o registro')

    finally:
        cursor.close()
        conn.close()

def insertParametros(first_name, last_name, company, age):
    conn = getConnection()
    cursor = conn.cursor()
    sql_query = "INSERT INTO CEO_DETAILS (first_name, last_name, company, age) VALUES({first_name}, {last_name}, {company}, {age})"

    '''
    data = (
    input("Name: ")
    input("Last Name: ")
    input("Company: ")
    int(input("Age: "))
    )
    '''
    
    data = (
        first_name,
        last_name,
        company,
        age
    )
    try:
        cursor.execute(sql_query, data)
        conn.commit()
        print("Registro inserido")

    finally:
        cursor.close()
        conn.close()

def select():
    conn = getConnection()
    cursor = conn.cursosr()
    sql_query = "SELECT * FROM CEO_DETAIL WHERE NAME = 'Steve'"
    #sql_query = "SELECT * from CEO_DETAILS"
    try:
        cursor.execute(sql_query)
        for result in cursor:
            print(result)
    except Exception as e:
        print(f'Erro ao obter o registro {e}')
    finally:
        cursor.close()
        conn.close()

def update():
    conn = getConnection()
    cursor = conn.cursor()
    sql_update = "UPDATE CEO_DETAIL SET COMPANY='Microsoft' where name = 'Steve'"

    #outro exemplo 
    sql_query = "UPADTE CEO_DATAILS set AGE WHERE FIRST_NAME = 'Steve'"

    try:
        cursor.execute(sql_update)
        conn.commit()
        print("Dados atualizados com sucesso!")
    
    except Exception as e:
        print(f'Erro na atualização do registro {e}')
    finally:
        cursor.close()
        conn.close()

def delete():
    conn = getConnection()
    cursor = conn.cursor()
    sql_delete = "DELETE FROM CEO_DETAILS WHERE FIRST_NAME = 'Steve'"
    
    try:
        cursor.execute(sql_delete)
        conn.commit()
        print("Registro deletado com sucesso!")
    
    except Exception as e:
        print(f'Erro no deleto do registro {e}')

    finally:
        cursor.close()
        conn.close()
    
#principal
select()
insert()
select()
update()
select()
delete()
select()