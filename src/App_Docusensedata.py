from flask import Flask, json, request, jsonify
from flask_mysqldb import MySQL,MySQLdb 

app = Flask(__name__)
  
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'kailash@028'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'docusense'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/database')
def database():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM Docusense_document_Database''')
    results = cur.fetchall()
    output = {'status':200, 'results':list(results) }
    print(results)
    return output

@app.route('/docutype')
def docutype():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM Docusense_document_type''')
    results = cur.fetchall()
    output = {'status':200, 'results':list(results) }
    return output

if __name__ == '__main__':
    app.run(debug=True, port = 5098)