from beanie import init_beanie
from motor import motor_asyncio

from src.models import Candidate, Job

async def init_db():
 client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/spva")
 database = database=client.get_database()
 await init_beanie(database=database, document_models=[Job, Candidate])