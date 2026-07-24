from flask import request, json, jsonify, Flask
from flask_mysqldb import MySQL
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

app.config['MYSQL_HOST'] = 'host.docker.internal'  # conexao com hosts internos
app.config['MYSQL_USER'] = '' # colocar user qnd for fzr teste dnv
app.config['MYSQL_PASSWORD'] = '' # senha se tiver
app.config['MYSQL_DB'] = 'flaskhost'

mysql = MySQL(app)

@app.route("/", methods=["GET"])
def index():
    data = requests.get("https://randomuser.me/api")
    return data.json()

@app.route("/inserthost", methods=["POST"])
def insert_host():
    response = requests.get("https://randomuser.me/api")
    data = response.json()
    username = data['results'][0]['name']['first']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(name) VALUES (%s)", (username,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"status": "sucesso", "usuario_inserido": username})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
