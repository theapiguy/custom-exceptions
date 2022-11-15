#  Custom Python Exceptions

class ReadError(Exception):
    def __init__(self, filename, record_key, message='Unable to read record.'):
        self.message = message
        self.filename = filename
        self.record_key = record_key
        super().__init__(self.message)

    def __str__(self):
        return '{}, {}>{}'.format(self.message, self.filename, self.record_key)


class RecordNotFound(Exception):
    def __init__(self, filename, record_key, message='Record not found.'):
        self.message = message
        self.filename = filename
        self.record_key = record_key
        super().__init__(self.message)

    def __str__(self):
        return '{}, {}>{}'.format(self.message, self.filename, self.record_key)


class MultipleRecordsFound(Exception):
    def __init__(self, filename, record_key, message='Multiple records found.'):
        self.message = message
        self.filename = filename
        self.record_key = record_key
        super().__init__(self.message)

    def __str__(self):
        return '{}, {}>{}'.format(self.message, self.filename, self.record_key)


if __name__ == "__main__":
    raise ReadError(filename='customer', record_key='1111111111')

