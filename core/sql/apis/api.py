from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from sql.apis.routes.user_manageent.user_router import user_router
from sql.apis.routes.custom.app_router import app_config_router
from sql.apis.routes.custom.cloud_router import cloud_router
from sql.apis.routes.custom.embeddings_router import embeddings_router
from sql.apis.routes.custom.chat_router import chat_router

app = FastAPI(
    title="base_template_server",
    version="0.1 - Beta",
    redoc_url="/documentation",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, tags=["Authentication"])
app.include_router(app_config_router, tags=["App Config"])
app.include_router(cloud_router, tags=["Cloud"])
app.include_router(embeddings_router, tags=["Custom"])
app.include_router(chat_router, tags=["Custom"])


@app.get("/")
def ping():
    """
    [ping func provides a health check]

    Returns:
        [dict]: [success response for the health check]
    """
    return {"response": "ping to Base Template inference server successful"}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="base_template_server",
        version="0.1 - Beta",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
