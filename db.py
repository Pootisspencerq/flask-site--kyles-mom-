import sqlite3

class DatabaseManager:
    def __init__(self, dbname):
        self.dbname = dbname

    def get_all_articles(self):
        try:
            with sqlite3.connect(self.dbname) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM articles")
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def get_article(self, article_id):
        try:
            with sqlite3.connect(self.dbname) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM articles WHERE id=?", (article_id,))
                return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None
