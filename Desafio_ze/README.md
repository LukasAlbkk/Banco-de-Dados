# Desafio Zé Delivery - Busca de Parceiros

Este projeto Python permite que o usuário interaja com um banco de dados MySQL, realizando buscas de parceiros com base no ID ou nas coordenadas geográficas do usuário. O sistema retorna informações sobre o parceiro mais próximo que cobre a área fornecida ou os dados de um parceiro específico com base no ID.

## Funcionalidades

- **Buscar parceiro por ID**: Retorna informações detalhadas sobre o parceiro.
- **Buscar parceiro mais próximo**: Dada uma localização (latitude e longitude), retorna o parceiro mais próximo cuja área de cobertura inclua a localização.

## Pré-requisitos

Para executar o projeto, você precisará dos seguintes requisitos instalados em sua máquina:

- Python 3.x
- MySQL
- Pacote `mysql-connector-python`

## Configuração do Ambiente

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/LukasAlbkk/Banco-de-Dados.git
    cd seu-repositorio
    ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

3. **Instale as dependências**:
    ```bash
    pip install mysql-connector-python
    ```

4. **Configure o banco de dados MySQL**:
    - Certifique-se de ter o MySQL instalado e rodando em sua máquina.
    - Configure o banco de dados `ze_delivery` com uma tabela `parceiros` para armazenar os dados.
    - Exemplo de criação de tabela:

    ```sql
    CREATE TABLE parceiros (
        id INT PRIMARY KEY,
        tradingName VARCHAR(255),
        ownerName VARCHAR(255),
        document VARCHAR(50) UNIQUE,
        address POINT,
        coverageArea MULTIPOLYGON
    );
    ```

5. **Carregue os dados no banco**:
    - Insira os dados dos parceiros na tabela `parceiros`. Se tiver um arquivo JSON, você pode carregar os dados diretamente no banco.

## Como Executar

1. **Edite as credenciais de conexão com o MySQL**:
    No arquivo `query_database.py`, edite as informações de conexão com o banco de dados MySQL de acordo com sua configuração:

    ```python
    conn = mysql.connector.connect(
        host="Seu_Host",  # Exemplo: localhost ou MacBook-Air-de-Lucas-3.local
        user="Seu_Usuario",
        password="Sua_Senha",
        database="ze_delivery"
    )
    ```

2. **Execute o script**:
    Com o ambiente configurado, execute o seguinte comando:

    ```bash
    python3 query_database.py
    ```

3. **Interaja com o sistema**:
    O programa oferece duas opções:
    
    - Buscar parceiro por ID.
    - Buscar o parceiro mais próximo com base em coordenadas (longitude e latitude).

    ### Exemplo de Interação:
    
    - Ao executar o programa, você verá o seguinte menu:

      ```plaintext
      -Digite 1 para buscar um determinado ID no banco de dados.
      -Digite 2 para digitar suas coordenadas e assim buscar a loja mais próxima de você.
      -Digite qualquer outro número para sair.
      ```

    - **Buscar por ID**:
      Digite `1` e insira o ID do parceiro que deseja buscar.

    - **Buscar parceiro mais próximo**:
      Digite `2` e insira as coordenadas de longitude e latitude para encontrar o parceiro mais próximo.

## Estrutura do Código

O código consiste em:

1. **Conexão com o Banco de Dados**: O script se conecta ao MySQL utilizando `mysql-connector-python`.
2. **Funções**:
    - `parceiro_existe`: Verifica se o parceiro existe pelo ID.
    - `buscar_parceiro_por_id`: Busca e exibe informações de um parceiro pelo ID.
    - `buscar_parceiro_proximo`: Dada uma localização, encontra o parceiro mais próximo cuja área de cobertura inclui a localização.
3. **Interação do Usuário**: O usuário interage com o sistema via terminal, escolhendo entre as opções de busca.

