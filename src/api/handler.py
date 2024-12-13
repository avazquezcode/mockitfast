import json
import time

from domain.model import Response

from fastapi import Response as FastAPIResponse


class Handler:
    def __init__(self, response_config: Response):
        self.data = response_config

    def response(self):
        if self.data.delay is not None:
            time.sleep(self.data.delay)

        body = self.data.body
        if type(body) is dict:
            body = json.dumps(body)

        return FastAPIResponse(body, self.data.status, self.data.headers)
