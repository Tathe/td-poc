class AppError(Exception):
    '''
    Raise this exception for each generic and specific one
    In handler write handle section for this exception so that we can get proper error code and error_message
    '''

    def __init__(self, error_message, error_code=None, exception_class=None):
        Exception.__init__(self)
        self.error_message = error_message
        self.error_code = error_code
        self.exception_class = exception_class

    def get_error_code(self):
        return self.error_code

    def get_error_message(self):
        return self.error_message

    def set_error_message(self, error_message):
        self.error_message = error_message

    def set_error_code(self, error_code):
        self.error_code = error_code

    def __repr__(self):
        return '<AppError %r>' % self.error_code

    def as_dict(self):
        return {"error_code": self.error_code, "error_message": self.error_message,
                "exception_class": self.exception_class}
