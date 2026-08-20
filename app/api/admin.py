from fastapi import APIRouter

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/stats")
def stats():
    return {
        "success": True,
        "message": "Admin dashboard",
        "users": 0,
        "bots": 0,
        "payments": 0
    }