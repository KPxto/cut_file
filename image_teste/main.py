from PIL import Image


im = Image.open('cte.jpg')


upper = 150
lower = 305

for i in range(10):
    im.crop(box=(5, upper, 600, lower)).save(f'lado1_{i}.jpg')
    im.crop(box=(605, upper, 1200, lower)).save(f'lado2_{i}.jpg')
    upper += 150
    lower += 150