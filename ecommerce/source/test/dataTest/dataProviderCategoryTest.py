from source.data.dataProviderCategory import DataProviderCategory
from source.domain.category import Category

dataProviderCategory = DataProviderCategory()

category = Category()
category.setName("Mobile Phone ---")
category.setDescription("Mobile Phone777 Description")

dataProviderCategory.insert(category)
dataProviderCategory.getList()
