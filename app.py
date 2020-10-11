from flask import Flask

app = Flask(__name__)


@app.route('/')
def render_main():
    return 'Здесь будет главная'


@app.route('/goals/<goal>/')
def render_doals(goal):
    return 'Здесь будет цель ' + goal


@app.route('/profiles/<teacher_id>/')
def render_profiles(teacher_id):
    return 'Здесь будет преподаватель ' + teacher_id


@app.route('/request/')
def render_request():
    return 'Здесь будет заявка на подбор'


@app.route('/request_done/')
def render_request_done():
    return 'Заявка на подбор отправлена'


@app.route('/booking/<teacher_id>/<day_of_the_week>/<time>/')
def render_booking(teacher_id, day_of_the_week, time):
    return 'здесь будет форма бронирования ' + teacher_id


@app.route('/booking_done/')
def render_booking_done():
    return 'заявка отправлена'


if __name__ == '__main__':
    app.run()
