from fastapi import FastAPI

from app.database import Base, engine

from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.bots import router as bots_router

try:
    from app.api.payments import router as payments_router
except Exception:
    payments_router = None

try:
    from app.api.admin import router as admin_router
except Exception:
    admin_router = None

try:
    from app.api.subscriptions import router as subscriptions_router
except Exception:
    subscriptions_router = None

# Telegram webhook router
try:
    from app.api.telegram_webhook import router as telegram_router
except Exception:
    telegram_router = None


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Telegram Bot Builder",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


@app.get("/")
async def root():
    return {
        "success": True,
        "message": "Telegram Bot Builder API",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    return {
        "success": True,
        "status": "online"
    }


# Include routers
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(bots_router)

if payments_router:
    app.include_router(payments_router)

if admin_router:
    app.include_router(admin_router)

if subscriptions_router:
    app.include_router(subscriptions_router)

if telegram_router:
    app.include_router(telegram_router)


@app.on_event("startup")
async def startup_event():
    print("===================================")
    print("Telegram Bot Builder Started")
    print("===================================")


@app.on_event("shutdown")
async def shutdown_event():
    print("===================================")
    print("Telegram Bot Builder Stopped")
    print("===================================")
