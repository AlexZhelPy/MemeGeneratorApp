import os
from PIL import Image, ImageDraw, ImageFont
from flask import Blueprint, render_template, request, send_file

bp = Blueprint('main', __name__, template_folder='templates')

@bp.route('/')
def home():
    """Главная страница"""
    return render_template('index.html')

@bp.route('/generate', methods=['POST'])
def generate_meme():
    """
    Генерирует мем на основе введённого текста и выбранного размера шрифта.
    Сохраняет итоговую картинку и отправляет её обратно браузеру.
    """
    text_top = request.form.get("top_text")
    text_bottom = request.form.get("bottom_text")
    font_size = int(request.form.get("font_size"))  # Размер шрифта, заданный пользователем
    image_path = 'images/template.jpeg'

    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Подключаем внешнюю версию шрифта с нужным размером
    font_path = os.path.join(os.path.dirname(__file__), "..", "static", "fonts", "Impact.ttf")
    font = ImageFont.truetype(font_path, size=font_size)

    def add_text(text, y):
        bbox = draw.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        x = (img.width - w) // 2
        draw.text((x, y), text, fill="white", font=font)

    if text_top:
        add_text(text_top, 10)
    if text_bottom:
        add_text(text_bottom, img.height - 100)

    # Абсолютный путь к выходной картинке
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
    output_path = os.path.join(output_dir, 'output.png')

    img.save(output_path)

    return send_file(output_path, mimetype='image/png')