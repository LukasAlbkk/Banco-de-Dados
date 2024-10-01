import mysql.connector

conn = mysql.connector.connect(
    host="local_host",  
    user="root",                          
    password="sua_senha",               
    database="ze_delivery"                
)
cursor = conn.cursor()

# Criar a tabela parceiros
create_table_query = """
CREATE TABLE IF NOT EXISTS parceiros (
    id INT PRIMARY KEY,
    tradingName VARCHAR(255),
    ownerName VARCHAR(255),
    document VARCHAR(50) UNIQUE,
    address POINT,
    coverageArea MULTIPOLYGON
);
"""

cursor.execute(create_table_query)
print("Tabela 'parceiros' criada ou já existe.")
conn.commit()

cursor.close()
conn.close()
print("Conexão com o banco de dados fechada.")
