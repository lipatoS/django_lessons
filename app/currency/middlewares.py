from currency.models import ResponseLog


class ResponseTimeMW:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        import time
        start = time.time()
        response = self.get_response(request)
        end = time.time()
        ResponseLog.objects.create(
            path=request.path,
            statuscode=response.status_code,
            responsetime=(end - start)*1000
        )

        return response


class GclidMW:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "gclid" in request.GET:
            print(f"Эмилио это ты? {request.path}")
        response = self.get_response(request)

        return response
