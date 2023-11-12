from gymhero.database.base_class import Base
from sqlalchemy import Integer, Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

training_unit_exercise = Table(
    "training_unit_exercise",
    Base.metadata,
    Column("training_unit_id", ForeignKey("training_units.id"), primary_key=True),
    Column("exercise_id", ForeignKey("exercises.id"), primary_key=True),
)


class TrainingUnit(Base):
    __tablename__ = "training_units"

    id = Column(Integer, primary_key=True)
    key = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    exercises = relationship("Exercise", secondary=training_unit_exercise)
