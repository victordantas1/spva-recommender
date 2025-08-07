from typing import List

from beanie import init_beanie
from motor import motor_asyncio

async def init_db(documents_list: List):
 client = motor_asyncio.AsyncIOMotorClient(config["mongodb_url"])
 database = database=client.get_database()
 await init_beanie(database=database, document_models=documents_list)