from PIL import Image, ImageDraw, ImageFont

print('Генератор мемов запущен!')

text_type = input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: ")

top_text = ''
bottom_text = ''

if text_type == '1':
    bottom_text = input('Введите нижний текст: ')
elif text_type == '2':
    top_text = input('Введите верхний текст: ')
    bottom_text = input('Введите нижний текст: ')
else:
    print('Введен неправильный режим. Перезапустите программу.')
    quit()

print(top_text, bottom_text)


memes = ['cat_at_restaurant.png', 'cat_with_glasses.png', 'trollface.jpg']

print('Выберите картинку для мема: ')

for i in range(len(memes)):
    print(i, memes[i])

image = Image.open('images/' + memes[int(input('Введите номер картинки: '))])


width, height = image.size

draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=70)

top_text_sizes = draw.textbbox((0, 0), top_text, font)
bottom_text_sizes = draw.textbbox((0, 0), bottom_text, font)

draw.text(((width - top_text_sizes[2]) / 2, 10), top_text, font=font, fill='black')
draw.text(
    ((width - bottom_text_sizes[2]) / 2, (height - bottom_text_sizes[3] - 10)),
    bottom_text, font=font, fill='black'
)

image.save('new_meme.jpg')