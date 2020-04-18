from source.data.dataProviderCategory import DataProviderCategory
from source.domain.category import Category

dataProviderCategory = DataProviderCategory()

category = Category()
category.setName("Mobile Phone 1100")
category.setDescription("Mobile Phone Description 1100")


dataProviderCategory.getList()
#dataProviderCategory.insert(category)
#dataProviderCategory.getList()
#print("******************Update******************")
#category.setId(5)
#dataProviderCategory.update(category)
#dataProviderCategory.getById(5)
#dataProviderCategory.delete(7)
