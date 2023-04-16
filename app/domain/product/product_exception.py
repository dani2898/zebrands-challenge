class ProductNotFoundError(Exception):
    message = "Product not found."

    def __str__(self):
        return ProductNotFoundError.message