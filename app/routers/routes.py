from fastapi import APIRouter
from app.api.api_bids import returnBids,returnBidByCode

router = APIRouter()

@router.get("/bids")
async def returnListBids():
    return returnBids()

@router.get("/bid/{bid_code}")
async def returnBidByCodeAPI(bid_code):
    return returnBidByCode(bid_code)
