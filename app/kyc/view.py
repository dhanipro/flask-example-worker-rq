from flask import Blueprint, current_app

kyc = Blueprint('kyc', __name__)

@kyc.route('/<int:second>')
def worker(second):
    job = current_app.task_queue.enqueue('app.job.example', second)
    # job = queue.enqueue('app.job.example', 23)
    return 'on progress'