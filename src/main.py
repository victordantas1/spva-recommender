import asyncio

from odmantic import AIOEngine

from models.candidate import Candidate



async def main():
    engine = AIOEngine(database='spva')
    candidate = await engine.find(Candidate, Candidate.user_id == 3)
    print(candidate)

if __name__ == "__main__":
    asyncio.run(main())