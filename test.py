from datetime import date
from data import db_session
from data.tasks import Tasks
from data.users import Users
from data.groups import Groups
from data.kinds import Kinds
from data.association_tables import *

db_session.global_init('db/school800.db')
session = db_session.create_session()

g1 = Groups(title='Абобики')
g2 = Groups(title='Кроты')
g3 = Groups(title='Шпроты')
g4 = Groups(title='Раковина')
for i in range(1, 5):
    session.add(eval(f'g{i}'))

k1 = Kinds(title='Cпортивные мероприятия')
k2 = Kinds(title='Школьные мероприятия')
k3 = Kinds(title='Конкурсы/олимпиады')
k4 = Kinds(title='Волонтёрская деятельность')
k5 = Kinds(title='Наставничество')
k6 = Kinds(title='Проведение мастер-классов')
k7 = Kinds(title='Дежурство по школе')
k8 = Kinds(title='Успехи в учёбе')
for i in range(1, 9):
    session.add(eval(f'k{i}'))

u1 = Users(uid='346fEsgGSE', email='artemkrot@gmail.com', first_name='Артем', second_name='Жуков', surname='Геннадьевич', rating=337, grade='11.4', group=1, hashed_password='1234')
u2 = Users(uid='754sgdjffhdghdg4w', email='kostyakrot@gmail.com', first_name='Костя', second_name='Дробязкин', surname='Алексеевич', rating=228, grade='11.2', group=4, hashed_password='124')
u3 = Users(uid='2ipiutystsr', email='yashakrot@gmail.com', first_name='Яков', second_name='Мартыненков', surname='Юрьевич', rating=404, grade='11.1', group=2, hashed_password='125554')
for i in range(1, 4):
    session.add(eval(f'u{i}'))

t1 = Tasks(task='Полить цветы на этаже', kind=7, daily=True, difficulty=1, type=1, completed=False, start=date(year=2024, month=3, day=1), end=date(year=2024, month=3, day=2))
t2 = Tasks(task='Подмести на школьной площадке', kind=7, daily=False, difficulty=2, type=1, completed=True, start=date(year=2024, month=3, day=7), end=date(year=2024, month=3, day=10))
t3 = Tasks(task='Стать отличником в четверти', kind=8, daily=False, difficulty=3, type=1, completed=False, start=date(year=2024, month=3, day=1), end=date(year=2024, month=5, day=1))
t4 = Tasks(task='Сходить на субботник группой', kind=4, daily=False, difficulty=1, type=2, completed=True, start=date(year=2024, month=3, day=8), end=date(year=2024, month=3, day=16))
t5 = Tasks(task='Поздравить ветеранов', kind=4, daily=False, difficulty=2, type=2, completed=False, start=date(year=2024, month=5, day=9), end=date(year=2024, month=5, day=10))
t6 = Tasks(task='Собрать гуманитарную помощь на СВО', kind=4, daily=False, difficulty=3, type=2, completed=True, start=date(year=2024, month=3, day=1), end=date(year=2024, month=4, day=1))
for i in range(1, 7):
    session.add(eval(f't{i}'))

t1.groups.append(g1)
g1.tasks.append(t2)
g1.tasks.append(t4)
t1.users.append(u1)

session.commit()