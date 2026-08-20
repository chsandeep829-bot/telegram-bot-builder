import uuid
import httpx

from fastapi import APIRouter, HTTPException
from app.config import settings
from app.schemas import PaymentCreateSchema

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.post("/create")
async def create_payment(
    data: PaymentCreateSchema
):
    order_id = str(uuid.uuid4())

    payload = {
        "amount": data.amount,
        "order_id": order_id,
        "customer_name": "Telegram User",
        "redirect_url": settings.REDIRECT_URL
    }

    headers = {
        "X-API-KEY": settings.KWIKUPI_API_KEY,
        "X-API-SECRET": settings.KWIKUPI_API_SECRET,
        "Content-Type": "application/json"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://kwikupi.com/api/create-payment",
                json=payload,
                headers=headers,
                timeout=30
            )

        result = response.json()

        return {
            "success": True,
            "payment_id": result.get("payment_id"),
            "payment_url": result.get("payment_page")
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/status/{payment_id}")
async def payment_status(
    payment_id: str
):
    headers = {
        "X-API-KEY": settings.KWIKUPI_API_KEY,
        "X-API-SECRET": settings.KWIKUPI_API_SECRET
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://kwikupi.com/api/payment-status/{payment_id}",
            headers=headers
        )

    return response.json()