import os
from dotenv import load_dotenv
from mysql import connector
from prefect import task

load_dotenv()

# Configuración de conexión a la base de datos
config = {
    "host": "localhost",
    "user": "root",
    "password": os.getenv("DB_PASSWORD"),
    "database": "db_codigo_amazon"
}

@task(name="Limpieza y carga de productos en la bd")
def task_load_products_baseline(products):
    with connector.connect(**config) as db:
        with db.cursor() as cursor:
            try:
                cursor.execute("DROP TABLE IF EXISTS product")
                db.commit()

                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS product (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        title VARCHAR(200) UNIQUE,
                        price FLOAT,
                        discount INT,
                        free_shipping BOOL,
                        rating FLOAT,
                        reviews INT,
                        variations INT,
                        best_seller BOOL
                    )
                """)
                db.commit()
            except Exception as error:
                print("Error: ", error)

            query_insert = """
                INSERT INTO product (title, price, discount, free_shipping, rating, reviews, variations, best_seller)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            try:
                cursor.executemany(query_insert, products)
                db.commit()
            except Exception as error:
                print("Error: ", error)

@task(name="Cargar nuevos productos en la bd")
def task_load_products_update(products):
    with connector.connect(**config) as db:
        with db.cursor() as cursor:
            query_insert = """
                INSERT INTO product (title, price, discount, free_shipping, rating, reviews, variations, best_seller)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    price = VALUES(price)
            """
            for product in products:
                try:
                    cursor.execute(query_insert, product)
                    db.commit()
                except Exception as error:
                    print("Error: ", error)