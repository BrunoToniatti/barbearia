from flask import Blueprint, jsonify
import pyodbc
from database import get_db_connection

profissionais_bp = Blueprint('profisionais', __name__)  # Criando o blueprint para as rotas de datas


@profissionais_bp.route('/api/profissionais', methods=['GET'])
def get_profisionais():
    conn = get_db_connection(database='barbeariaETL')
    cursor = conn.cursor()
    cursor.execute('SELECT Profissional, COUNT(*) AS quantidade FROM clientes_atendidos GROUP BY Profissional')
    profissionais = cursor.fetchall()

    profissional_list = [{"Profissional": row[0], "Quantidade": row[1]} for row in profissionais]

    cursor.close()
    conn.close()

    return jsonify(profissional_list)