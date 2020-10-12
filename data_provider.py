import json


def get_teacher(id):
    with open("teachers.json", "r") as f:
        teachers = json.load(f)
    for t in teachers:
        if t['id'] == id:
            return t
    return None


def get_goal(key):
    with open("goals.json", "r") as f:
        goals = json.load(f)
    for k, v in goals.items():
        if k == key:
            return v
    return None


def whole_week():
    return {
        "mon": "Понедельник",
        "tue": "Вторник",
        "wed": "Среда",
        "thu": "Четверг",
        "fri": "Пятница",
        "sat": "Суббота",
        "sun": "Воскресенье"
    }


print(get_goal('relocate'))
