# Проект FitLife - MVP версия 1.0


# 1. Знакомство
user_name = input("Как тебя зовут? ")
print("Привет!", user_name)
user_age = int(input("Сколько тебе лет? "))


# 2. Сбор данных
Body_weight = "Укажите свой вес в кг.(используйте точку): "
Growth_curve = "Введите рост в метрах, используя точку: "
user_weight = float(input(Body_weight))
user_height = float(input(Growth_curve))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
water_per_kg = 30
in_liter = 1000
bmi = user_weight / (user_height ** 2)  #Расчет индекса массы тела


# Подсчет воды: вес * 30 мл
# Расчет нормы воды в день в милилитрах
water_ml = user_weight * water_per_kg
# Перевод нормы воды в день из милилитров в литры
water_l = water_ml / in_liter


# 4. Вывод красивого результата
print(f"Отчет для пользователя: {user_name} {user_name}г.")
print(f"Твой Индекс Массы Тела: {round(bmi, 1)}")
print(f"Рекомендуемая норма воды: {round(water_l, 1)} л. в день")
print("Расчет окончен. Будьте здоровы!")
