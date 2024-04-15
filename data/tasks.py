import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Tasks(SqlAlchemyBase):
    __tablename__ = 'tasks'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    task = sqlalchemy.Column(sqlalchemy.String)  # текст задания
    start = sqlalchemy.Column(sqlalchemy.Date)  # начало задания
    end = sqlalchemy.Column(sqlalchemy.Date)  # конец задания
    difficulty = sqlalchemy.Column(sqlalchemy.Integer)  # 1 - легкое, 2 - среднее, 3 - сложное
    completed = sqlalchemy.Column(sqlalchemy.Boolean)  # выполнено - true или нет - false
    type = sqlalchemy.Column(sqlalchemy.Integer)  # групповое - 2 или индивидуальное - 1
    kind = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('kinds.id')) #направление задания
    daily = sqlalchemy.Column(sqlalchemy.Boolean) # ежедневное - true или нет - false

    users = orm.relationship(
        "Users",
        secondary="tasks_to_users",
        backref="tasks"
    )

    groups = orm.relationship(
        "Groups",
        secondary="tasks_to_groups",
        backref="tasks"
    )

    kinds = orm.relationship(
        "Kinds",
        backref="tasks"
    )
