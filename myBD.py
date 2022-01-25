import sqlite3

class myBDS():

    def create_bd(self):
        try:
            conn = sqlite3.connect("Score.db")
            cursor = conn.cursor()
            cursor.execute(
                """CREATE TABLE score (date STRING, colvo INTEGER)""")
            conn.close()
        except BaseException:
            f = open('logF.txt', 'a')
            f.write('Ошибка в myBDS create_bd' + '\n')

    def add_item(self, date: str, kolvo: int):
        try:
            conn = sqlite3.connect("Score.db")
            cursor = conn.cursor()
            cursor.execute(f"""INSERT INTO score VALUES ('{date}', {kolvo})""")
            conn.commit()
            conn.close()
        except BaseException:
            f = open('logF.txt', 'a')
            f.write('Ошибка в myBDS add_item' + '\n')

    def get_allitem(self):
        a = []
        try:
            conn = sqlite3.connect("Score.db")
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM score""")
            records = cursor.fetchall()
            for row in records:
                a.append([row[0], row[1]])
            conn.commit()
            conn.close()
            return a
        except BaseException:
            f = open('logF.txt', 'a')
            f.write('Ошибка в myBDS get_allitem' + '\n')

    def del_all(self):
        try:
            conn = sqlite3.connect("Score.db")
            cursor = conn.cursor()
            cursor.execute("""DROP TABLE score""")
            conn.commit()
            conn.close()
        except BaseException:
            f = open('logF.txt', 'a')
            f.write('Ошибка в myBDS del_all' + '\n')