class ProductNotFoundError(Exception):
    message = "Product not found."

    def __str__(self):
        return ProductNotFoundError.message
    
class SkuAlreadyExistError(Exception):
    message = "Sku already exists"

    def __str__(self):
        return SkuAlreadyExistError.message