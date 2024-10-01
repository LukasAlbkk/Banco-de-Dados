import mysql.connector
import json

# Conectar ao banco de dados
conn = mysql.connector.connect(
    host="MacBook-Air-de-Lucas-3.local",
    user="root",
    password="Santos2001",
    database="ze_delivery"
)
cursor = conn.cursor()

# Abrir e carregar o arquivo JSON
with open('pdvs.json', 'r') as f:
    data = json.load(f)

# Acessar a chave 'pdvs'
pdvs = data['pdvs']

# Preparar o comando SQL para inserir os dados
sql_insert = """
    INSERT INTO parceiros (id, tradingName, ownerName, document, address, coverageArea)
    VALUES (%s, %s, %s, %s, ST_GeomFromText(%s), ST_GeomFromText(%s))
"""

# Iterar sobre os dados dentro da chave 'pdvs' e inserir no banco de dados
for item in pdvs:
    id = item["id"]
    tradingName = item["tradingName"]
    ownerName = item["ownerName"]
    document = item["document"]

    # Convertendo a coordenada do endereço para WKT (Well-Known Text)
    address_coordinates = item["address"]["coordinates"]
    address_wkt = f'POINT({address_coordinates[0]} {address_coordinates[1]})'

    # Convertendo a área de cobertura (coverageArea) para WKT
    multipolygon_coordinates = item["coverageArea"]["coordinates"]
    multipolygon_wkt = 'MULTIPOLYGON(' + ', '.join(
        ['((' + ', '.join([f'{coord[0]} {coord[1]}' for coord in polygon[0]]) + '))' for polygon in multipolygon_coordinates]
    ) + ')'

    # Inserir os dados no banco de dados
    cursor.execute(sql_insert, (id, tradingName, ownerName, document, address_wkt, multipolygon_wkt))

# Confirmar (commit) as inserções no banco de dados
conn.commit()

# Fechar a conexão
cursor.close()
conn.close()

print("Dados inseridos com sucesso.")
