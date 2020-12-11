import sqlite3

connection  = sqlite3.connect('flask_hw3.db',check_same_thread = False)
cursor = connection.cursor()

def check_pw(username):
    connection = sqlite3.connect('flask_hw3.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT Password FROM Users WHERE UserName = '{username}'ORDER BY UserName DESC;""".format(username = username))
    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    return password
    
def check_adminPW(username):
    connection = sqlite3.connect('flask_hw3.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT Password FROM Admin WHERE UserName = '{username}'ORDER BY UserName DESC;""".format(username = username))
    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    return password

def check_users():
    connection = sqlite3.connect('flask_hw3.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT UserName FROM Users ORDER BY UserName DESC;""")
    db_users = cursor.fetchall()
    users = []

    for i in range(len(db_users)):
        person = db_users[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()

    return users

def signup(username, password, firstname, lastname):
    connection = sqlite3.connect('flask_hw3.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT Password FROM Users WHERE UserName = '{username}';""".format(username = username))
    exists = cursor.fetchone()

    if exists is None:
        cursor.execute("""INSERT INTO Users(UserName,Password,FirstName,LastName)VALUES('{username}','{password}','{firstname}','{lastname}');""".format(username=username,password=password,firstname=firstname,lastname=lastname))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        return('User already existed!!! ')

    return 'You have succesfully signed up! '

def submitTask(jobcode,username,task,status):
    connection = sqlite3.connect('flask_hw3.db',check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(""" INSERT INTO Task(JobCode,UserName,Task,Status)VALUES('{jobcode}','{username}','{task}','{status}');""".format(jobcode=jobcode,username=username,task=task,status=status))
    connection.commit()
    cursor.close()
    connection.close()

    return 'Thank you for submitting or updating your task. navigate to "Home" to view the your list of task'
