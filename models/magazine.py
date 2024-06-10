from database.connection import get_db_connection

class Magazine:
    def __init__(self, magazine_id, name, category):
        self._id = None
        self.id = magazine_id

        self._name = None
        self.name = name
        
        self._category = None
        self.category = category

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, magazine_id):
        if not isinstance(magazine_id, int):
            raise TypeError("Magazine ID must be an integer")
        else:
            self._id = magazine_id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def id(self, name):
        if not (isinstance(name, str) and 2<= len(name) <= 16):
            raise TypeError("Magazine name must be  a string that's between 2 and 16 characters long.")
        else:
            self._name = name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if not (isinstance(category, str) and 0 < len(category)):
            raise TypeError("Magazine category must be  anon-empty string")
        else:
            self._category = category

    def add_to_magazines():
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO magazines(name, category)
            VALUES (?,?)
        """
        cursor.execute(sql, (self.name, self.category))
        conn.commit()
        conn.close()

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            SELECT articles.id, articles.title, articles.content
            FROM articles
            JOIN magazines ON articles.magazine_id = magazine.id
            WHERE magazines.id =?
        """
        cursor.execute(sql, (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            SELECT DISTINCT authors.id, authors.name
            FROM articles
            JOIN authors ON articles.author_id = authors.id
            WHERE magazines.id = ?
        """
        cursor.execute(sql, (self.id,))
        contributors = cursor.fetchall()
        conn.close()
        return contributors

    def article_titles(self):
        conn = get_db_connection
        cursor = conn.cursor()
        sql = """
            SELECT title
            FROM articles
            WHERE magazine_id = ?
        """
        cursor.execute(sql, (self.id,))
        article_titles = [row[0] for row in cursor.fetchall()]
        return article_titles

    def contributing_authors(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
            SELECT authors.id, authors.name
            FROM articles
            JOIN authors ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING count(*) > 2
        """
        cursor.execute(sql, (self.id,))
        contributing_authors = cursor.fetchall()
        return [Author(author[0], author[1]) for author in contributing_authors] if contributing_authors else None


    def __repr__(self):
        return f'<Magazine {self.name}>'
    
    