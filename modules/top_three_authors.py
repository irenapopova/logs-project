from modules import connection
from modules import formatter


def get_top_three_authors():
    
    db_connection = connection.get_connection()
    cursor = db_connection.cursor()
    top_three_authors = """
        SELECT name, author, title, path, COUNT(path) AS hits
        FROM articles, log, authors
        WHERE log.path = CONCAT('/article/', articles.slug)
        AND articles.author = authors.id
        GROUP BY path, title, name, author
        ORDER BY hits DESC;
    """
    cursor.execute(top_three_authors)
    return cursor.fetchall()


def print_top_three_authors():
    print("Top Authors:")
    formatter.repeat_separator()
    for item in get_top_three_authors():
        print( "'"+str(item[2]) +
              "', by the author '" + str(item[0]) +
              "' on the page '" + str(item[3]) +
              "' are " + formatter.format_num(item[4]) + '.')
        print("")
    formatter.repeat_separator()
