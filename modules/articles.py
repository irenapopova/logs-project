from modules import connection
from modules import formatter
from tabulate import tabulate

def articles():
    #print("data{}".format(connection)) # string interpolation !/(comprehension/literals)
    #i CAN Add more objects bracket notation, separated by comma
    db_connection = connection.get_connection()
    #print("data{}".format(cursor))
    cursor = db_connection.cursor()
#python uses indentation to identify code blocks
    popular_articles = ("""
        SELECT title, path, COUNT(path) AS hits, authors.name
        FROM articles
        JOIN authors
        ON articles.author = authors.id
        JOIN log
        ON log.path = concat('/article/', articles.slug)
        GROUP BY title, path, authors.name
        ORDER BY hits DESC LIMIT 3;
    """)
    cursor.execute(popular_articles)
    return cursor






def print_articles():
    print("Top Articles:")
    print()
    print(tabulate([
        {
            "Title": title,
            "Author": author,
            "Page": page,
            "Numbers of views": views
        } for (title, page, views, author) in articles()], headers="keys")) # MODIFY EV
    print()

# with the for loop (list comprehension) I am getting all data details

   # (title, author, page, views) = ["Candidate is jerk, alleges rival",  "Rudolf von Treppenwitz"  , "/article/candidate-is-jerk", 338647]
   
   #     print(f"total views' {str(items[0])} " \
          #    f", by the author {str(items[3])} " \
          #    f" on the page {str(items[1])}" \
        #      f" are {formatter.format_num(int(items[2]))}.")
    #formatter.repeat_separator()
