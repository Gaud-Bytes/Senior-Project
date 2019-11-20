import sqlite3 as sql

conn = sql.connect('GameData.db')
c = conn.cursor()

#creates TABLE if doesn't exist and VACUUM frees all empty memoty space to prevent database corruption
c.execute('''VACUUM;''')
c.execute('''DROP TABLE IF EXISTS BOARD;''')
c.execute('''DROP TABLE IF EXISTS SPACE_EVAL;''')

#U is for unknown, E is for missed or unavailable, S is for a success
c.execute('''CREATE TABLE IF NOT EXISTS SPACE_EVAL(
        SPACE_EVAL_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        SPACE_EVAL_LEFT varchar(1) NOT NULL DEFAULT 'U',
        SPACE_EVAL_UP varchar(1) NOT NULL DEFAULT 'U',
        SPACE_EVAL_RIGHT varchar(1) NOT NULL DEFAULT 'U',
        SPACE_EVAL_DOWN varchar(1) NOT NULL DEFAULT 'U',
        SPACE_EVAL_SUCCESS INT NOT NULL DEFAULT 0,
        SPACE_EVAL_TOTAL INT NOT NULL DEFAULT 0
    );''')

#Initialize all possible Space States
evals = ['U', 'E', 'S']
for x in evals:
    for y in evals:
        for z in evals:
            for i in evals:
                c.execute('''INSERT INTO SPACE_EVAL(SPACE_EVAL_LEFT, SPACE_EVAL_UP, SPACE_EVAL_RIGHT, SPACE_EVAL_DOWN) 
                             VALUES(?, ?, ?, ?);''', (x, y, z, i))

#default situation of all adjacents unknown non edge squares
#c.execute('''INSERT INTO SPACE_EVAL(SPACE_EVAL_LEFT) VALUES('U');''')

#default for 4 corners

#TOP LEFT
#c.execute('''INSERT INTO SPACE_EVAL(SPACE_EVAL_LEFT, SPACE_EVAL_UP) VALUES('E', 'E');''')

#BOTTOM LEFT
#c.execute('''INSERT INTO SPACE_EVAL(SPACE_EVAL_LEFT, SPACE_EVAL_DOWN) VALUES('E', 'E');''')

#TOP RIGHT
#c.execute('''INSERT INTO SPACE_EVAL(SPACE_EVAL_RIGHT, SPACE_EVAL_UP) VALUES('E', 'E');''')

#BOTTOM RIGHT
#c.execute('''INSERT INTO SPACE_EVAL(SPACE_EVAL_RIGHT, SPACE_EVAL_DOWN) VALUES('E', 'E');''')

#defaul for 4 edges of Board

#LEFT EDGE
#c.execute('''INSERT INTO SPACE_EVAL(SPACE_EVAL_LEFT) VALUES('E');''')

#TOP EDGE
#c.execute('''INSERT INTO SPACE_EVAL(SPACE_EVAL_UP) VALUES('E');''')

#RIGHT EDGE
#c.execute('''INSERT INTO SPACE_EVAL(SPACE_EVAL_RIGHT) VALUES('E');''')

#BOTTOM EDGE
#c.execute('''INSERT INTO SPACE_EVAL(SPACE_EVAL_DOWN) VALUES('E');''')
        
#saves
conn.commit()
print("DATABASE IS SOURCED")

#test that the fields are all correct after the commit
c.execute('''SELECT * FROM SPACE_EVAL''')

rows = c.fetchall()

for row in rows:
    print(row)

#closes connection
c.close()
conn.close()


