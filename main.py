import os
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/enviroments")
async def enviroments():
    envs = dict(os.environ)
    return {"enviroments": envs}
