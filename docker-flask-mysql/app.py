from flask import Flask, Response, request, abort
from flask import jsonify
from flaskext.mysql import MySQL
import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
logging.getLogger('pika').setLevel(logging.WARNING)
log = logging.getLogger()

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'techbow'
app.config['MYSQL_DATABASE_HOST'] = 'mysql-host'
mysql.init_app(app)

@app.route("/")
def hello():
    return Response("Hi from your Flask app running in your Docker container!")

@app.route("/user/<int:user_id>", methods=['GET'])
def get_email_by_user_id(user_id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT email from user where id = {user_id}".format(user_id=user_id))
    email = cursor.fetchone()
    conn.close()
    return jsonify({'user_id': user_id, 'email': email})

@app.route('/user', methods=['POST'])
def create_task():
    if not request.json or not 'name' in request.json:
        abort(400)
    conn = mysql.connect()
    cursor = conn.cursor()
    log.info("name: " + request.json['name'] + " email: " + request.json['email'])
    insert_stmt = (
        "INSERT INTO user (name, email) "
        "VALUES (%s, %s)"
    )
    data = (request.json['name'], request.json['email'])
    cursor.execute(insert_stmt, data)
    # By default Connector/Python turns autocommit off
    # The commit() function allows the data to be saved permanently.
    conn.commit()
    cursor.execute("SELECT LAST_INSERT_ID()")
    user_id = cursor.fetchone()
    conn.close()
    return jsonify({'user_id': user_id})

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
