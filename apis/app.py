from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from service import get_prediction_from_url
import urllib.parse

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Route gốc (homepage)
@app.route('/')
def home():
    return "ping!"

@app.route('/domains/<path:domain_name>', methods=['GET'])
@cross_origin()
def get_user(domain_name):
   try:
        encoded_domain = urllib.parse.quote(domain_name)
        return jsonify(get_prediction_from_url(encoded_domain))
   except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)