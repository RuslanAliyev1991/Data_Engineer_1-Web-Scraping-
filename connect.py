import cx_Oracle

import config


class ConnectDatabase:
    connection = None

    def __init__(self):
        try:
            self.connection = cx_Oracle.connect(config.username, config.password, config.dsn, encoding=config.encoding)
            # show the version of the Oracle Database
            print("Connecting database...")
        except cx_Oracle.Error as error:
            print(error)
