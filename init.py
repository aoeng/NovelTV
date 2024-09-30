from sqlalchemy import create_engine

from model.model import Model

engine = create_engine("sqlite:///database/app.db")
base = Model

base.metadata.create_all(engine)