from database.connection import get_db_connection
# retrieval of name property from the database.

class Author:
    def __init__(self, author_id, name):
        self._id = None
        self.id = author_id
        self._name = None
        self.name = name

    
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, author_id):
        if not isinstance(author_id, int):
            raise TypeError("Author ID must be an integer")
        else:
            self._id = author_id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError("Author name has already been set")
        if not isinstance(name, str) or len(name) == 0:
            raise TypeError("Author name must be a non-empty string")
        self._name = name

    def add_to_authors():
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO authors(name)
            VALUES (?)
        """
        cursor.execute(sql, (self.name,))
        conn.commit()
        conn.close()
    
    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            SELECT articles.id, articles.title, articles.content, articles.author_id, articles.magazine_id
            FROM articles
            JOIN authors ON articles.author_id = authors.id
            WHERE authors.id =?
        """
        cursor.execute(sql, (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles
    
    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            SELECT DISTINCT magazines.id, magazine.name, magazine.category
            FROM articles
            JOIN magazines ON articles.magazine_id = magazines.id
            WHERE articles.author_id =?
        """
        cursor.execute(sql, (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines


    def __repr__(self):
        return f'<Author {self.name}>'
    