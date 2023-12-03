from sqlalchemy import Column, ForeignKey, text
from sqlalchemy.dialects.postgresql import TEXT, JSON

from .base import BaseTable


class Accommodation(BaseTable):
    __tablename__ = "accommodation"

    trip_id = Column(
        "trip_id",
        ForeignKey("trip.id", ondelete="CASCADE", onupdate="SET NULL"),
        nullable=False,
        doc="Identifier of trip, which contains ticket",
    )
    hotel = Column(
        "hotel",
        JSON,
        nullable=False,
        doc="Title of bookmark",
    )
    offers = Column(
        "link",
        JSON,
        nullable=False,
        doc="Link to resource",
    )
