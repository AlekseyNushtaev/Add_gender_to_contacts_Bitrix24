from sqlalchemy import select

from models import Session, NamesMan, NamesWoman
from parser import Parser


class DbWorker:
    """Класс для работы с базой данных"""
    def __init__(self, session: Session) -> None:
        self.session = session

    def names_to_db(self, table, tag: str) -> None:
        """Функция для добавления записей в таблицу"""
        names = Parser.get_names(tag)
        session.add_all(table(title=name) for name in names)
        session.commit()

    def find_name(self, name: str) -> str | None:
        """Функция для поиска имен в базе данных, возвращает пол"""
        query = select(NamesMan).where(NamesMan.title == name)
        man = session.scalar(query)
        query = select(NamesWoman).where(NamesWoman.title == name)
        woman = session.scalar(query)
        if man:
            res = "male"
        elif woman:
            res = "female"
        else:
            res = None
        return res


session = Session()
dbworker = DbWorker(session)
dbworker.names_to_db(NamesMan, "man")
dbworker.names_to_db(NamesWoman, "woman")
print(dbworker.find_name("Андрей"))
session.close()
