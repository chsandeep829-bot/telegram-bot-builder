from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Bot

router = APIRouter(
    prefix="/bots",
    tags=["Bots"]
)


@router.get("/")
def get_bots(
    db: Session = Depends(get_db)
):
    bots = db.query(Bot).all()

    return {
        "success": True,
        "count": len(bots),
        "bots": [
            {
                "id": bot.id,
                "name": bot.bot_name,
                "status": bot.status
            }
            for bot in bots
        ]
    }


@router.post("/create")
def create_bot(
    data: dict,
    db: Session = Depends(get_db)
):
    bot = Bot(
        user_id=data["user_id"],
        bot_name=data["bot_name"],
        bot_token=data["bot_token"],
        status="stopped"
    )

    db.add(bot)
    db.commit()
    db.refresh(bot)

    return {
        "success": True,
        "bot_id": bot.id
    }


@router.delete("/{bot_id}")
def delete_bot(
    bot_id: int,
    db: Session = Depends(get_db)
):
    bot = db.query(Bot).filter(
        Bot.id == bot_id
    ).first()

    if not bot:
        raise HTTPException(
            status_code=404,
            detail="Bot not found"
        )

    db.delete(bot)
    db.commit()

    return {
        "success": True
    }