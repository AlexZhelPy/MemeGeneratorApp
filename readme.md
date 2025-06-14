# 🎨 Meme Generator App

Приложение для быстрой генерации мемов с возможностью редактирования текста и настройки размера шрифта.

## 📌 О проекте
Этот проект представляет собой простую веб-платформу для создания мемов на основе заранее подготовленных изображений. Вы можете добавлять собственный текст вверху и внизу изображения, настраивать размер шрифта и мгновенно получать готовое изображение.

## ⚙️ Требования
Перед началом работы убедитесь, что у вас установлены необходимые инструменты и зависимости:

- Python >= 3.6
- Библиотека Pillow для работы с изображениями
- Flask для веб-интерфейса

Установите нужные пакеты с помощью команды:

````
pip install flask pillow
````

## 💾 Установка и настройка
Склонируйте репозиторий и установите зависимости:

````
git clone https://github.com/AlexZhelPy/MemeGeneratorApp.git
cd meme-generator
pip install -r requirements.txt
````
Создайте структуру папок и разместите в них ресурсы:

* Папка images — хранит исходные изображения-шаблоны (например, template.jpg).
* Папка static — включает таблицы стилей (style.css) и шрифты (fonts/Arial.ttf).
* Скопируйте нужные файлы в указанные места.
## 🚀 Запуск приложения
Запустите приложение локально:

````
python main.py
````
Посмотрите результат в браузере по адресу: http://127.0.0.1:5000/.

## 🖋️ Инструкция по использованию
+ Зайдите на главную страницу приложения.
+ Введите текст для верхней части мема ("верхний текст").
+ Введите текст для нижней части мема ("нижний текст").
+ Выберите размер шрифта, двигая ползунок или вводя число вручную.
+ Нажмите кнопку "Создать мем".

Готовое изображение появится на экране.
### 🤷 Возможные ошибки и их решение
- Нет доступа к ресурсам: убедитесь, что все необходимые файлы (изображение, шрифт) находятся в нужных местах.
- Проблемы с размером шрифта: проверьте, что шрифт доступен и путь к нему указан верно.
