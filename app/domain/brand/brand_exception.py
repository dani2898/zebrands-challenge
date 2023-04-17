class BrandNotFoundError(Exception):
    message = "Brand not found."

    def __str__(self):
        return BrandNotFoundError.message