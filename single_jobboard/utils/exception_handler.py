from starlette.responses import UJSONResponse


async def http_exception_handler(request, exc):
    return UJSONResponse({"error": exc.detail}, status_code=exc.status_code)
