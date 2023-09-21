from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'  
app.config['MYSQL_USER'] = 'root'       
app.config['MYSQL_PASSWORD'] = ''       
app.config['MYSQL_DB'] = 'mental_thrive'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        idnumber = request.form['idnumber']
        studentname = request.form['studentname']
        birthdate = request.form['birthdate']
        email = request.form['email']

        connect = mysql.connection.cursor()

        connect.execute("INSERT INTO students (idnumber, studentname, birthdate, email) VALUES (%s, %s, %s, %s)",
                    (idnumber, studentname, birthdate, email))

        
        mysql.connection.commit()

        connect.close()

        return redirect(url_for('result', studentname=studentname))

    return render_template('index.html')


@app.route('/result/<studentname>')
def result(studentname):
    return render_template('result.html', studentname=studentname)


"""@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        studentname = request.form['studentname']
        return render_template('result.html', studentname=studentname)
    return render_template('index.html')"""


if __name__ == '__main__':
    app.run(debug=True)
