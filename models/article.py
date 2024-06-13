from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    create_tables()

    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM authors WHERE name = ?', (author_name,))
    
    author_information = cursor.fetchone()

    
    if author_information:
        author_id = author_information[0]
    else:
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
        author_id = cursor.lastrowid

    cursor.execute('SELECT id FROM magazines WHERE name = ?', (magazine_name,))
    magazine_info = cursor.fetchone()

    if magazine_info:
        magazine_id = magazine_info[0]
    
    else:
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (magazine_name, magazine_category))
        magazine_id = cursor.lastrowid

    conn.commit()
    conn.close()

    article = Article(None, article_title, article_content, author_id, magazine_id)

    show_all()

def show_all():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM authors LIMIT 5')
    authors = cursor.fetchall()

    cursor.execute('SELECT * FROM articles LIMIT 5')
    articles = cursor.fetchall()

    cursor.execute('SELECT * FROM magazines LIMIT 5')
    magazines = cursor.fetchall()

    conn.close()

    print("\nMagazines:")
    for magazine in magazines:
        print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

    print("\nAuthors:")
    for author in authors:
        print(Author(author["id"], author["name"]))

    print("\nArticles:")
    for article in articles:
        print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))

    
if __name__ == "__main__":
    main()