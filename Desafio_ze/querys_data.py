import mysql.connector

conn = mysql.connector.connect(
    host="local_host",
    user="root",
    password="sua_senha",
    database="ze_delivery"
)
cursor = conn.cursor()

#verificar se o parceiro já existe
def parceiro_existe(parceiro_id):
    cursor.execute("SELECT COUNT(*) FROM parceiros WHERE id = %s", (parceiro_id,))
    count = cursor.fetchone()[0]
    return count > 0

# Função para buscar parceiro por ID
def buscar_parceiro_por_id(parceiro_id):
    sql = """
    SELECT id, tradingName, ownerName, document, ST_AsText(address) AS address, ST_AsText(coverageArea) AS coverageArea
    FROM parceiros
    WHERE id = %s
    """
    cursor.execute(sql, (parceiro_id,))
    parceiro = cursor.fetchone()  
    if parceiro:
        print("ID:", parceiro[0])
        print("Nome Comercial:", parceiro[1])
        print("Nome do Dono:", parceiro[2])
        print("Documento:", parceiro[3])
        print("Endereço (WKT):", parceiro[4])
        print("Área de Cobertura (WKT):", parceiro[5])
    else:
        print(f"Nenhum parceiro encontrado com o ID {parceiro_id}")



## Buscando pareceiro mais proximo:
def buscar_parceiro_proximo(longitude, latitude):
    sql = """
    SELECT id, tradingName, ownerName, document, ST_AsText(address), ST_AsText(coverageArea),
        ST_Distance(ST_GeomFromText('POINT(%s %s)'), address) AS distance
    FROM parceiros
    WHERE ST_Contains(coverageArea, ST_GeomFromText('POINT(%s %s)'))
    ORDER BY distance ASC
    LIMIT 1;
    """
    cursor.execute(sql, (longitude, latitude, longitude, latitude))
    parceiro = cursor.fetchone() 
    if parceiro:
        print("ID:", parceiro[0])
        print("Nome Comercial:", parceiro[1])
        print("Nome do Dono:", parceiro[2])
        print("Documento:", parceiro[3])
        print("Endereço (WKT):", parceiro[4])
        print("Área de Cobertura (WKT):", parceiro[5])
        print("Distância:", round(parceiro[6], 6)) 
    else:
        print(f"Nenhum parceiro encontrado para a localização ({longitude}, {latitude})")


#interface de usuário:
i = 1
while(i == 1):
    print("-Digite 1 para buscar um determinado ID no banco de dados.\n-Digite 2 para digitar suas coordenadas e assim buscar a loja mais próxima de você.\n-Digite qualquer outro número para sair.")
    char = int(input())
    if (char == 1):
        parceiro_id = input("Digite o ID do parceiro: ")
        buscar_parceiro_por_id(parceiro_id)
        print("-------------------------------------------------------")
    elif (char == 2):
        longitude = float(input("Digite a longitude: "))
        latitude = float(input("Digite a latitude: "))
        buscar_parceiro_proximo(longitude, latitude)
        print("-------------------------------------------------------")
    else:
        i = 0


conn.commit()
cursor.close()
conn.close()
