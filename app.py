from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def assignment8():  # put application's code here
    return render_template('assignment8.html',
                           myName ={'fristName' :"liron", 'lastName' :"amiel"},
                            myLovedNumber =6,
                           user= ['user1','user2'])

if __name__ == '__main__':
    app.run()
