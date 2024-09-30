from typing import List

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship

from model.model import Model
from model.section import Section


class Novel(Model):
    __tablename__ = 'novels'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    file: Mapped[str] = mapped_column(String(100))
    sdcp: Mapped[str] = mapped_column(String(100))
    intro: Mapped[str] = mapped_column(String(200))
    cover: Mapped[str] = mapped_column(String(100), nullable=True)
    auto_limit: Mapped[int] = mapped_column(Integer, default=20000)

    sections: Mapped[List["Section"]] = relationship(back_populates="novel", cascade="all, delete-orphan")
