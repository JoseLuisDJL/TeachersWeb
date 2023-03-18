from flask import Flask,request,jsonify,make_response
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'mysecretkey'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'prueba_th'

api_cors_config = {
    "origins":"*",
    "allow_headers_":"*"
}

CORS(app,supports_credentials=True, resources={r"/*":api_cors_config})

mysql = MySQL(app)



@app.route('/' )
def index():
    return 'recieve'

@app.route('/addTeacher', methods=['POST'])
def addTeacher():
    
    a = 'Registro exitoso!'
    
    if request.method == 'POST':
        name = request.json['name']
        rfc = request.json['rfc']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO maestros VALUE (%s,%s,%s)',(0,name,rfc))
        mysql.connection.commit()
        #flash('Maestro agregado satisfactoriamente')
        return make_response(jsonify(a),200)

@app.route('/Teachers', methods=['GET'])
def getTeachers():
    a = 'Registro exitoso!'
    
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM maestros')
        res = cur.fetchall()
        
        return make_response(jsonify(res),200)

@app.route('/Teachers/<id>', methods=['GET'])
def getTeacher(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM `maestros` WHERE maestro_id = %s',(id,))
    res = cur.fetchone()
    print(id)
    return make_response(jsonify(res),200)

@app.route('/Teachers/<int:id>', methods=['DELETE'])
def delteTeacher(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM maestros WHERE maestro_id =  %s',(id,))
    mysql.connection.commit()
    return jsonify({'msg':'Maestro Eliminado'})

@app.route('/Teachers/<int:id>', methods=['PUT'])
def updateTeacher(id):
    a = 'Datos actualizados con exito!'
    if request.method == 'PUT':
        name = request.json['name']
        rfc = request.json['rfc']
    
        cur = mysql.connection.cursor()
        cur.execute('UPDATE maestros SET nombre = %s ,rfc=%s WHERE maestro_id = %s',(name,rfc,id,))
        mysql.connection.commit()
        return make_response(jsonify(a),200)   
        

if __name__ == "__main__":
    app.run(debug=True)