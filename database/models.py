import atexit
from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, sessionmaker

from config import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB

PG_DSN = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)

atexit.register(engine.dispose)


class Base(DeclarativeBase):
    pass


class NamesMan(Base):
    __tablename__ = 'names_man'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False)


class NamesWoman(Base):
    __tablename__ = 'names_woman'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False)


#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
