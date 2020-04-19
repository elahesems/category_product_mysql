import mysql.connector


class DataProviderCategory:
    def insert(self,category):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                database="ecommerce",
                user="root",
                password="99426306100")
            query = "INSERT INTO category (Name,Dscription) VALUES ('{0}','{1}')".format(category.getName(),category.getDescription())

            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            print(cursor.rowcount, "record inserted successfully")
            cursor.close()
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ex:
            print(ex)
        finally:
            if connection.is_connected():
                connection.close()
                print("Mysql connection is closed")

    def getList(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                database="ecommerce",
                user="root",
                password="99426306100")

            query = "SELECT * FROM category"
            cursor = connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            print("Total Category Number : {0}".format(cursor.rowcount))

            for row in records:
                print("Id          : {0}".format(row[0]))
                print("Name        : {0}".format(row[1]))
                print("Description : {0}".format(row[2]))
                print("**********************************")

        except:
            print()

