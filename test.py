from datetime import date
from data import db_session
from data.tasks import Tasks
from data.users import Users
from data.groups import Groups
from data.kinds import Kinds
from data.association_tables import *

db_session.global_init('db/school800.db')
session = db_session.create_session()

g1 = Groups(title='Инноваторы: Нео', rating=4464, image='neo.')
g2 = Groups(title='Инженеры: Класт', rating=6879, image='clast.')
g3 = Groups(title='Аналитики: Трейл', rating=2234, image='trail.')
g4 = Groups(title='Исследователи: Скрипт', rating=2868, image='script.')
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

t1 = Tasks(task='Полить цветы на школьной территории',
           kind=7, daily=True, difficulty=1, type=1, start=date(year=2024, month=3, day=1), end=date(year=2024, month=3, day=2))
t2 = Tasks(task='Подмести и вымыть пол на школьной площадке',
           kind=7, daily=False, difficulty=2, type=2, start=date(year=2024, month=3, day=7), end=date(year=2024, month=3, day=14))
t3 = Tasks(task='Провести исследование и написать отчёт о том, какие виды растений лучше всего подходят для обустройства школьного двора',
           kind=2, daily=False, difficulty=3, type=1, start=date(year=2024, month=3, day=1), end=date(year=2024, month=3, day=15))
t4 = Tasks(task='Провести уборку столовой после завтрака',
           kind=7, daily=True, difficulty=2, type=1, start=date(year=2024, month=3, day=8), end=date(year=2024, month=3, day=9))
t5 = Tasks(task='Подготовить и провести урок в рамках школьного кружка или клуба',
           kind=2, daily=False, difficulty=3, type=1, start=date(year=2024, month=5, day=9), end=date(year=2024, month=5, day=23))
t6 = Tasks(task='Организовать и провести спортивный турнир по воллейболу среди учеников',
           kind=1, daily=False, difficulty=2, type=2, start=date(year=2024, month=4, day=1), end=date(year=2024, month=4, day=30))
t7 = Tasks(task='Посадить дерево на территории школы',
           kind=4, daily=True, difficulty=3, type=1, start=date(year=2024, month=4, day=1), end=date(year=2024, month=4, day=2))
t8 = Tasks(task='Помочь учителю подготовить материалы для урока',
           kind=2, daily=True, difficulty=2, type=1, start=date(year=2024, month=3, day=1), end=date(year=2024, month=3, day=2))
t9 = Tasks(task='Провести анализ использования энергии в школьном здании и предложить меры по её экономии',
           kind=2, daily=False, difficulty=3, type=2, start=date(year=2024, month=2, day=1), end=date(year=2024, month=2, day=30))
t10 = Tasks(task='Провести исследование о вреде курения среди школьников и представить результаты на школьной конференции',
           kind=2, daily=False, difficulty=3, type=2, start=date(year=2024, month=1, day=1), end=date(year=2024, month=1, day=30))

t11 = Tasks(task='Помочь в организации и проведении школьного праздника',
           kind=5, daily=True, difficulty=2, type=1, start=date(year=2024, month=4, day=1), end=date(year=2024, month=4, day=2))
t12 = Tasks(task='Помочь ученику с домашним заданием или подготовкой к контрольной работе',
           kind=5, daily=False, difficulty=1, type=1, start=date(year=2024, month=3, day=7), end=date(year=2024, month=3, day=14))
t13 = Tasks(task='Провести мастер-класс по изучаемому предмету для младших школьников',
           kind=6, daily=False, difficulty=2, type=1, start=date(year=2024, month=2, day=1), end=date(year=2024, month=2, day=20))
t14 = Tasks(task='Организовать сбор вторсырья для переработки на благотворительный фонд',
           kind=4, daily=False, difficulty=2, type=2, start=date(year=2024, month=3, day=8), end=date(year=2024, month=3, day=25))
t15 = Tasks(task='Помочь ученику с трудностями в обучении',
           kind=5, daily=True, difficulty=2, type=1, start=date(year=2024, month=5, day=9), end=date(year=2024, month=5, day=10))
t16 = Tasks(task='Провести исследование о влиянии социальных сетей на молодежь и подготовить презентацию результатов',
           kind=2, daily=False, difficulty=3, type=2, start=date(year=2024, month=4, day=1), end=date(year=2024, month=4, day=30))
t17 = Tasks(task='Принять участие в экологической акции по уборке мусора на улицах района',
           kind=4, daily=False, difficulty=2, type=2, start=date(year=2024, month=4, day=1), end=date(year=2024, month=4, day=15))
t18 = Tasks(task='Помочь библиотекарю организовать книжный уголок в классе',
           kind=2, daily=False, difficulty=1, type=1, start=date(year=2024, month=3, day=1), end=date(year=2024, month=3, day=7))
t19 = Tasks(task='Участвовать в работе школьного интернет-журнала: писать статьи, делиться новостями',
           kind=2, daily=False, difficulty=3, type=2, start=date(year=2024, month=2, day=1), end=date(year=2024, month=4, day=2))
t20 = Tasks(task='Провести анкетирование среди учеников по теме предпочтений в образовательном процессе и анализировать полученные данные',
           kind=2, daily=False, difficulty=3, type=2, start=date(year=2024, month=1, day=8), end=date(year=2024, month=1, day=16))

for i in range(1, 21):
    session.add(eval(f't{i}'))

t1.groups.append(g1)
g1.tasks.append(t2)
g1.tasks.append(t4)
t1.users.append(u1)

session.commit()