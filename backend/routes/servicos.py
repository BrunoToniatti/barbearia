from database import get_db_connection
from flask import Blueprint, jsonify

servicos_bp = Blueprint('servicos', __name__)

@servicos_bp.route('/api/servicos', methods=['GET'])
def get_services():
    conn = get_db_connection(database='barbeariaETL')
    cursor = conn.cursor()
    cursor.execute('SELECT Servico, COUNT(*) AS quantidade FROM clientes_atendidos GROUP BY Servico ORDER BY quantidade DESC')
    servicos = cursor.fetchall()  

    service_list = [{"Servico": row[0], "Quantidade": row[1]} for row in servicos]

    cursor.close()
    conn.close()

    return jsonify(service_list)