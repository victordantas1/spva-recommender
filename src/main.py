import asyncio

from odmantic import AIOEngine

from models.candidate import Candidate
from models.job import Job


async def main():
    engine = AIOEngine(database='spva')
    candidate_id = 3
    job_id = 21
    candidate = await engine.find_one(Candidate, Candidate.user_id == candidate_id)
    job = await engine.find_one(Job, Job.job_id == job_id)
    print(f"Candidate {candidate_id}:\n{candidate}")
    print(f"Job {job_id}:\n{job}")

if __name__ == "__main__":
    asyncio.run(main())