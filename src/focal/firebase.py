import firebase_admin
from firebase_admin import credentials, firestore_async
from google.cloud.firestore  import AsyncClient

from focal.config import get_settings

def init_firebase() -> firebase_admin.App:
    try:
        return firebase_admin.get_app()
    except ValueError:
        pass
    
    settings = get_settings()
    cred = credentials.Certificate(settings.firebase_credentials_path)
    return firebase_admin.initialize_app(cred)

def get_firestore() -> AsyncClient:
    return firestore_async.client()

async def check_firestore() -> None:
    db = get_firestore()
    await db.collection('health').document('ping').get()
    