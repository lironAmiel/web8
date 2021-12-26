from flask import Flask , render_template
from flask import request


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


if __name__ == '__main__':
    app.run()
