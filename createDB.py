import sqlite3 as sql

conn = sql.connect('GameData.db')
c = conn.cursor()

#creates TABLE if doesn't exist and VACUUM frees all empty memoty space to prevent database corruption
c.execute('''VACUUM;''')
c.execute('''DROP TABLE IF EXISTS BOARD;''')
c.execute('''DROP TABLE IF EXISTS SPACE_EVAL;''')

c.execute('''CREATE TABLE IF NOT EXISTS BOARD(
                BOARD_X INT NOT NULL,
                BOARD_Y INT NOT NULL,
                BOARD_SUCCESS INT NOT NULL DEFAULT 0,
                BOARD_TOTAL INT NOT NULL DEFAULT 0,
                PRIMARY KEY (BOARD_X, BOARD_y)
            );''')

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


#Initialize BOARD space
for x in range(0, 10):
    for y in range(0, 10):
        c.execute('''INSERT INTO BOARD (BOARD_X, BOARD_Y) VALUES (?, ?)''', (x, y))

#Initialize all possible Space States
evals = ['U', 'E', 'S']
for x in evals:
    for y in evals:
        for z in evals:
            for i in evals:
                c.execute('''INSERT INTO SPACE_EVAL(SPACE_EVAL_LEFT, SPACE_EVAL_UP, SPACE_EVAL_RIGHT, SPACE_EVAL_DOWN) 
                             VALUES(?, ?, ?, ?);''', (x, y, z, i))
        
#saves
conn.commit()
print("DATABASE IS SOURCED")

#test that the fields are all correct after the commit
c.execute('''SELECT * FROM SPACE_EVAL''')

rows = c.fetchall()

print("SPACE_EVAL")
for row in rows:
    print(row)

c.execute('''SELECT * FROM BOARD''')
s = c.fetchall()

print("BOARD")
for row in s:
    print(row)
#closes connection
c.close()
conn.close()


