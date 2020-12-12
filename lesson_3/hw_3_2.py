def user_info(name, surname, year, city, email, phone):
    print(f"Меня зовут {name} {surname}. Я {year} года рождения. Живу в городе {city}. Моя почта {email} и "
          f"телефон - {phone}")
    return ''


user = {
    'name': input("Введите Ваше имя: "),
    'surname': input("Введите Вашу фамилию: "),
    'year': input("Введите год рождения: "),
    'city': input("Введите город проживания: "),
    'email': input("Введите электронную почту: "),
    'phone': input("Введите Ващ телефонный номер: ")
}
print(user_info(**user))
