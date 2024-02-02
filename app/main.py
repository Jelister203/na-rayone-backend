from fastapi import FastAPI
import gunicorn

from .api import routers


app = FastAPI()
app.include_router(routers.router)

if __name__ == "__main__":
    gunicorn.run(app=app)
