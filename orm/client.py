import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Shop, Book, Stock, Sale

DB_PORT = "5432"
DB_NAME = "publisher"
DB_HOST = "localhost"
DB_ENGINE = "postgresql"
DB_USERNAME = "postgres"
DB_PASSWORD = "RtpZV7ow"

DSN = "{}://{}:{}@{}:{}/{}".format(DB_ENGINE, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
engine = sqlalchemy.create_engine(DSN)

create_table = False
load_data = False


class Connect:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()


def import_data(conn):
    with open('fixtures/tests_data.json', 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]

        conn.session.add(model(id=record.get('pk'), **record.get('fields')))
        conn.session.commit()


if __name__ == "__main__":
    conn = Connect()

    if create_table:
        print(f"Connect to db: {DSN}")
        create_tables(engine)
    if load_data:
        print("Load data:")
        import_data(conn)

    q_publisher = conn.session.query(Publisher).all()

    for s in q_publisher:
        print(f"{s.id} - {s.name}")

    publisher_id = input("Please input ID a publisher: ")

    q_purchase_invoices = conn.session.query(Book).join(Stock.shop).join(Stock.book).join(Stock.shop)\
        .filter(Book.id_publisher == publisher_id)

    for purchase_invoice in q_purchase_invoices.all():
        print(purchase_invoice.id, purchase_invoice.title, purchase_invoice.id_publisher)

# SQL query
"""
    SELECT
    book.title as book_title,
    shop.name as shop_name,
    sale.price as price,
    sale.date_sale as date
    FROM book
    JOIN stock ON stock.id_book = book.id
    JOIN shop ON shop.id = stock.id_shop
    JOIN sale ON sale.id_stock = stock.id
    WHERE id_publisher = 1
    ORDER BY shop.name
"""

# SQl result
"""
    book_title	                                shop_name	price	date
    Programming Python, 4th Edition	            Amazon      16.00	2018-10-25
    Programming Python, 4th Edition	            Labirint    50.05	2018-10-25
    Natural Language Processing with Python	    Labirint    50.05	2018-10-25
"""
