import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.String,
                                     default=datetime.datetime.today().strftime("%d.%m.%Y %H:%M"))
    is_private = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    members = sqlalchemy.Column(sqlalchemy.Integer, default=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, 
                                sqlalchemy.ForeignKey("users.id"))
    payment = sqlalchemy.Column(sqlalchemy.Integer)
    user = orm.relation('User')
    categories = orm.relation("Category",
                          secondary="association",
                          backref="news")