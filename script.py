import os
import json

# Функція для завантаження конфігурації з файлу
def load_config(filename='config.json'):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {}

# Перевірка наявності файлу конфігурації
config = load_config()

# Якщо файл існує і містить параметри, використовуємо їх, інакше запитуємо в користувача
if config:
    print("Конфігурація завантажена з файлу.\n")
else:
    print("Конфігураційний файл не знайдено, будуть використовуватись значення за замовчуванням.\n")

# Запит на кількість кнопок, якщо не задано в конфігурації
num_buttons = config.get('num_buttons')
if not num_buttons:
    num_buttons = int(input("Введіть кількість кнопок у боковому меню: "))
else:
    print(f"Кількість кнопок задана в файлі: {num_buttons}")

# Запит на назви кнопок, якщо не задано в конфігурації
button_names = config.get('button_names')
if not button_names:
    button_names = []
    for i in range(num_buttons):
        name = input(f"Введіть назву для кнопки {i + 1}: ")
        button_names.append(name)
else:
    print(f"Назви кнопок задані в файлі: {', '.join(button_names)}")

# Запит на тип контенту для кожної кнопки, якщо не задано в конфігурації
content_types = config.get('content_types')
if not content_types:
    content_types = []
    for i in range(num_buttons):
        content_type = int(input("Виберіть тип контенту для кнопки (1 - текст, 2 - зображення): "))
        while content_type not in [1, 2]:
            content_type = int(input("Некоректний вибір. Будь ласка, введіть '1' для тексту або '2' для зображення: "))
        content_types.append(content_type)
else:
    print(f"Типи контенту для кнопок задані в файлі: {', '.join(map(str, content_types))}")

# Запит на посилання для лабораторних робіт, якщо не задано в конфігурації
lab_links = config.get('lab_links')
if not lab_links:
    lab_links = []
    for i in range(9):
        link = input(f"Введіть посилання для лабораторної роботи №{i + 1}: ")
        lab_links.append(link)
else:
    print(f"Посилання на лабораторні роботи задані в файлі.")

# Запит на групу та ПІБ, якщо не задано в конфігурації
group_name = config.get('group_name')
if not group_name:
    group_name = input("Введіть назву групи: ")
else:
    print(f"Назва групи задана в файлі: {group_name}")

full_name = config.get('full_name')
if not full_name:
    full_name = input("Введіть ПІБ: ")
else:
    print(f"ПІБ задано в файлі: {full_name}")

# Запит на стать, якщо не задано в конфігурації
gender = config.get('gender')
if not gender:
    gender = input("Введіть стать студента (ч/ж): ").strip().lower()
    while gender not in ['ч', 'ж']:
        gender = input("Некоректний вибір. Будь ласка, введіть 'ч' для студента або 'ж' для студентки: ").strip().lower()
else:
    print(f"Стать студента задана в файлі: {gender}")

# Шаблон для HTML-сторінок
html_template = '''
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>ЗВІТИ З ЛАБОРАТОРНИХ РОБІТ</h1>
            <h2>З ДИСЦИПЛІНИ «ІНТЕРНЕТ-ТЕХНОЛОГІЇ та ПРОЄКТУВАННЯ ВЕБ-ЗАСТОСУВАНЬ»</h2>
            <p>
                {student_info} <!-- Добавлено поле для информации о студенте -->
            </p>
        </header>
        
        <div class="menu">
            {lab_buttons}
        </div>
        
        <div class="main">
            <div class="sidebar">
                {sidebar_links}
            </div>
            <div class="content">
                <div class="info-or-image-box">
                    {content}
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''

# Створення сторінок
for i in range(num_buttons):
    title = f'Сторінка {i + 1}: {button_names[i]}' if button_names else f'Сторінка {i + 1}'
    
    # Генерація кнопок для верхнього блоку
    lab_buttons = ''.join(
        f'<a href="{lab_links[j]}" class="lab-button">Лабораторна робота №{j + 1}</a>' for j in range(len(lab_links))
    )

    # Генерація посилань для бокового меню
    # Генерація посилань для бокового меню
    sidebar_links = ''.join(
    	f'<a href="page_{j + 1}.html" class="sidebar-button">{button_names[j]}</a>' if j > 0 else f'<a href="index.html" class="sidebar-button">{button_names[j]}</a>'
    	for j in range(num_buttons)
    )


    # Формування інформації про студента
    if gender == 'ч':
        student_info = f"Виконав студент групи {group_name} {full_name}"
    else:
        student_info = f"Виконала студентка групи {group_name} {full_name}"

    # Контент сторінки (текст або зображення)
    if content_types[i] == 1:  # Текстова сторінка
        content = f'''
            <div class="info-box">
                <h3>Місце виведення інформації для {button_names[i]}</h3>
                <p>Це поле призначене для відображення статичного контенту, який не можна редагувати.</p>
                <p>Приклад тексту з <a href="#">посиланням</a> на зовнішній ресурс.</p>
            </div>
        '''
    else:  # Сторінка з зображенням
        content = '''
            <div class="image-box">
                <img src="example-image.png" alt="Приклад зображення" class="responsive-image">
            </div>
        '''

    # Заповнення шаблону
    page_content = html_template.format(
        title=title,
        lab_buttons=lab_buttons,
        sidebar_links=sidebar_links,
        content=content,
        student_info=student_info  # Передача інформації про студента в шаблон
    )

    # Ім'я файлу: перша сторінка — index.html, інші — page_2.html, page_3.html і т.д.
    file_name = 'index.html' if i == 0 else f'page_{i + 1}.html'

    # Збереження сторінки
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(page_content)

print(f'Сгенеровано {num_buttons} сторінок у кореневій папці.')
