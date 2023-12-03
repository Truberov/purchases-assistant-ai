from logging import getLogger

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from uvicorn import run

from assistant.config import DefaultSettings
from assistant.config.utils import get_settings
from assistant.endpoints import list_of_routes
from assistant.utils.common import get_hostname


logger = getLogger(__name__)


def bind_routes(application: FastAPI, setting: DefaultSettings) -> None:
    """
    Bind all routes to application.
    """
    for route in list_of_routes:
        application.include_router(route, prefix=setting.PATH_PREFIX)


def get_app() -> FastAPI:
    """
    Creates application and all dependable objects.
    """
    description = "Микросервиc для создания и управления командировками"

    tags_metadata = [
        {
            "name": "Assistant",
            "description": "API trips.",
        },

    ]

    application = FastAPI(
        title="Assistant Service",
        description=description,
        docs_url="/swagger",
        openapi_url="/openapi",
        version="1.0.0",
        openapi_tags=tags_metadata,
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    settings = get_settings()
    bind_routes(application, settings)
    application.state.settings = settings
    return application


app = get_app()


if __name__ == "__main__":  # pragma: no cover
    settings_for_application = get_settings()
    run(
        "assistant.__main__:app",
        host=get_hostname(settings_for_application.APP_HOST),
        port=settings_for_application.APP_PORT,
        reload=True,
        reload_dirs=["assistant"],
        log_level="debug",
    )
