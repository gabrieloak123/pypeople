from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from pythando.schemas import Message

app = FastAPI()


@app.get(
    "/",
    status_code=HTTPStatus.OK,
    response_model=Message,
    response_class=JSONResponse,
)
def read_root():
    return {"message": "hello world"}
