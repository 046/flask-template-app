# run.py
from flask import Flask, jsonify
 
app = Flask(__name__)
 
 
@app.route('/')
def api_sample():
    """
    API Sample
    """
    result = {"code": "001", "name": "apple"}
    return jsonify(ResultSet=result)
 
 
if __name__ == '__main__':
    app.run()
