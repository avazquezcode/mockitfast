import json
import time

from domain.model import Response
from utils.templating import replace_variables_in_str, replace_variables_in_dict

from fastapi import Response as FastAPIResponse
from fastapi import Request


class Handler:
    def __init__(self, response_config: Response):
        self.data = response_config

    def response(self, request: Request):
        if self.data.delay is not None:
            time.sleep(self.data.delay)

        body = self.transform_body(self.data.body, request)
        return FastAPIResponse(body, self.data.status, self.data.headers)

    def transform_body(self, body, request: Request):
        if type(body) is dict:
            body = replace_variables_in_dict(request.path_params, body)
            body = json.dumps(body)
        else:
            body = replace_variables_in_str(request.path_params, body)
        return body
