from fastapi import APIRouter

router = APIRouter(
    prefix="/subscriptions",
    tags=["Subscriptions"]
)


@router.get("/plans")
def plans():
    return {
        "plans": [
            {
                "name": "1 Day",
                "price": 10
            },
            {
                "name": "7 Days",
                "price": 30
            },
            {
                "name": "28 Days",
                "price": 50
            },
            {
                "name": "84 Days",
                "price": 100
            },
            {
                "name": "168 Days",
                "price": 150
            },
            {
                "name": "365 Days",
                "price": 250
            },
            {
                "name": "Permanent",
                "price": 499
            }
        ]
    }