from flask import Blueprint, jsonify, request
import csv
from database import get_db_connection

etl_bp = Blueprint('etl', __name__)

@etl_bp.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "Arquivo vazio"}), 400
    
    try:
        file_content = file.stream.read().decode("ISO-8859-1")  
        data = list(csv.reader(file_content.splitlines(), delimiter='\t'))

        conn = get_db_connection(database='barbeariaETL')
        cursor = conn.cursor()

        for idx, row in enumerate(data):
            if idx == 0:
                continue
            
            if len(row) < 2:  
                continue  

            cursor.execute("INSERT INTO clientes_atendidos (Data, Cliente, Servico, Valor, Profissional, Horario) VALUES (?, ?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4], row[5]))
        
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Arquivo carregado com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500