import sqlite3 as sql

sourceDB = input("Source DB: ")
targetDB = input("Target DB: ")

sourceConn = sql.connect(str(sourceDB))
targetConn = sql.connect(str(targetDB))

sourceCursor = sourceConn.cursor()
targetCursor = targetConn.cursor()

targetCursor.execute('''VACUUM;''')
targetCursor.execute('''DROP TABLE IF EXISTS BOARD;''')
targetCursor.execute('''DROP TABLE IF EXISTS SPACE_EVAL;''')

#U is for unknown, E is for missed or unavailable, S is for a success
targetCursor.execute('''CREATE TABLE IF NOT EXISTS SPACE_EVAL(
        SPACE_EVAL_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        SPACE_EVAL_LEFT varchar(1) NOT NULL DEFAULT 'U',
        SPACE_EVAL_UP varchar(1) NOT NULL DEFAULT 'U',
        SPACE_EVAL_RIGHT varchar(1) NOT NULL DEFAULT 'U',
        SPACE_EVAL_DOWN varchar(1) NOT NULL DEFAULT 'U',
        SPACE_EVAL_SUCCESS INT NOT NULL DEFAULT 0,
        SPACE_EVAL_TOTAL INT NOT NULL DEFAULT 0
    );''')

targetCursor.execute('''CREATE TABLE IF NOT EXISTS BOARD(
                BOARD_X INT NOT NULL,
                BOARD_Y INT NOT NULL,
                BOARD_SUCCESS INT NOT NULL DEFAULT 0,
                BOARD_TOTAL INT NOT NULL DEFAULT 0,
                PRIMARY KEY (BOARD_X, BOARD_y)
            );''')

sourceCursor.execute('''SELECT * FROM SPACE_EVAL''')
space_evals = sourceCursor.fetchall()

for space_eval in space_evals:
    targetCursor.execute('''INSERT INTO SPACE_EVAL
                        (SPACE_EVAL_LEFT, SPACE_EVAL_UP, SPACE_EVAL_RIGHT, SPACE_EVAL_DOWN, SPACE_EVAL_SUCCESS, SPACE_EVAL_TOTAL) 
                        VALUES (?, ?, ? , ?, ?, ?);''', 
                        (space_eval[1], space_eval[2], space_eval[3], space_eval[4], space_eval[5], space_eval[6]))

sourceCursor.execute('''SELECT * FROM BOARD''')
spaces = sourceCursor.fetchall()

for space in spaces:
    targetCursor.execute('''INSERT INTO BOARD (BOARD_X, BOARD_y, BOARD_SUCCESS, BOARD_TOTAL)
                            VALUES (?, ?, ?, ?)''', (space[0], space[1], space[2], space[3]))

targetConn.commit()
print("DATABASE IS LOADED")

targetCursor.execute('''SELECT * FROM SPACE_EVAL''')
space_evals = targetCursor.fetchall()

for space_eval in space_evals:
    print(space_eval)

targetCursor.execute('''SELECT * FROM BOARD''')
spaces = targetCursor.fetchall()

for space in spaces:
    print(space)



sourceCursor.close()
targetCursor.close()
sourceConn.close()
targetConn.close()







