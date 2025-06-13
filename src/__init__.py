from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.routes.user import user

from src.db.database import create_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    print("✅ App is enable...")
    yield
    print("❌ App is disable...")


def create_app():
    app = FastAPI(lifespan=lifespan)
    app.include_router(user)

    return app