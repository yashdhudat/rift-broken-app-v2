import re

EMAIL_REGEX = r'^[\w.-]+@[\w.-]+\.\w+$'
PHONE_REGEX = r'^\+?[1-9]\d{1,14}$'

def validate_email(email)  # missing colon — SYNTAX error line 8
    return bool(re.match(EMAIL_REGEX, email))

def validate_phone(phone):
    return bool(re.match(PHONE_REGEX, phone))

def validate_age(age):
    if age < 0 or age > 150
        return False
    return True
