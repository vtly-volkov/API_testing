import logging
from typing import Optional, Dict, Any, Union

import requests

from api.endpoints import Endpoints
from settings import get_settings

settings = get_settings()
logging.basicConfig(level=logging.INFO)


class BaseSession:
    def __init__(self):
        self.base_url = settings.API_URL

    @staticmethod
    def get(
        endpoint: Union[Endpoints, str],
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ):
        """
        :param endpoint: The API endpoint to which the GET request will be made.
                         Can be an instance of the Endpoints class or a string.
        :param params: Optional dictionary of URL parameters to append to the request.
                       Defaults to None.
        :param headers: Optional dictionary of HTTP headers to send with the request.
                        Defaults to None.
        :return: The HTTP response received from the endpoint.
        """
        url = endpoint.url if isinstance(endpoint, Endpoints) else endpoint
        if headers is None:
            headers = {}
        resp = requests.get(url, params=params, headers=headers, verify=False)
        if resp.status_code == 401 and resp.json().get("code") == 1114:
            resp = requests.get(url, params=params, headers=headers, verify=False)

        return resp

