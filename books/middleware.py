import logging
import time

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger('books.middleware')

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = (time.time() - start) * 1000
        logger.info(
            '%s %s user=%s status=%s time=%.0fms',
            request.method, request.path, request.user,
            response.status_code, duration,
        )
        return response