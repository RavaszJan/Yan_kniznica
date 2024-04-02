import psycopg2
conn=psycopg2.connect(
    dbname="bzt8ja5y0liw4km0hwcr",
    user="u11fxhhcifz9zmbzqkoq",
    password="FQr5KnsfTOpEtGC35HJalo2DbABkd2",
    host="bzt8ja5y0liw4km0hwcr-postgresql.services.clever-cloud.com",
    port="50013",
)
print(conn)
cursor=conn.cursor()

class Genre:
    def __init__(self,name,description):
        self.name=name
        self.description=description

    def add_genre(self):
        cursor.execute("""
        INSERT INTO genres(name,description)
        VALUE (%s,%S)
        """,(self.name,self.description))



class Book:
    def __init__(self,title,author_ID,genre_ID,copies):
        self.title=title
        self.author_ID=author_ID
        # self.genre_ID=genre_ID
        self.copies=copies

    def add_book(self):
        cursor.execute("""
        INSERT INTO books(title,author_ID,genre_ID,copies)
        VALUES (%s,%s,%s,%s)
        """, (self.title, self.author_ID,self.genre_ID,self.copies))


genre_1=Genre("Fantasy","Literatura fantasy")
book_1=Book("Harry Potter",1,	1,3)
book_1.add_book()


# conn.comit()
