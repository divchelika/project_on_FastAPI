from sqlalchemy import Column, Integer, VARCHAR
from database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(225))
    platform = Column(VARCHAR(225))
    date_released = Column(VARCHAR(225))
