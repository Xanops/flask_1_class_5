from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Колонизация</title>
                            </head>
                            <body>
                                <h1 align="center">Анкета претендента</h1>
                                <h2 align="center">на участие в миссии</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <p><input type="text" class="form-control" placeholder="Введите фамилию" name="first_name">
                                        <input type="text" class="form-control" placeholder="Введите имя" name="second_name"></p>
                                        <p><input type="email" class="form-control" placeholder="Введите адрес почты" name="email" aria-describedby="emailHelp">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у Вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                                <option>Начальное</option>
                                                <option>Основное</option>
                                                <option>Среднее</option>
                                                <option>Среднее профессиональное</option>
                                                <option>Высшее</option>
                                            </select>
                                        </div></p>
                                        <p><div class="form-group ">
                                            <label for="form-check">Какие у вас есть профессии?</label>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="checkbox1" value="">
                                                <label class="form-check-label" for="checkbox1">
                                                    инженер-исследователь
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="checkbox2" value="">
                                                <label class="form-check-label" for="checkbox2">
                                                    пилот
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="checkbox3" value="">
                                                <label class="form-check-label" for="checkbox3">
                                                    строитель
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="checkbox4" value="">
                                                <label class="form-check-label" for="checkbox4">
                                                    экзобиолог
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="checkbox5" value="">
                                                <label class="form-check-label" for="checkbox5">
                                                    врач
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="checkbox6" value="">
                                                <label class="form-check-label" for="checkbox6">
                                                    инженер по терраформированию
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="checkbox7" value="">
                                                <label class="form-check-label" for="checkbox7">
                                                    климатолог
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="checkbox8" value="">
                                                <label class="form-check-label" for="checkbox8">
                                                    специалист по радиационной защите
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="checkbox9" value="">
                                                <label class="form-check-label" for="checkbox9">
                                                    астрогеолог
                                                </label>
                                            </div>
                                            <div>
                                                <input class="form-check-input" type="checkbox" id="checkbox10" value="">
                                                <label class="form-check-label" for="checkbox10">
                                                    гляциолог
                                                </label>
                                            </div>
                                        </div></p>
                                        <p><div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="sex" id="male" value="">
                                                <label class="form-check-label" for="male">
                                                    Мужской
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="sex" id="female" value="">
                                                <label class="form-check-label" for="female">
                                                    Женский
                                                </label>
                                            </div>
                                        </div></p>
                                        <p><div class="form-group">
                                            <label for="textArea">Почему вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="5" name="about"></textarea>
                                        </div></p>
                                        <p><div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control" id="photo" name="file">
                                        </div></p>
                                        <p><div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">
                                                Готовы остаться на Марсе?
                                            </label>
                                        </div></p>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                            </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['first_name'])
        print(request.form['second_name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
