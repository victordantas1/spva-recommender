from ..models.job import JobTextView, Job

class JobRepository:
    def __init__(self):
        pass

    async def get_job(self, job_id: int):
        job = await Job.find_one(Job.job_id == job_id).project(JobTextView)
        return job

