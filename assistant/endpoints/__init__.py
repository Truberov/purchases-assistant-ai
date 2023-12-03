from assistant.endpoints.health_check import api_router as health_check_router
from assistant.endpoints.qa import api_router as qa_router

list_of_routes = [
    health_check_router,
    qa_router,
]

__all__ = [
    "list_of_routes",
]
