# !/usr/bin/env python3
"""
    xpan multimedia file 
    include:
        listall
        filemetas
"""
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from pprint import pprint
from openapi_client.api import multimediafile_api
import openapi_client
import time


def listall():
    """
    listall
    """
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = multimediafile_api.MultimediafileApi(api_client)
        access_token = "123.56c5d1f8eedf1f9404c547282c5dbcf4.YmmjpAlsjUFbPly3mJizVYqdfGDLsBaY5pyg3qL.a9IIIQ"  # str |
        path = "/"  # str |
        recursion = 1  # int |
        web = "1"  # str |  (optional)
        start = 0  # int |  (optional)
        limit = 2  # int |  (optional)
        order = "time"  # str |  (optional)
        desc = 1  # int |  (optional)

        # example passing only required values which don't have defaults set
        # and optional values
        try:
            api_response = api_instance.xpanfilelistall(
                access_token, path, recursion, web=web, start=start, limit=limit, order=order, desc=desc)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling MultimediafileApi->xpanfilelistall: %s\n" % e)


def filemetas():
    """
    filemetas
    """
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = multimediafile_api.MultimediafileApi(api_client)
        access_token = "123.56c5d1f8eedf1f9404c547282c5dbcf4.YmmjpAlsjUFbPly3mJizVYqdfGDLsBaY5pyg3qL.a9IIIQ"  # str |
        fsids = "[258813175385405]"  # str |
        thumb = "1"  # str |  (optional)
        extra = "1"  # str |  (optional)
        dlink = "1"  # str |  (optional)
        needmedia = 1  # int |  (optional)

        # example passing only required values which don't have defaults set
        # and optional values
        try:
            api_response = api_instance.xpanmultimediafilemetas(
                access_token, fsids, thumb=thumb, extra=extra, dlink=dlink, needmedia=needmedia)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling MultimediafileApi->xpanmultimediafilemetas: %s\n" % e)


if __name__ == '__main__':
    listall()
    filemetas()
