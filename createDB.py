import sqlite3 as sql

conn = sql.connect('GameData.db')
c = conn.cursor()

#creates TABLE if doesn't exist and VACUUM frees all empty memoty space to prevent database corruption
c.execute('''VACUUM;''')
c.execute('''DROP TABLE IF EXISTS BOARD;''')

c.execute('''CREATE TABLE IF NOT EXISTS BOARD(
    BOARD_X INT NOT NULL,
    BOARD_Y INT NOT NULL,
    BOARD_WEIGHT INT NOT NULL DEFAULT 1,
    PRIMARY KEY(BOARD_X, BOARD_Y)
    );''')

for x in range(0, 10):
    for y in range(0, 10):
        c.execute('''INSERT INTO BOARD (BOARD_X, BOARD_Y) VALUES (?, ?)''', (x, y))
        
#saves
conn.commit()
print("DATABASE IS SOURCED")

#test that the fields are all correct after the commit
c.execute('''SELECT * FROM BOARD''')

rows = c.fetchall()

for row in rows:
    print(row)

#closes connection
c.close()
conn.close()


