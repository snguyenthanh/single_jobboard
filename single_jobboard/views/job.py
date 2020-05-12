from starlette.endpoints import HTTPEndpoint
from starlette.responses import UJSONResponse
from starlette.routing import Route

from single_jobboard import web_scraper


class JobRoot(HTTPEndpoint):
    # async def post(self, request):
    #     if await redis_client.exists("video_streaming"):
    #         return
    #
    #     result = record_live.delay()
    #     await redis_client.set(
    #         "video_streaming", {"id": result.task_id, "status": "running",}
    #     )
    #
    # async def delete(self, request):
    #     task = await redis_client.get("video_streaming")
    #     if not task:
    #         raise NotFound("Unable to find task")
    #
    #     task_result = AbortableAsyncResult(task["id"])
    #
    #     task_result.abort()
    #     revoke(task["id"])
    #     await redis_client.delete("video_streaming")
    #     return Response("")

    async def get(self, request):
        jobs = await web_scraper.get_jobs([])

        return UJSONResponse({"data": "hello"})


# class InspectionWithId(HTTPEndpoint):
#     @unpack_request(skip_body=True)
#     @serialize(out=RecordPublic)
#     async def get(self, request, inspection_id, **kwargs):
#         inspection_data = Record.retrieve(id=inspection_id)
#         return {
#             "data": parse_inspection_output(inspection_data),
#         }
#
#     async def delete(self, request, inspection_id, **kwargs):
#         pass


routes = [
    Route("/", JobRoot),
    # Route("/{inspection_id}", InspectionWithId),
]
