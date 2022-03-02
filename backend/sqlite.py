import sqlite3
from django import db



con = sqlite3.connect("Leetcode.db")
c = con.cursor()

# c.execute(" CREATE TABLE admins (fullname VARCHAR NOT NULL, address VARCHAR NOT NULL, username VARCHAR NOT NULL UNIQUE, password VARCHAR NOT NULL ) ")


# c.execute(""" CREATE TABLE problems (title VARCHAR(120), 
#                decription VARCHAR,
#                solutions VARCHAR,
#                difficulty VARCHAR,
#                userid VARCHAR NOT NULL,
#                acceptence VARCHAR,
#                FOREIGN KEY(userid) REFERENCES createadmin(id) 
#                 )""")
# con.commit()
# con.close()                


def signup(data):
    con = sqlite3.connect("Leetcode.db")

    c = con.cursor()
    data = (data[0],data[1],data[2],data[3])
    c.execute(f"INSERT INTO admins VALUES {data}")
    con.commit()
    con.close()
    db.connections.close_all()
    return c
    

# def getuser():
#     con = sqlite3.connect("Leetcode.db",timeout=10)
#     c = con.cursor()
#     c.execute(f"SELECT * FROM admins")
#     data = c.fetchall()
#     z = []
#     for d in data:
#         z.append((d[0],d[1],d[2],d[3]))
#     con.commit()
#     con.close()
#     db.connections.close_all()

#     return z


def createproblem(data):
    con = sqlite3.connect("Leetcode.db",timeout=10)

    c = con.cursor()
    data = (data[0],data[1],data[2],data[3],data[4],data[5])
    c.execute(f"INSERT INTO problems VALUES {data}")
    con.commit()
    con.close()
    db.connections.close_all()

# def getproblem():
#     con = sqlite3.connect("Leetcode.db",timeout=10)
#     c = con.cursor()
#     c.execute(f"SELECT * FROM problems")
#     data = c.fetchall()
#     z = []
#     for d in data:
#         z.append((d[0],d[1],d[2],d[3],d[4]),d[5])
#     con.commit()
#     con.close()
#     db.connections.close_all()

#     return z


def login(data):
    con = sqlite3.connect("Leetcode.db",timeout=10)
    c = con.cursor()
    # print('>>>>>>>>>>>>>>>>>>',data)
    data = (data[0],data[1])
    
    c.execute(f"SELECT * FROM admins WHERE username='{data[0]}' AND password='{data[1]}' ")
    print(c.fetchall())
    con.commit()
    con.close()
    db.connections.close_all()
    return c   



