from flask import Flask, render_template, request, redirect, url_for
from PIL import Image



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        corta(uploaded_file)
    return redirect(url_for('index'))




def corta(fn):
    im = Image.open(fn)
    upper = 150
    lower = 305
    for i in range(10):
        im.crop(box=(5, upper, 600, lower)).save(f'lado1_{i}.jpg')
        im.crop(box=(605, upper, 1200, lower)).save(f'lado2_{i}.jpg')
        upper += 150
        lower += 150



if __name__ == '__main__':
    app.run()