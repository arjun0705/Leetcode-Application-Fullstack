
import sqlite3
from time import process_time
from django import db

# con = sqlite3.connect('db.sqlite3')

# cr = con.cursor()

# cr.execute(""" CREATE TABLE users(
#     first_name VARCHAR(25),
#     last_name  VARCHAR(25),
#     email TEXT UNIQUE NOT NULL,
#     password VARCHAR(20) NOT NULL,
#     is_admin BOOLEAN DEFAULT 1
# )""")

# con.commit()
# con.close()

# con = sqlite3.connect('db.sqlite3')

# cr = con.cursor()

# cr.execute(""" CREATE TABLE problems(
#     Title VARCHAR(500),
#     Description TEXT,
#     Difficulty VARCHAR(30),
#     Solution TEXT,
#     usrid VARCHAR NOT NULL
      
# )""")
# con.commit()
# con.close()





def addUser(data):
    conn = sqlite3.connect('db.sqlite3')
    cr = conn.cursor()
    try:
        cr.execute(f""" INSERT INTO users VALUES {data}""")
    finally:
        conn.commit()
        conn.close()

def checkUser(data):
    conn = sqlite3.connect("db.sqlite3")  
    cr = conn.cursor()
    user = None
    try:
        cr.execute(f"SELECT * FROM users WHERE email LIKE '{data}' ")  
        user = cr.fetchone()  
    finally:
        conn.commit()
        conn.close()
        return user    
    
def addProblem(data):
    conn = sqlite3.connect('db.sqlite3')
    cr = conn.cursor()

    cr.execute(f"INSERT INTO problems VALUES {data} ")
    conn.commit()
    conn.close()

def getProblem(id):
    conn = sqlite3.connect('db.sqlite3')
    cr = conn.cursor()
    cr.execute(f"SELECT * FROM problems WHERE rowid LIKE {id} ")
    problem = cr.fetchone()
    conn.commit()
    conn.commit()
    return problem

def getProblems():
    conn = sqlite3.connect('db.sqlite3')
    cr = conn.cursor()
    cr.execute(f"SELECT * FROM problems")
    problems = cr.fetchall()
    conn.commit()
    conn.commit()
    return problems    

def updateProblem(data,id):
    conn = sqlite3.connect('db.sqlite3')
    cr = conn.cursor()
    cr.execute(f"UPDATE problems SET Title = '{data['title']}',Description = '{data['description']}',Difficulty = '{data['difficulty']}',Solution = '{data['solution']}' WHERE rowid LIKE {id} ")
    # problem = cr.fetchone()
    conn.commit()
    conn.commit()
    # return problem    

def deleteProblem(id):
    conn = sqlite3.connect('db.sqlite3')
    cr = conn.cursor()
    cr.execute(f"DELETE FROM problems WHERE rowid LIKE {id} ")
    conn.commit()
    conn.commit()
    

