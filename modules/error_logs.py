from modules import connection
from modules import formatter


def get_top_three_articles():
    db_connection = connection.get_connection()
    # You need to join the logs to the path
    cursor = db_connection.cursor()
    error_reports = """
        SELECT time::DATE,
        SUM (
            CASE WHEN status = '200 OK'
            THEN 1
            ELSE 0
            END) AS success,
        SUM (
            CASE WHEN status  =  '404 NOT FOUND.'
            THEN 1
            ELSE 0
            END) AS error
        FROM log GROUP BY time::DATE;
    """
    cursor.execute(error_reports)
    return cursor.fetchall()


def print_error_logs():
    print("Top articles:")
    formatter.repeat_separator()
    for item in get_top_three_articles():
        pass

    formatter.repeat_separator()
