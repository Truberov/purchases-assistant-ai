from sqlalchemy import Column, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP

from .base import BaseTable


class Trip(BaseTable):
    __tablename__ = "trip"

    client_id = Column(
        "client_id",
        UUID(as_uuid=True),
        nullable=False,
        doc="id of client",
    )
    start_datetime = Column(
        "start_datetime",
        TIMESTAMP(timezone=True),
        nullable=True,
        doc="trip datetime start"
    )
    end_date = Column(
        "end_datetime",
        TIMESTAMP(timezone=True),
        nullable=True,
        doc="trip datetime end"
    )
