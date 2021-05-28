from .celery import app as celery_app

__all__ = ('celery_app',)  # do we really need it? it's already public! 🤔
