from sqlalchemy import Integer, String, Text, JSON, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship

from model.model import Model
from model.novel import Novel


class Role(Model):
    __tablename__ = 'roles'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    novel_id: Mapped[int] = mapped_column(ForeignKey("novels.id"))
    name: Mapped[str] = mapped_column(String(100))
    picture: Mapped[str] = mapped_column(String(100))

    novel: Mapped["Novel"] = relationship(back_populates="roles")
