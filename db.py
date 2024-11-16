import sqlite3
class DatabaseManager:
    def __init__(self, dbname,):
        self.conn = sqlite3.connect("blog.db")
        self.cursor = self.conn.cursor()
    

    def get_all_articles(self):
        self.cursor.execute("""SELECT * FROM articles""")
        data =self.cursor.fetchall()
        return data  