from typing import List

from ..models.job import JobTextView, Job

class JobRepository:
    def __init__(self):
        pass

    async def get_job(self, job_id: int) -> Job:
        job = await Job.find(Job.job_id == job_id).sort("-update_date").project(JobTextView).first_or_none()
        return job

