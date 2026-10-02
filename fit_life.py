# Проект FitLife - MVP версия 1.0

import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# Константы
WATER_PER_KG = 30
WATER_ONE_LITER = 1000

# Приветственное сообщение
print('Привет! Я твой фитнес-помощник FitLife. Давай познакомимся')

# Получение информации от пользователя
user_name = input('Как тебя зовут? ')
user_age = int(input('Сколько тебе полных лет? '))

# 2. Сбор данных
print(f'Что бы я стал полезным для тебя, {user_name}, '
      'мне нужно еще немного информации.')
user_weight = float(input('Какой твой вес? (в килограммах, используя точку) '))
user_height = float(input('Какой твой рост? (в метрах, используя точку) '))

# Расчет индекса массы тела
bmi = round(user_weight / (user_height ** 2), 2)

# Расчет нормы воды
water_norm = round(user_weight * WATER_PER_KG / WATER_ONE_LITER, 1)

# Вывод результатов
print(
    f'Отчет для пользователя: {user_name} ({user_age} л.)\n'
    f'Твой Индекс Массы Тела: {bmi}\n'
    f'Рекомендуемая норма воды: {water_norm} л. в день\n\n'
    'Расчет окончен. Будьте здоровы!',
)
