from flask import Flask, jsonify, request
from flask_cors import CORS
from routes.datas import datas_bp
from routes.profissioniais import profissionais_bp
from routes.servicos import servicos_bp
from routes.etl import etl_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(etl_bp)

app.register_blueprint(servicos_bp)

app.register_blueprint(profissionais_bp)

app.register_blueprint(datas_bp)


if __name__ == '__main__':
    app.run(debug=True)
