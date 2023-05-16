from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters!')


def validate_first_letter_to_be_capital(value):
    if value[0].islower():
        raise ValidationError('Value must starts with capital letter!')


def validate_letters_numbers_space_and_dash(value):
    for ch in value:
        if not (ch.isalpha() or ch.isdigit() or ch == ' ' or ch == '-'):
            raise ValidationError('Value must contain only letters, numbers and "-"!')