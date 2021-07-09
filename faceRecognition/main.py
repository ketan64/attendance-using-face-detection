from flask import Flask, render_template,request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb


app = Flask(__name__)
app.secret_key = "12345678"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"

app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "login"
# app.config["MYSQL_"]

db = MySQL(app)

@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("select * from logininfo where email=%s and password=%s ",(username,password))
            info = cursor.fetchone()
            if info['email'] == username and info['password'] == password:
                return "login successful"
            else:
                return "login unsuccessfull, please register"


    return  render_template("register.html")


# @app.route('/register.html')
# def new_user():
#     return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)

