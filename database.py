from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from models import NamesMan, NamesWoman
from parser import Parser


class DbWorker:
    """Класс для работы с базой данных"""
    def __init__(self, session: Session) -> None:
        self.session = session

    def names_to_db(self, table, tag: str) -> None:
        """Функция для добавления записей в таблицу"""
        names = Parser.get_names(tag)
        self.session.add_all(table(title=name) for name in names)
        self.session.commit()

    def find_name(self, name: str) -> str | None:
        """Функция для поиска имен в базе данных, возвращает пол"""
        try:
            query = select(NamesMan).where(NamesMan.title == name)
            self.session.execute(query).one()
            res = "male"
        except NoResultFound:
            try:
                query = select(NamesWoman).where(NamesWoman.title == name)
                self.session.execute(query).one()
                res = "female"
            except NoResultFound:
                res = None
        return res
