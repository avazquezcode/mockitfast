from pydantic import BaseModel, Field
from enum import Enum
from typing import Union, Annotated, Mapping


class MethodEnum(str, Enum):
    get = 'GET'
    post = 'POST'
    put = 'PUT'
    delete = 'DELETE'


class Response(BaseModel):
    body: Union[dict, str] = None
    status: Annotated[int, Field(strict=True, gt=99, lt=600)]
    delay: int = None
    headers: Mapping[str, str] | None = None


class Endpoint(BaseModel):
    path: str
    name: str = ""
    description: str = ""
    method: MethodEnum
    response: Response


class Router(BaseModel):
    endpoints: list[Endpoint] = []
