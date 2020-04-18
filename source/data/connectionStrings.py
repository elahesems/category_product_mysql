import mysql


class ConnectionStrings:

    @staticmethod
    def connectionStringEcommerce():
        connection = mysql.connector.connect(
            host="localhost",
            database="ecommerce",
            user="root",
            password="99426306100")
        return connection
