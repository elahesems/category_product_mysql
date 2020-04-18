import mysql.connector

from source.data import connectionStrings
from source.data.connectionStrings import ConnectionStrings


class DataProviderProduct:
    connection = None

    def insert(self,product):

        try:
            self.connection = connectionStrings.connectionStringEcommerce()
            query = "INSERT INTO product (Name,Description,Price,CategoryId) VALUES ('{0}','{1}','{2}','{3}')"\
                .format(product.getName(), product.getDescription(), product.getPrice(), product.getCategoryId())

            cursor= self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print(cursor.rowcount,"record inserted successfully")
            cursor.close()
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ex:
            print(ex)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("Mysql connection is closed")



    def update(self,product):
        try:
            self.connection = ConnectionStrings.connectionStringEcommerce()

            print("Before Updating Process")
            self.getById(product.getId())
            cursor = self.connection.cursor()

            query = "UPDATE product SET Name='{0}', Description='{1}', Price={2}, CategoryId={3} WHERE id={4}" \
            .format(product.getName(), product.getDescription(), product.getPrice(), product.getCategoryId(), product.getId())

            cursor.execute(query)
            self.connection.commit()
            print("Record is updated successfully")

            print("After Updating Record")
            self.getById(product.getId())

        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ex:
            print(ex)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("Mysql connection is closed")


    def getById(self, id):
        try:
            self.connection = ConnectionStrings.connectionStringEcommerce()
            cursor = self.connection.cursor()
            print("Select Specific product")
            query = "SELECT * FROM product WHERE id = {0}".format(id)
            cursor.execute(query)
            record = cursor.fetchone()
            print(record)
            return record


        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ex:
            print(ex)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("Mysql connection is closed")


    def getList(self):
        try:
            self.connection = ConnectionStrings.connectionStringEcommerce()
            query = "SELECT * FROM product"
            cursor = self.connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            print("Total product Number : {0}".format(cursor.rowcount))

            for row in records:
                print("Id          : {0}".format(row[0]))
                print("Name        : {0}".format(row[1]))
                print("Description : {0}".format(row[2]))
                print("Price       : {0}".format(row[3]))
                print("CategoryId  : {0}".format(row[4]))
                print("__________________________________")
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ex:
            print(ex)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("Mysql connection is closed")

    def delete(self, id):
        try:

            result = self.getById(id)
            if result is not None:
                self.connection = ConnectionStrings.connectionStringEcommerce()
                cursor = self.connection.cursor()
                query = "DELETE FROM product WHERE Id = {0}".format(id)
                cursor.execute(query)
                self.connection.commit()
            else:
                return False
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ex:
            print(ex)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("Mysql connection is closed")