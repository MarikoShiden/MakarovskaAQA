is_number = lambda s: s.replace('.', '', 1).isdigit() if s.count('.') <= 1 else False

input_string = input('Enter symbols without space: ')

if is_number(input_string):
    print(f'"{input_string}" is a number.')
else:
    print(f'"{input_string}" is not a number.')
