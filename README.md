# Controle de Barbearia

Bem-vindo ao repositório do **Controle de Barbearia**! Este sistema tem como objetivo gerenciar o controle de estoque, financeiro e de clientes de uma barbearia, trazendo também relatórios completos atualizados mensalmente via ETL proporcionando uma administração mais eficiente, prática e detalhada do seu comércio.

## Tecnologias Utilizadas

- **Backend**: Python
- **Frontend**: HTML, CSS e JavaScript
- **Banco de Dados**: SQL SERVER
- **API**: Criação de endpoints RESTful (GET, POST, PUT, DELETE) para manipulação de informações

## Funcionalidades do Sistema

- ETL: Subir um arquivo .txt por um sistema ETL.
- Relatórios atualizados: Visualizar relatório completos, qual o melhor barberio, qual os melhores serviços, ganhos mensais...
- Gestão de clientes: Cadastro, edição e exclusão
- Controle de estoque: Gerenciamento de produtos e materiais utilizados
- Controle financeiro: Registro de entradas e saídas
- Interface amigável e responsiva

## Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/BrunoToniatti/barbearia

2. Instale as depedências
   ```bash
   pip install -r requirements.txt

3. Configure a sua conexão para o banco de dados no arquivo *database.py*

## Como utilizar

1. Inicie o servidor Flask
   ```bash
   python app.py

2. Subir os dados pelo ETL
   - Acesse a página etl.html
   - Suba o arquivo clientes_atendidos.txt
   **Normalmente este processo de subir os dados pode levar tempo, são 5.000 linhas**

3. Acessar os relatórios
   - Automáticamente já irá subir os dados para o banco
   - E você pode acessar os relatórios