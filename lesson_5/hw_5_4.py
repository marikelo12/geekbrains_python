slovar = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
new_text = []
with open('text_5_4_1.txt') as my_numbers:
    for line in my_numbers:
        element = line.split(' ', 1)
        a = slovar.get(element[0])
        element.pop(0)
        element.insert(0, a)
        new_line = ' '.join(element)
        print(new_line)
        new_text.append(new_line)

with open('text_5_4_2.txt', 'w') as my_obj_2:
    my_obj_2.writelines(new_text)
