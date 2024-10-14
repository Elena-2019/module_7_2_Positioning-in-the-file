def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')

    number_str = 1
    strings_positions = {}

    for string in strings:
        numbers_byte = file.tell()
        file.write(f'{string}\n')
        strings_positions[(number_str, numbers_byte)] = string
        number_str += 1
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
