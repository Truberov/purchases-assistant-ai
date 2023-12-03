from sqlalchemy import Column, ForeignKey, text
from sqlalchemy.dialects.postgresql import TEXT, JSON

from .base import BaseTable
from .trip import Trip


class Ticket(BaseTable):
    __tablename__ = "ticket"

    trip_id = Column(
        "trip_id",
        ForeignKey("trip.id", ondelete="CASCADE", onupdate="SET NULL"),
        nullable=False,
        doc="Identifier of trip, which contains ticket",
    )
    partner = Column(
        "partner",
        TEXT,
        nullable=False,
        doc="The company that performs the flight",
    )
    from_id = Column(
        "from_id",
        TEXT,
        nullable=False,
        doc="Identifier of user, who own bookmark",
    )
    to_id = Column(
        "to_id",
        TEXT,
        nullable=False,
        doc="Identifier of tag",
    )
    forward = Column(
        "forward",
        TEXT,
        nullable=False,
        doc=""
    )
    backward = Column(
        "backward",
        TEXT,
        nullable=True,
        doc="",
    )
    ticket_class = Column(
        "ticket_class",
        TEXT,
        nullable=False,
        doc="Ticket class(L, M, W...)",
    )
    tariff = Column(
        "tariff",
        JSON,
        nullable=False,
        doc="Currency and value"
    )
