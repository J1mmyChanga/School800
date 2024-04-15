import sqlalchemy

from .db_session import SqlAlchemyBase

association_table_1 = sqlalchemy.Table(
    "tasks_to_groups",
    SqlAlchemyBase.metadata,
    sqlalchemy.Column("task", sqlalchemy.Integer, sqlalchemy.ForeignKey("tasks.id")),
    sqlalchemy.Column("group", sqlalchemy.Integer, sqlalchemy.ForeignKey("groups.id")))

association_table_2 = sqlalchemy.Table(
    "tasks_to_users",
    SqlAlchemyBase.metadata,
    sqlalchemy.Column("task", sqlalchemy.Integer, sqlalchemy.ForeignKey("tasks.id")),
    sqlalchemy.Column("user", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.uid")))