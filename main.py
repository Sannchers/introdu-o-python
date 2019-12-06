import os
from PIL import Image, ImageDraw, ImageFont

font_type = "fonts/unicode.impact.ttf"

def _save_meme_handler():
  count = 0

  def _wrapper(image):
    nonlocal count
    new_image_path = f"/tmp/meme-version-{count}" + get_extension(image.filename)
    image.save(new_image_path)
    count += 1
    return new_image_path

  return _wrapper


meme_saver = _save_meme_handler()



def generate_meme(base_image, text):
  # Calculamos a font de forma dinâmica
  font_size = calculate_font_size(base_image.size, text)
  font = ImageFont.truetype(font_type, font_size)

  image_draw = ImageDraw.Draw(base_image)
  # Calculamos a posição do texto de forma dinâmica
  text_position = calculate_text_position(font.getsize(text), base_image.size)
  image_draw.text(text_position, text.upper(), font=font)

  new_image_path = meme_saver(base_image)
  return new_image_path

def _save_meme_handler():
  count = 0

  def _wrapper(image):
    nonlocal count
    new_image_path = f"/tmp/meme-version-{count}" + get_extension(image.filename)
    image.save(new_image_path)
    count += 1
    return new_image_path

  return _wrapper

def get_extension(filename):
  return os.path.splitext(filename)[-1]

def calculate_font_size(image_size, text):
  image_width, image_height = image_size

  # O texto não deve ocupar mais que 80% da largura da imagem
  # Dessa forma conseguimos ter um espaço de 10% em cada lateral
  text_container = image_width * 0.8

  current_font_size = 10
  text_width = 0

  while (text_container - text_width) > text_container * 0.05:
    font = ImageFont.truetype(font_type, current_font_size)
    text_width, _ = font.getsize(text)

    # Incremento o tamanho da font em 10% a cada iteração do loop
    current_font_size += int(current_font_size * 0.1)
  
  return current_font_size

def calculate_text_position(text_size, image_size):
  image_width, image_height = image_size
  text_width, text_height = text_size
  
  width = (image_width - text_width) // 2

  # Pra gerar uma margem de espaço na parte de baixo 
  # diminuimos o tamanho total em 2%
  image_height -= image_height * 0.02
  height = (image_height - text_height)

  return (width, height)

base_image_path = "/home/ubuntu/Downloads/pg.jpg"
image = Image.open(base_image_path)
#generate_meme(image, "T")
image.show()



