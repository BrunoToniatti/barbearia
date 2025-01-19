from flask import Blueprint, jsonify
import pyodbc
from database import get_db_connection

datas_bp = Blueprint('datas', __name__)  # Criando o blueprint para as rotas de datas


@datas_bp.route('/api/datas', methods=['GET'])
def get_datas():
    conn = get_db_connection(database='barbeariaETL')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT MONTH(Data) AS Mes, 
               SUM(CAST(REPLACE(Valor, ',', '.') AS FLOAT)) AS valor
        FROM clientes_atendidos  
        WHERE YEAR(Data) = 2024
        GROUP BY MONTH(Data)
    """)
    datas = cursor.fetchall()

    meses = {
        '1': 'Janeiro', '2': 'Fevereiro', '3': 'Março', '4': 'Abril',
        '5': 'Maio', '6': 'Junho', '7': 'Julho', '8': 'Agosto',
        '9': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'
    }

    datas_list = [{"Data": meses[str(row[0])], "Valor": row[1]} for row in datas]

    cursor.close()
    conn.close()

    return jsonify(datas_list)
