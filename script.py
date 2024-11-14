import os

# Задаем параметры
num_buttons = int(input("Введіть кількість кнопок у боковому меню: "))
button_names = []
content_types = []

for i in range(num_buttons):
    name = input(f"Введіть назву для кнопки {i + 1}: ")
    button_names.append(name)
    
    # Изменяем ввод типа контента на числовой
    content_type = int(input("Виберіть тип контенту для кнопки (1 - текст, 2 - зображення): "))
    while content_type not in [1, 2]:
        content_type = int(input("Некоректний вибір. Будь ласка, введіть '1' для тексту або '2' для зображення: "))
    content_types.append(content_type)

# Ввод ссылок для верхнего блока кнопок
lab_links = []
for i in range(9):
    link = input(f"Введіть посилання для лабораторної роботи №{i + 1}: ")
    lab_links.append(link)

# Ввод дополнительной информации
group_name = input("Введіть назву групи: ")
full_name = input("Введіть ПІБ: ")
gender = input("Введіть стать студента (ч/ж): ").strip().lower()
while gender not in ['ч', 'ж']:
    gender = input("Некоректний вибір. Будь ласка, введіть 'ч' для студента або 'ж' для студентки: ").strip().lower()

# Папка для хранения сгенерированных страниц
output_dir = 'generated_pages'
os.makedirs(output_dir, exist_ok=True)

# Шаблон для HTML-страниц
html_template = '''
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>ЗВІТИ З ЛАБОРАТОРНИХ РОБІТ</h1>
            <h2>З ДИСЦИПЛІНИ «ІНТЕРНЕТ-ТЕХНОЛОГІЇ та ПРОЄКТУВАННЯ ВЕБ-ЗАСТОСУВАНЬ»</h2>
            <p>
                {student_info}
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

# Создание страниц
for i in range(num_buttons):
    title = f'Сторінка {i + 1}: {button_names[i]}'
    
    # Генерация кнопок для верхнего блока
    lab_buttons = ''.join(
        f'<a href="{lab_links[j]}" class="lab-button">Лабораторна робота №{j + 1}</a>' for j in range(9)
    )

    # Генерация ссылок для бокового меню
    sidebar_links = ''.join(f'<a href="{"index.html" if j == 0 else f"page_{j + 1}.html"}" class="sidebar-button">{button_names[j]}</a>' for j in range(num_buttons))

    # Формирование информации о студенте
    if gender == 'ч':
        student_info = f"Виконав студент групи {group_name} {full_name}"
    else:
        student_info = f"Виконала студентка групи {group_name} {full_name}"

    # Контент страницы (текст или изображение)
    if content_types[i] == 1:  # Текстовая страница
        content = f'''
            <div class="info-box">
                <h3>Місце виведення інформації для {button_names[i]}</h3>
                <p>Це поле призначене для відображення статичного контенту, який не можна редагувати.</p>
                <p>Приклад тексту з <a href="#">посиланням</a> на зовнішній ресурс.</p>
            </div>
        '''
    else:  # Страница с изображением
        content = '''
            <div class="image-box">
                <img src="example-image.jpg" alt="Приклад зображення" class="responsive-image">
            </div>
        '''

    # Определение имени файла (первый файл - index.html)
    file_name = 'index.html' if i == 0 else f'page_{i + 1}.html'

    # Заполнение шаблона
    page_content = html_template.format(
        title=title,
        lab_buttons=lab_buttons,
        sidebar_links=sidebar_links,
        content=content,
        student_info=student_info
    )

    # Сохранение страницы
    with open(os.path.join(output_dir, file_name), 'w', encoding='utf-8') as f:
        f.write(page_content)

print(f'Сгенеровано {num_buttons} сторінок у папці "{output_dir}".')
