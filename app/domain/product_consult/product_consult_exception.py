class ProductConsultError(Exception):
    message = "Product Consult not registered."

    def __str__(self):
        return ProductConsultError.message
