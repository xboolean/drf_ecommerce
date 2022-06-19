from base.logger import Logger


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = Logger(
            name="middleware",
            level="DEBUG",
            format="<green>[{time}]</green><level>[{level}]</level>{message}")

    def __call__(self, request):
        response = self.get_response(request)
        log_level = "info"

        if 200 <= response.status_code < 300:
            log_level = "success"
        elif 400 <= response.status_code < 500:
            log_level = "error"
        elif 500 <= response.status_code:
            log_level = "critical"

        getattr(self.logger, log_level)(
            message="<cyan>[{method}]</cyan><level>[{status}]</level>: {path}".format(
                method=request.method,
                status=response.status_code,
                path=request.path_info,
            ))
        return response
