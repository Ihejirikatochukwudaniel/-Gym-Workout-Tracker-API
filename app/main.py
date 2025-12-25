"""FastAPI application entrypoint."""
from fastapi import FastAPI

from app.api.api_v1.router import api_router
from app.db import session as db_session


def create_app() -> FastAPI:
    app = FastAPI(title="Gym Workout Tracker API", version="0.1.0")

    app.include_router(api_router, prefix="/api/v1")

    @app.on_event("startup")
    def on_startup():
        # Create DB tables in dev mode (SQLite). Production should use migrations.
        engine = db_session.engine
        from app.db.base import Base  # local import

        # Import all models so they are registered on Base.metadata
        import app.models  # noqa: F401

        Base.metadata.create_all(bind=engine)

    return app


app = create_app()
