from connect import ConnectDatabase
from scraping import Scraping


class OracleProcess:

    def insert_product(self, url, title, price):
        price = str(price)
        sql = ('insert into products(site_url, product_title, product_price) '
               'values(:url, :title, :price)')
        connect_oracle = ConnectDatabase()
        try:
            with connect_oracle.connection.cursor() as cursor:
                cursor.execute(sql, [str(url), str(title), float(price)])
                connect_oracle.connection.commit()
            return "Data inserted..."
        except Exception as error:
            return error
        finally:
            connect_oracle.connection.close()
