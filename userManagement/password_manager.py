from django.contrib.auth.hashers import BasePasswordHasher
from collections import OrderedDict


def is_password_usable(encoded):
    print(encoded)
    return True


class BudgetHasher(BasePasswordHasher):
    algorithm = "Budget"

    def verify(self, password, encoded):
        return encoded == self.encode(password)

    def encode(self, password, salt=None):
        return password + 'secure'

    def safe_summary(self, encoded):
        return OrderedDict([
            (_('algorithm'), "Budget"),
            (_('iterations'), "At least 1"),
            (_('salt'), "No salt"),
            (_('hash'), "No hash"),
        ])
