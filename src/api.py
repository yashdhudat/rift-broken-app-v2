from flask import Flask, request, jsonify
from src.validator import validate_email

app = Flask(__name__)

@app.route('/validate', methods=['POST'])
def validate():
data = request.get_json()  # INDENTATION error line 8
    email = data.get('email', '')
    if validate_email(email):
        return jsonify({'valid': True})
    return jsonify({'valid': False})

@app.route('/health')
def health():
        return jsonify({'status': 'ok'})  # INDENTATION error line 16
