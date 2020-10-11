from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def render_main():
    return render_template('index.html')


@app.route('/goals/<goal>/')
def render_doals(goal):
    return render_template('goal.html', goal=goal)


@app.route('/profiles/<teacher_id>/')
def render_profiles(teacher_id):
    return render_template('profile.html', teacher_id=teacher_id)


@app.route('/request/')
def render_request():
    return render_template('request.html')


@app.route('/request_done/')
def render_request_done():
    return render_template('request_done.html')


@app.route('/booking/<teacher_id>/<day_of_the_week>/<time>/')
def render_booking(teacher_id, day_of_the_week, time):
    return render_template('booking.html', teacher_id=teacher_id, day_of_the_week=day_of_the_week, time=teacher_id)


@app.route('/booking_done/')
def render_booking_done():
    return render_template('booking_done.html')


if __name__ == '__main__':
    app.run()
