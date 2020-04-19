from source.domain.base import Base


class Category(Base):
    def __init__(self, id=None, name=None, description=None):
        super().__init__(id)
        self.name = name
        self.description = description

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description
