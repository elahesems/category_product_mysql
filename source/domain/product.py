from source.domain.base import Base


class Product(Base):
    def __init__(self, id=None, name=None, description=None, price=None, categoryId=None):
        super().__init__(id)
        self.name = name
        self.description = description
        self.price = price
        self.categoryId = categoryId

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description

    def setPrice(self, price):
        self.price = price

    def setCategoryId(self, categoryId):
        self.categoryId = categoryId

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.price

    def getCategoryId(self):
        return self.categoryId
