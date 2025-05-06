from flask import Flask, render_template, request, jsonify
from des import DES
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.get_json()
        key = data.get('key')
        plaintext = data.get('plaintext')
        
        if not key or not plaintext:
            return jsonify({'error': 'Chave e texto plano são obrigatórios'}), 400
            
        
        des = DES(key)
        ciphertext = des.encrypt(plaintext.encode('utf-8'))
        

        ciphertext_b64 = base64.b64encode(ciphertext).decode('utf-8')
        
        return jsonify({
            'ciphertext': ciphertext_b64,
            'message': 'Criptografia realizada com sucesso'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        data = request.get_json()
        key = data.get('key')
        ciphertext = data.get('ciphertext')
        
        if not key or not ciphertext:
            return jsonify({'error': 'Chave e texto cifrado são obrigatórios'}), 400
            
        ciphertext_bytes = base64.b64decode(ciphertext)
        
        des = DES(key)
        plaintext = des.decrypt(ciphertext_bytes)
        
        return jsonify({
            'plaintext': plaintext.decode('utf-8'),
            'message': 'Descriptografia realizada com sucesso'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 