class HttpUnprocessableEntityError(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.stataus_code = 422
        self.name = "UnprocessableEntity"
        self.message = message
