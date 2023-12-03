from enum import Enum


class TripStatus(str, Enum):
    NEW = "NEW"
    CANCELED = "CANCELED"
    FINISHED = "FINISHED"
    IN_PROGRESS = "IN_PROGRESS"
    NEED_APPROVE = "NEED_APPROVE"
    APPROVED = "APPROVED"


class TicketClass(str, Enum):
    W = "W"
    L = "L"


class RoomCategory(str, Enum):
    STANDARD = "STANDARD"
    LUX = "LUX"
