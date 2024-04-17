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
    individual = sqlalchemy.Column(sqlalchemy.Boolean)  # групповое - false или индивидуальное - true
    kind = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('kinds.id')) #направление задания
    status = sqlalchemy.Column(sqlalchemy.Boolean) # тру - не на рассмотрении, фолс - на рассмотрении
    completed = sqlalchemy.Column(sqlalchemy.Boolean) # тру - принято, фолс - не принято
    daily = sqlalchemy.Column(sqlalchemy.Boolean) # ежедневное - true или нет - false

    users_completed = orm.relationship(
        "Users",
        secondary="tasks_to_users_completed",
        backref="tasks_completed"
    )

    groups_completed = orm.relationship(
        "Groups",
        secondary="tasks_to_groups_completed",
        backref="tasks_completed"
    )

    users_in_process = orm.relationship(
        "Users",
        secondary="tasks_to_users_in_process",
        backref="tasks_in_process"
    )

    groups_in_process = orm.relationship(
        "Groups",
        secondary="tasks_to_groups_in_process",
        backref="tasks_in_process"
    )

    users_undone = orm.relationship(
        "Users",
        secondary="tasks_to_users_undone",
        backref="tasks_undone"
    )

    groups_undone = orm.relationship(
        "Groups",
        secondary="tasks_to_groups_undone",
        backref="tasks_undone"
    )



    kinds = orm.relationship(
        "Kinds",
        backref="tasks"
    )
