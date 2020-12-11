from flask import Flask, render_template, request, session, redirect, url_for, g,Markup
import model
import sqlite3

app= Flask(__name__)
app.secret_key = 'jumpjacks'

# username = ''
user = model.check_users()

@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']

@app.route('/login', methods = ['GET','POST'])
def login():
    try:
        if request.method == 'POST':
            session.pop('username', None)
            areyouuser = request.form['username']
            pwd = model.check_pw(areyouuser)
            if request.form['password'] == pwd:
                session['username'] = request.form['username']
                message = ' Navigate to "HOME" to review your tasks.'
                return render_template('homepage.html',message = 'Welcome back, ' + session['username'] + '!' + message)
    except Exception as error:
            return render_template('login.html', message = 'Error has occurred: ' + str(error) + '. You might have inserted the wrong username or password')
    return render_template('login.html')

@app.route('/', methods=['GET'])
def home():
    if 'username' in session:
        g.user = session['username']
        connection = sqlite3.connect('flask_hw3.db', check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM Task WHERE UserName = ?""",[g.user])
        data = cursor.fetchall()
        return render_template('status.html', tableTask = data)
        connection.commit()
        cursor.close()
        connection.close()
    return render_template('index.html', message = Markup('Welcome to the daily task homepage <br> Login or signup to access or register item task'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        message = 'Please sign up by clicking button "submit" after all the required fields are filled in'
        return render_template('signup.html', message = message)
    else:
        username = request.form["username"]
        password = request.form["password"]
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        if username == '' or password == ' ' or firstname == '' or lastname == '':
            return render_template('signup.html', message = "please make sure no column is left empty")
        message = model.signup(username, password,firstname,lastname)
        return render_template('signup.html', message = message)

@app.route('/dashboard', methods = ['GET','POST'])
def dashboard():
    if request.method == 'GET':
        message = 'Register here your task of today'
        return render_template('dashboard.html', message = message)
    else:
        jobcode = request.form["jobcode"]
        username = session['username']
        task = request.form['task']
        status = request.form['status']
        message = model.submitTask(jobcode, username,task,status)
    return render_template('dashboard.html', message = message)
    # return render_template('dashboard.html')

@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('index.html', message = 'You have succesfully logged out')


@app.route('/adminLogin', methods = ['GET','POST'])
def adminLogin():
    try:
        if request.method == 'POST':
            session.pop('username', None)
            areyouuser = request.form['username']
            pwd = model.check_adminPW(areyouuser)
            if request.form['password'] == pwd:
                session['username'] = request.form['username']
                connection = sqlite3.connect('flask_hw3.db', check_same_thread=False)
                cursor = connection.cursor()
                cursor.execute("""SELECT * FROM Users""")
                results = cursor.fetchall()
                numberOfSignUps = len(results)
                cursor = connection.cursor()
                cursor.execute("""SELECT COUNT (*) FROM Task""")
                results = cursor.fetchone()
                totalList = results[0]
                return render_template('adminLogin_withData.html',numberOfSignUps = numberOfSignUps,totalList=totalList)
                connection.commit()
                cursor.close()
                connection.close()
        return render_template('adminLogin.html')
    except Exception as error:
        return render_template('adminLogin.html', message = 'Error has occurred: ' + str(error))

@app.route('/adminPage', methods = ['GET'])
def adminPage():
    connection = sqlite3.connect('flask_hw3.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM Task """)
    data = cursor.fetchall()
    return render_template('adminPage.html', tableTask = data)
    connection.commit()
    cursor.close()
    connection.close()

#routing About page:
@app.route('/about', methods=['GET'])
def About():
    return render_template('about.html')

#routing Terms of use page:
@app.route('/termsOfUse',methods=['GET'])
def termsOfUse():
    return render_template('termsOfUse.html')

#routing privacy page:
@app.route('/privacy',methods = ['GET'])
def privacy():
    return render_template('privacy.html')

@app.route('/edit', methods = ['GET','POST'])
def editStatus():
    print('testing edit status')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000,debug = True)
    #sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #sock.bind(('localhost',0))
    #port = sock.getsockname()[1]
    #sock.close()
    #app.run(port=port)
