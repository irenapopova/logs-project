import psycopg2


def get_connection():
    db = psycopg2.connect("dbname=news user=postgres password=postgres host=localhost port=5432")
    return db

def listAuthors(cursor):
    
    cursor.execute("SELECT * FROM public.authors")
    for record in cursor: #it starts the loop
        #<40 fix the length of the first column to 40 characters and add space betwwen line
        print(f'{record[0]: <40}| {record[1]: <25} | {record[2]}')#the recort is a parameter i pass to the print function

def listArticles(cursor):
    cursor.execute("SELECT * FROM public.articles")
    
    for record in cursor: #it starts the loop
        print(f'{record[1]: <40}|{record[2]}')

# the cursor is the object
# above function execute an sql query

if __name__ == '__main__':
    db = get_connection()
    listArticles(db.cursor()) #calling the cursor function of the db object
    listAuthors(db.cursor())
    #the scope of the variable is limited to the function
