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


def import_data(db_connection):
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

        db_connection.session.add(model(id=record.get('pk'), **record.get('fields')))
        db_connection.session.commit()


def get_publisher(db_connection):
    all_publishers = db_connection.session.query(Publisher).all()

    for p in all_publishers:
        print(f"{p.id} - {p.name}")

    result = input("Please input publisher's ID or Name: ")

    return result


def get_invoices(db_connection, publisher):
    invoices = db_connection.session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)\
        .select_from(Shop).join(Stock).join(Book).join(Publisher).join(Sale)

    if publisher.isdigit():
        invoices_filtered = invoices.filter(Publisher.id == publisher).all()
    else:
        invoices_filtered = invoices.filter(Publisher.name == publisher).all()

    for book_title, shop_name, price, date_sale in invoices_filtered:
        print(f"{book_title: <40} | {shop_name: <10} | {price: <8} | {date_sale.strftime('%d-%m-%Y')}")


if __name__ == "__main__":
    conn = Connect()

    # Create tables
    if create_table:
        print(f"Connect to db: {DSN}")
        create_tables(engine)

    # Load data
    if load_data:
        print("Load data:")
        import_data(conn)

    # Input publisher by ID or Name and get invoices
    get_invoices(conn, get_publisher(conn))
