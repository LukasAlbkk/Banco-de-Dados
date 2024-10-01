import mysql.connector
import json

conn = mysql.connector.connect(
    host="local_host",
    user="root",
    password="sua_senha",
    database="ze_delivery"
)
cursor = conn.cursor()

# carregar o arquivo JSON
with open('pdvs.json', 'r') as f:
    data = json.load(f)
pdvs = data['pdvs']

sql_insert = """
    INSERT INTO parceiros (id, tradingName, ownerName, document, address, coverageArea)
    VALUES (%s, %s, %s, %s, ST_GeomFromText(%s), ST_GeomFromText(%s))
"""

for item in pdvs:
    id = item["id"]
    tradingName = item["tradingName"]
    ownerName = item["ownerName"]
    document = item["document"]
    address_coordinates = item["address"]["coordinates"]
    address_wkt = f'POINT({address_coordinates[0]} {address_coordinates[1]})'

    multipolygon_coordinates = item["coverageArea"]["coordinates"]
    multipolygon_wkt = 'MULTIPOLYGON(' + ', '.join(
        ['((' + ', '.join([f'{coord[0]} {coord[1]}' for coord in polygon[0]]) + '))' for polygon in multipolygon_coordinates]
    ) + ')'

    cursor.execute(sql_insert, (id, tradingName, ownerName, document, address_wkt, multipolygon_wkt))

conn.commit()
cursor.close()
conn.close()

print("Dados inseridos com sucesso.")
