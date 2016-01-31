from hashids import Hashids
from werkzeug.routing import BaseConverter, ValidationError

from server.extensions import cache

class BoolConverter(BaseConverter):
    def __init__(self, url_map, false_value, true_value):
        super(BoolConverter, self).__init__(url_map)
        self.false_value = false_value
        self.true_value = true_value
        self.regex = '(?:{0}|{1})'.format(false_value, true_value)

    def to_python(self, value):
        return value == self.true_value

    def to_url(self, value):
        return self.true_value if value else self.false_value

class HashidConverter(BaseConverter):
    # ID hashing configuration.
    # DO NOT CHANGE ONCE THE APP IS PUBLICLY AVAILABLE. You will break every
    # link with an ID in it.
    hashids = Hashids(min_length=6)

    def to_python(self, value):
        numbers = self.hashids.decode(value)
        if len(numbers) != 1:
            raise ValidationError('Could not decode hash {} into ID'.format(value))
        return numbers[0]

    def to_url(self, value):
        return self.hashids.encode(value)
