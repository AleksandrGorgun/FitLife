# Проект FitLife - MVP версия 1.0


# 1. Знакомство
while True:
    user_name = input("Как тебя зовут? ").strip()
    if user_name:
        break
    print("Имя не может быть пустым. Пожалуйста, введите своё имя.")

print(f"Привет, {user_name}!")

while True:
    age = input("Сколько вам лет? ").strip()
    try:
        user_age = int(age)
        if 0 <= user_age <= 100:
            break
        else:
            print("Пожалуйста, укажите возраст от 0 до 100 лет.")
    except ValueError:
        print("Возраст должен быть целым числом. Попробуйте ещё раз.")


# 2. Сбор данных
body_weight = "Укажите свой вес в кг.(используйте точку): "
growth_curve = "Введите рост в метрах, используя точку: "

while True:
    weight = input(body_weight)
    try:
        user_weight = float(weight)
        if 5 <= user_weight <= 200:
            break
        else:
            print("Пожалуйста укажите вес от 5 до 200 кг.")
    except ValueError:
        print("Вес должен быть числом. Например 45.6 или 76")
while True:
    height = input(growth_curve)
    try:
        user_height = float(height)
        if 0.5 <= user_height <= 2.5:
            break
        else:
            print("Пожалуйста укажите рост от 0.5 до 2.5 м.")
    except ValueError:
        print("Рост должен быть числом. Например 1.3 или 2")


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
water_per_kg = 30
in_liter = 1000
bmi = user_weight / (user_height ** 2)  # Расчет индекса массы тела


# Подсчет воды: вес * 30 мл
# Расчет нормы воды в день в милилитрах
water_ml = user_weight * water_per_kg
# Перевод нормы воды в день из милилитров в литры
water_l = water_ml / in_liter


# 4. Вывод красивого результата
# Логика вывода нужного слова "год", "лет", "года"
last_digit_age = user_age % 10
last_two_age = user_age % 100

if 11 <= last_two_age <= 19:
    age_word = "лет"
elif last_digit_age == 1:
    age_word = "год"
elif 2 <= last_digit_age <= 4:
    age_word = "года"
else:
    age_word = "лет"

print(f"Отчет для пользователя: {user_name} {user_age} {age_word}")
print(f"Твой Индекс Массы Тела: {round(bmi, 1)}")

# Логика вывода нужного слова "литр" "литра" "литров"
# Проверяем есть ли у числа дробная часть
fractional_part = (water_l % 1) != 0
water = int(water_l)
last_digit_water = (water) % 10
last_two_water = (water) % 100


if fractional_part:
    water_word = "литра"
elif 11 <= last_two_water <= 19:
    water_word = "литров"
elif last_digit_water == 1:
    water_word = "литр"
elif 2 <= last_digit_water <= 4:
    water_word = "литра"
else:
    water_word = "литров"
print(f"Рекомендуемая норма воды: {round(water_l, 1)} {water_word} в день")

print("Расчет окончен. Будьте здоровы!")
