from source.data.dataProviderProduct import DataProviderProduct
from source.domain.product import Product

dataProviderProduct = DataProviderProduct()



product = Product()

product.setName("Mobile Phone 1100")

product.setDescription("Mobile Phone Description 1100")

product.setPrice("5000$")

product.setCategoryId("PP")




dataProviderProduct.getList()
#dataProviderProduct.insert(product)
#dataProviderProduct.getList()
#print("******************Update******************")
product.setId(2)
dataProviderProduct.update(product)
#dataProviderProduct.getById(5)
#dataProviderProduct.delete(7)
