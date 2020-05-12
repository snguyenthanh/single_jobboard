from starlette.routing import Mount, Route

# from single_jobboard.views.root import root
from single_jobboard.views.job import routes as job_routes


routes = [
    # Route("/", root),
    Mount("/jobs", routes=job_routes),
]
