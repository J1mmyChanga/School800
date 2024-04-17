from datetime import date
from data import db_session
from data.tasks import Tasks
from data.users import Users
from data.groups import Groups
from data.kinds import Kinds
from data.association_tables import *

db_session.global_init('db/school800.db')
session = db_session.create_session()

g1 = Groups(title='Нео', rating=44)
g2 = Groups(title='Класт', rating=68)
g3 = Groups(title='Трейл', rating=23)
g4 = Groups(title='Скрипт', rating=68)
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

u1 = Users(email='artemkrot@gmail.com', first_name='Артем', second_name='Жуков', surname='Геннадьевич', rating=337, grade='11.4', group=1, hashed_password='1234')
u2 = Users(email='kostyakrot@gmail.com', first_name='Костя', second_name='Дробязкин', surname='Алексеевич', rating=228, grade='11.2', group=4, hashed_password='124')
u3 = Users(email='yashakrot@gmail.com', first_name='Яков', second_name='Мартыненков', surname='Юрьевич', rating=404, grade='11.1', group=2, hashed_password='125554')
u4 = Users(email='aboba@gmail.com', first_name='Владислав', second_name='Ковалев', surname='Батькович', rating=34, grade='11.5', group=3, hashed_password='125554')
for i in range(1, 5):
    session.add(eval(f'u{i}'))

t1 = Tasks(task='Полить цветы на школьной территории',
           completed=False, status=True, kind=7, daily=True, difficulty=1, individual=True, start=date(year=2024, month=3, day=1), end=date(year=2024, month=3, day=2))
t2 = Tasks(task='Подмести и вымыть пол на школьной площадке',
           completed=False, status=True, kind=7, daily=False, difficulty=2, individual=False, start=date(year=2024, month=3, day=7), end=date(year=2024, month=3, day=14))
t3 = Tasks(task='Исследовать и написать отчёт о лучших растений для обустройства школы',
           completed=False, status=True, kind=2, daily=False, difficulty=3, individual=True, start=date(year=2024, month=3, day=1), end=date(year=2024, month=3, day=15))
t4 = Tasks(task='Провести уборку столовой после завтрака',
           completed=False, status=True, kind=7, daily=True, difficulty=2, individual=True, start=date(year=2024, month=3, day=8), end=date(year=2024, month=3, day=9))
t5 = Tasks(task='Подготовить и провести урок в рамках школьного кружка или клуба',
           completed=False, status=True, kind=2, daily=False, difficulty=3, individual=True, start=date(year=2024, month=5, day=9), end=date(year=2024, month=5, day=23))
t6 = Tasks(task='Организовать и провести спортивный турнир по воллейболу среди учеников',
           completed=False, status=True, kind=1, daily=False, difficulty=2, individual=False, start=date(year=2024, month=4, day=1), end=date(year=2024, month=4, day=30))
t7 = Tasks(task='Посадить дерево на территории школы',
           completed=False, status=True, kind=4, daily=True, difficulty=3, individual=True, start=date(year=2024, month=4, day=1), end=date(year=2024, month=4, day=2))
t8 = Tasks(task='Помочь учителю подготовить материалы для урока',
           completed=False, status=True, kind=2, daily=True, difficulty=2, individual=True, start=date(year=2024, month=3, day=1), end=date(year=2024, month=3, day=2))
t9 = Tasks(task='Провести анализ и предложить меры по экономии энергии в школьном здании',
           completed=False, status=True, kind=2, daily=False, difficulty=3, individual=False, start=date(year=2024, month=2, day=1), end=date(year=2024, month=2, day=23))
t10 = Tasks(task='Исследовать вред куренияи и представить работу на школьной конференции',
           completed=False, status=True, kind=2, daily=False, difficulty=3, individual=False, start=date(year=2024, month=1, day=1), end=date(year=2024, month=1, day=30))

t11 = Tasks(task='Помочь в организации и проведении школьного праздника',
           completed=False, status=False, kind=5, daily=True, difficulty=2, individual=True, start=date(year=2024, month=4, day=1), end=date(year=2024, month=4, day=2))
t12 = Tasks(task='Помочь ученику с домашним заданием или подготовкой к контрольной работе',
           completed=False, status=False, kind=5, daily=False, difficulty=1, individual=True, start=date(year=2024, month=3, day=7), end=date(year=2024, month=3, day=14))
t13 = Tasks(task='Провести мастер-класс по изучаемому предмету для младших школьников',
           completed=False, status=False, kind=6, daily=False, difficulty=2, individual=True, start=date(year=2024, month=2, day=1), end=date(year=2024, month=2, day=20))
t14 = Tasks(task='Организовать сбор вторсырья для переработки на благотворительный фонд',
           completed=False, status=False, kind=4, daily=False, difficulty=2, individual=False, start=date(year=2024, month=3, day=8), end=date(year=2024, month=3, day=25))
t15 = Tasks(task='Помочь ученику с трудностями в обучении',
           completed=False, status=False, kind=5, daily=True, difficulty=2, individual=True, start=date(year=2024, month=5, day=9), end=date(year=2024, month=5, day=10))
t16 = Tasks(task='Провести исследование и подготовить презентацию о влиянии социальных сетей',
           completed=False, status=False, kind=2, daily=False, difficulty=3, individual=False, start=date(year=2024, month=4, day=1), end=date(year=2024, month=4, day=30))
t17 = Tasks(task='Принять участие в экологической акции по уборке мусора на улицах района',
           completed=False, status=False, kind=4, daily=False, difficulty=2, individual=False, start=date(year=2024, month=4, day=1), end=date(year=2024, month=4, day=15))
t18 = Tasks(task='Помочь библиотекарю организовать книжный уголок в классе',
           completed=False, status=False, kind=2, daily=False, difficulty=1, individual=True, start=date(year=2024, month=3, day=1), end=date(year=2024, month=3, day=7))
t19 = Tasks(task='Участвовать в работе школьного интернет-журнала: писать статьи, делиться новостями',
           completed=False, status=False, kind=2, daily=False, difficulty=3, individual=False, start=date(year=2024, month=2, day=1), end=date(year=2024, month=4, day=2))
t20 = Tasks(task='Провести анкетирование по теме предпочтений в образовательном процессе',
           completed=False, status=False, kind=2, daily=False, difficulty=3, individual=False, start=date(year=2024, month=1, day=8), end=date(year=2024, month=1, day=16))

for i in range(1, 21):
    session.add(eval(f't{i}'))

t4.status=True
t5.status=True
t6.status=True
u3.tasks_in_process.append(t4)
u3.tasks_in_process.append(t5)
u3.tasks_in_process.append(t6)

u3.tasks_undone.append(t1)
u3.tasks_undone.append(t2)
u3.tasks_undone.append(t3)

t7.completed=True
t8.completed=True
t9.completed=True
u3.tasks_completed.append(t7)
u3.tasks_completed.append(t8)
u3.tasks_completed.append(t9)
session.commit()