def fix_error(data):
    if data is not None and 'items' in data:
        return [item['name'] for item in data['items']]
    return []

# Misol ma'lumotlar
data = {
    'items': [
        {'name': 'Item 1'},
        {'name': 'Item 2'},
        {'name': 'Item 3'}
    ]
}

print(fix_error(data))  # ['Item 1', 'Item 2', 'Item 3']

data = None
print(fix_error(data))  # []

data = {
    'items': []
}
print(fix_error(data))  # []

data = {
    'items': None
}
print(fix_error(data))  # []
