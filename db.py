import sqlite3


class Database:
    '''def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS privacy (id INTEGER PRIMARY KEY, name1 text, birth1 text, email1 text, name2 text, birth2 text, email2 text, name3 text, birth3 text, email3 text, name4 text, birth4 text, email4 text)")
        self.conn.commit()'''

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS privacy1 (id INTEGER PRIMARY KEY, name1 text, name2 text)")
        self.conn.commit()

    '''def fetch(self):
        self.cur.execute("SELECT * FROM privacy1")
        rows = self.cur.fetchall()
        return rows'''

    def insert2(self, name1, name2):
        self.cur.execute("INSERT INTO privacy1 VALUES (NULL, ?, ?)",
                         (name1, name2))
        self.conn.commit()

    def insert(self, name1, birth1, email1, name2, birth2, email2, name3, birth3, email3, name4, birth4, email4):
        self.cur.execute("INSERT INTO privacy VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (name1, birth1, email1, name2, birth2, email2, name3, birth3, email3, name4, birth4, email4))
        self.conn.commit()

    '''def remove(self, id):
        self.cur.execute("DELETE FROM privacy1 WHERE id=?", (id,))
        self.conn.commit()'''

    '''def update(self, id, name1, birth1, email1, name2, birth2, email2, name3, birth3, email3, name4, birth4, email4):
        self.cur.execute(
            "UPDATE privacy SET name1 = ?, birth1 = ?, email1 = ?, name2 = ?, birth2 = ?, email2 = ?, name3 = ?, birth3 = ?, email3 = ?, name4 = ?, birth4 = ?, email4 = ?",
            (id, name1, birth1, email1, name2, birth2, email2, name3, birth3, email3, name4, birth4, email4))
        self.conn.commit()'''

    def __del__(self):
        self.conn.close()


db = Database('store.db')


