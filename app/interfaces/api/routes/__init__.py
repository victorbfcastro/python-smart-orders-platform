from fastapi import APIRouter
from .healthcheck import router as health_router
# from .customers import router as customer_router (mais tarde)

router = APIRouter()
router.include_router(health_router)
# router.include_router(customer_router, prefix="/customers")
