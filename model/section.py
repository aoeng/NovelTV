import json

from sqlalchemy import create_engine, Column, Integer, String, Text, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship

from model.model import Model
from model.novel import Novel


class Section(Model):
    __tablename__ = 'sections'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    novel_id: Mapped[int] = mapped_column(ForeignKey("novels.id"))
    content: Mapped[str] = mapped_column(Text(), nullable=True)
    status: Mapped[int] = mapped_column(Integer, default=0)
    sort: Mapped[int] = mapped_column(Integer, default=0)

    novel: Mapped["Novel"] = relationship(back_populates="sections")
