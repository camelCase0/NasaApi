from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.handlers import router

def get_application() -> FastAPI:
    description="""
        It is Google maps, but for International Criminal Court 🚀
        """
    application = FastAPI(
        title="Justice.eye",
        description=description,
        version="0.2.3",
        contact={
            "name": "Figma design",
            "url": "https://www.figma.com/file/JB4CQHcaj4C7fjNuCQBqWJ/Ukraine-map-etc?type=design&mode=design&t=P3PC8lDzdnppsHyt-1"
        },
    )
    application.include_router(router)
    return application

app = get_application()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)