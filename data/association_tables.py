import sqlalchemy

from .db_session import SqlAlchemyBase

association_table_1 = sqlalchemy.Table(
    "tasks_to_groups_completed",
    SqlAlchemyBase.metadata,
    sqlalchemy.Column("task", sqlalchemy.Integer, sqlalchemy.ForeignKey("tasks.id")),
    sqlalchemy.Column("group", sqlalchemy.Integer, sqlalchemy.ForeignKey("groups.id")))

association_table_2 = sqlalchemy.Table(
    "tasks_to_users_completed",
    SqlAlchemyBase.metadata,
    sqlalchemy.Column("task", sqlalchemy.Integer, sqlalchemy.ForeignKey("tasks.id")),
    sqlalchemy.Column("user", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")))

association_table_3 = sqlalchemy.Table(
    "tasks_to_groups_in_process",
    SqlAlchemyBase.metadata,
    sqlalchemy.Column("task", sqlalchemy.Integer, sqlalchemy.ForeignKey("tasks.id")),
    sqlalchemy.Column("group", sqlalchemy.Integer, sqlalchemy.ForeignKey("groups.id")))

association_table_4 = sqlalchemy.Table(
    "tasks_to_users_in_process",
    SqlAlchemyBase.metadata,
    sqlalchemy.Column("task", sqlalchemy.Integer, sqlalchemy.ForeignKey("tasks.id")),
    sqlalchemy.Column("user", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")))

association_table_5 = sqlalchemy.Table(
    "tasks_to_groups_undone",
    SqlAlchemyBase.metadata,
    sqlalchemy.Column("task", sqlalchemy.Integer, sqlalchemy.ForeignKey("tasks.id")),
    sqlalchemy.Column("group", sqlalchemy.Integer, sqlalchemy.ForeignKey("groups.id")))

association_table_6 = sqlalchemy.Table(
    "tasks_to_users_undone",
    SqlAlchemyBase.metadata,
    sqlalchemy.Column("task", sqlalchemy.Integer, sqlalchemy.ForeignKey("tasks.id")),
    sqlalchemy.Column("user", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")))