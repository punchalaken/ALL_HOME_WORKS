from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale
from sql_login import login, password, host, port, database_name
import json
import os


def books():
    pub = input('Введите имя автора: ')
    for title, name, price, ds in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).\
        join(Shop).join(Sale).filter(Publisher.name == pub).all():
        print(f"{title} | {name} | {price} | {ds.strftime('%d-%m-%Y')}")


if __name__ == '__main__':
    DSN = f'postgresql://{login}:{password}@{host}:{port}/{database_name}'
    engine = create_engine(DSN)

    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    file_path = os.path.join('fixtures', 'tests_data.json')

    with open(file_path, 'r') as td:
        data = json.load(td)
        for record in data:
            model = {
                'publisher': Publisher,
                'shop': Shop,
                'book': Book,
                'stock': Stock,
                'sale': Sale,
            }[record.get('model')]
            session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()



    books()