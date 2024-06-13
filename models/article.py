from database.connection import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @property
    def author(self):
        from models.author import Author
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors WHERE id = ?', (self.author_id,))
        author_info = cursor.fetchone()
        conn.close()
        if author_info:
            return Author(author_info["id"], author_info["name"])
        else:
            return None

    @property
    def magazine(self):
        from models.magazine import Magazine
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines WHERE id = ?', (self.magazine_id,))
        magazine_info = cursor.fetchone()
        conn.close()
        if magazine_info:
            return Magazine(magazine_info["id"], magazine_info["name"], magazine_info["category"])
        else:
            return None

    def __repr__(self):
        return f'Article(title={self.title}, content={self.content}, author_id={self.author_id}, magazine_id={self.magazine_id})'
