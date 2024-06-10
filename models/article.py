
from database.connection import get_db_connection

class Article:
    def __init__(self, article_id, title, content, author_id, magazine_id):
        self.id = article_id
        self._title = None
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, '_title') and self._title is not None:
            raise AttributeError("Article title has already been set")
        if not (isinstance(title, str) and 5 <= len(title) <= 50):
            raise TypeError("Article title must be a string between 5 and 50 characters")
        self._title = title

    @property
    def author(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            SELECT authors.id, authors.name
            FROM articles
            JOIN authors ON articles.author_id = authors.id
            WHERE articles.id =?
        """
        cursor.execute(sql, (self.id,))
        author = cursor.fetchone()
        conn.close()
        return author
    
    @property
    def magazine(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            SELECT magazines.id, magazines.name, magazines.category
            FROM articles
            JOIN magazines ON articles.magazine_id = magazines.id
            WHERE articles.id =?
        """
        cursor.execute(sql, (self.id,))
        magazine = cursor.fetchone()
        conn.close()
        return magazine

    def add_to_articles():
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO articles(title, content, author_id, magazine_id)
            VALUES (?,?,?,?)
        """
        cursor.execute(sql, (self.title, self.content, self.author_id, self.magazine_id))
        conn.commit()
        conn.close()

    def __repr__(self):
        return f'<Article {self.title}>'
