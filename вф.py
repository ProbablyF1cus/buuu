from flask import Flask

app = Flask(__name__)
@app.route('/image_mars')
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='MARS.png')}"
            alt="здесь должна была быть картинка, но что-то пошло не так :("
                    <p> Вот она какая, красная планета <p>
                  </body>
                </html>"""
@app.route('/')
def title():
    return 'Миссия Колонизация Марса'
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"
@app.route('/promotion')
def promotion():
    return "Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!"



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')