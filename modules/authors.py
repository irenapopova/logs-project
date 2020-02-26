from modules import connection
from modules import formatter
from tabulate import tabulate


def authors():
    
    db_connection = connection.get_connection()
    cursor = db_connection.cursor()
    popular_authors = """
        SELECT name,title,path,count(title) AS views
        FROM articles,log,authors
        WHERE log.path = CONCAT('/article/', articles.slug)
        AND articles.author = authors.id
        GROUP BY path, title, name ORDER BY views DESC LIMIT 3;"""
    
    cursor.execute(popular_authors)
    return cursor.fetchall()


def print_authors():
    print("Top Authors:")
    print()
    print(tabulate([
        {
            "Title": title,
            "Author": author,
            "Page": page,
            "Numbers of views": result
        } for (author, title, page, result) in authors()], headers="keys")) # MODIFY EVERY ELEMENT 
    print()
