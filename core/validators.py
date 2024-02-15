from django.core.exceptions import ValidationError
def email_validator(value):
    if not "gmail" in value:
        raise  ValidationError("Invalid email address")
    return value