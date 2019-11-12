import sqlite3 as sql

conn = sql.connect('GameData.db')
c = conn.cursor()

c.execute('''DROP TABLE BOARD;''')

c.execute('''CREATE TABLE BOARD(
    BOARD_X INT NOT NULL,
    BOARD_Y INT NOT NULL,
    BOARD_WEIGHT INT NOT NULL DEFAULT 1,
    PRIMARY KEY(BOARD_X, BOARD_Y)
    );''')

for x in range(0, 10):
    for y in range(0, 10):
        c.execute('''INSERT INTO BOARD (BOARD_X, BOARD_Y) VALUES (?, ?)''', (x, y))

conn.commit()
print("DATABASE IS SOURCED")

c.execute('''SELECT * FROM BOARD''')

rows = c.fetchall()

for row in rows:
    print(row)

conn.close()


