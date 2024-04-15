import sqlalchemy

from .db_session import SqlAlchemyBase


class Kinds(SqlAlchemyBase):
    __tablename__ = 'kinds'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)