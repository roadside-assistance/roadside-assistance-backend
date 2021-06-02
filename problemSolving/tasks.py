from celery import shared_task


@shared_task
def notify_expert(problem_id: int):
    pass