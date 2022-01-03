from flask import Flask , render_template
from flask import request, redirect
import mysql.connector
from interact_with_DB import interact_db

'''mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="users"
)

mycursor = mydb.cursor()

sql = "INSERT INTO user (userNum, userName, email) VALUES (%s, %s, %s)"
val = ("user1", "Liron", "amiel@gmail.com")
mycursor.execute(sql, val)
mydb.commit()'''


app = Flask(__name__)

@app.route('/home')
@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/assignment8')
def assignment8():  # put application's code here
    return render_template('assignment8.html',
                           myName ={'fristName' :"liron", 'lastName' :"amiel"},
                            myLovedNumber =6,
                           user= ['user1','user2'])


@app.route('/assignment9')
def assignment9():
    return render_template('assignment9.html')

@app.route('/search')
def search():
    users = {'user1':{"name": "Liron", "email":"amiell@gmail.com"},
              'user2':{"name": "Ronen", "email":"ronen@gmail.com"},
              'user3':{"name":"Gal", "email":"gal@gmail.com"},
                'user4':{"name":"Yossi", "email":"yossi@gmail.com"},
              'user5':{"name": "Mira", "email":"mira@gmail.com"}}
    dic = []
    em=[]
    if 'sName' in request.args:
        name = request.args['sName']
        for user in users.keys() :
            if users[user]['name'] == str(name):
                return render_template('search.html', name=name, email= users[user]['email'])
            if name == '':
                dic.append(users[user]['name'])
                em.append(users[user]['email'])
        if name == '':
            return render_template('search.html', name=dic,email=em)
        return render_template('search.html')

    else:
        return render_template('search.html')

@app.route('/login', methods=['GET','POST'])
def login_func():
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        username = request.form['username']
        return render_template('login.html',username=username)

@app.route('/assigment10', methods=['GET','POST'])
def ass10():
    return render_template('assigment10.html')

@app.route('/users', methods=['GET','POST'])
def users():
    query= 'select * from users;'
    users= interact_db(query=query, query_type='fetch')
    return render_template('users.html', users=users)

@app.route('/insertUser', methods=['POST'])
def insertUser():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    query = "insert into users(name, email, password) values ('%s','%s','%s')" % (name, email, password)
    interact_db(query=query, query_type='commit')
    return redirect('/users')

@app.route('/delet_user', methods = ['POST'])
def delet_user():
    userId = request.form['id']
    query = "delete from users where id='%s';" % userId
    interact_db(query=query, query_type='commit')
    return redirect('/users')

@app.route('/update', methods = ['POST'])
def update():
    newName = request.form['newName']
    name = request.form['name']
    query = "update users set name= '%s' where name='%s';" % (newName, name)
    interact_db(query=query, query_type='commit')
    return redirect('/users')



if __name__ == '__main__':
    app.run(debug=true)
