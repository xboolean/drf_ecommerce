from celery import shared_task
from .utils import send_email
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task(name='sent_activation_email')
def send_email_task(data):
    logger.info("Sent activation link!")
    return send_email(data)

