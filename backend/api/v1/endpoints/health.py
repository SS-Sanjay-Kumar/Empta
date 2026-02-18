from fastapi import APIRouter

healthRouter = APIRouter()

@healthRouter.get("/")
def check_health():
    return {"status":"ok"}