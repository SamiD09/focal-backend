import asyncio
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from focal.firebase import init_firebase, check_firestore
from focal.config import get_settings

logger=logging.getLogger(__name__)
settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_firebase()
    yield
    
app = FastAPI(title = 'Focal API', lifespan = lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.cors_origin_list,
    allow_methods = ['GET', 'PUT', 'DELETE', 'PATCH', 'POST'],
    allow_headers = ['Authorization', 'Content-Type'],
)

@app.get("/health")
async def health():
    try:
        await asyncio.wait_for(check_firestore(), timeout=15)
    except Exception:   
        logger.exception('Firestore Health Check Fail')
        return JSONResponse(status_code=503, content = {'status': 'degraded', 'firestore': 'unreachable', })
    return {'status': 'ok', 'firestore': 'reachable',}

