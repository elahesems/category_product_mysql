import mysql.connector

from source.data.connectionStrings import ConnectionStrings


class DataProviderCategory:
    connection = None

    def insert(self, category):
        try:
            self.connection = ConnectionStrings.connectionStringEcommerce()
            query = "INSERT INTO category (Name,Description) VALUES ('{0}','{1}')" \
                .format(category.getName(), category.getDescription())

            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print(cursor.rowcount, "record inserted successfully")
            cursor.close()
        except mysql.connector.Error as mysqlError:
            print(mysqlError.msg)
        except Exception as ex:
            print(ex)
        finally:
            if self.connection.is_connected():
                self.connection.close()
                print("Mysql connection is closed")

    def update(self, category):
        try:
            self.connection = ConnectionStrings.connectionStringEcommerce()

            print("Before Updating Process")
            self.getById(category.getId())
            cursor = self.connection.cursor()

            sqlUpdateQuery = "UPDATE category SET Name='{0}', Description='{1}' WHERE id={2}" \
                .format(category.getName(), category.getDescription(), category.getId())
            cursor.execute(sqlUpdateQuery)
            self.connection.commit()
            print("Record is updated successfully")

            print("After Updating Record")
            self.getById(category.getId())

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
            print("Select Specific Category")
            selectQuery = "SELECT * FROM category WHERE id = {0}".format(id)
            cursor.execute(selectQuery)
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
            query = "SELECT * FROM category"
            cursor = self.connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            print("Total Category Number : {0}".format(cursor.rowcount))

            for row in records:
                print("Id          : {0}".format(row[0]))
                print("Name        : {0}".format(row[1]))
                print("Description : {0}".format(row[2]))
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
                sqlDeletionQuery = "DELETE FROM category WHERE Id = {0}".format(id)
                cursor.execute(sqlDeletionQuery)
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
