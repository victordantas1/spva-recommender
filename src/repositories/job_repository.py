from models.job import Job


class JobRepository:
    def __init__(self, engine):
        self.engine = engine

    async def get_job(self, job_id) -> Job:
        job = await self.engine.find_one(Job, Job.job_id == job_id)
        return job

