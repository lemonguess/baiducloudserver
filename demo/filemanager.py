# !/usr/bin/env python3
"""
    xpan filemanager 
    include:
        filemanager move
        filemanager copy
        filemanager remove
        filemanager delete
"""
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from pprint import pprint
import openapi_client
from openapi_client.api import filemanager_api


def move():
    """
    filemanager move
    """
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = filemanager_api.FilemanagerApi(api_client)
        access_token = "123.56c5d1f8eedf1f9404c547282c5dbcf4.YmmjpAlsjUFbPly3mJizVYqdfGDLsBaY5pyg3qL.a9IIIQ"  # str |
        _async = 1  # int | async
        # str | filelist
        filelist = '[{"path":"/test/123456.docx","dest":"/test/abc","newname":"123456.docx","ondup":"overwrite"}]'
        ondup = "overwrite"  # str | ondup (optional)

        # example passing only required values which don't have defaults set
        # and optional values
        try:
            api_response = api_instance.filemanagermove(
                access_token, _async, filelist, ondup=ondup)
            print(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling FilemanagerApi->filemanagermove: %s\n" % e)


def copy():
    """
    filemanager copy
    """
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = filemanager_api.FilemanagerApi(api_client)
        access_token = "123.56c5d1f8eedf1f9404c547282c5dbcf4.YmmjpAlsjUFbPly3mJizVYqdfGDLsBaY5pyg3qL.a9IIIQ"  # str |
        _async = 1  # int | async
        # str | filelist
        filelist = '[{"path":"/test/123456.docx","dest":"/test/abc","newname":"123.docx","ondup":"overwrite"}]'

        # example passing only required values which don't have defaults set
        try:
            api_response = api_instance.filemanagercopy(access_token, _async, filelist)
            print(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling FilemanagerApi->filemanagercopy: %s\n" % e)


def rename():
    """
    filemanager rename
    """
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = filemanager_api.FilemanagerApi(api_client)
        access_token = "123.56c5d1f8eedf1f9404c547282c5dbcf4.YmmjpAlsjUFbPly3mJizVYqdfGDLsBaY5pyg3qL.a9IIIQ"  # str |
        _async = 1  # int | async
        filelist = '[{"path":"/test/123456.docx","newname":"123.docx"}]'  # str | filelist
        ondup = "overwrite"  # str | ondup (optional)

        # example passing only required values which don't have defaults set
        # and optional values
        try:
            api_response = api_instance.filemanagerrename(
                access_token, _async, filelist, ondup=ondup)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling FilemanagerApi->filemanagerrename: %s\n" % e)


def delete():
    """
    filemanager delete
    """
    with openapi_client.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = filemanager_api.FilemanagerApi(api_client)
        access_token = "123.56c5d1f8eedf1f9404c547282c5dbcf4.YmmjpAlsjUFbPly3mJizVYqdfGDLsBaY5pyg3qL.a9IIIQ"  # str |
        _async = 1  # int | async
        filelist = '[{"path":"/test/123456.docx"}]'  # str | filelist
        ondup = "overwrite"  # str | ondup (optional)

        # example passing only required values which don't have defaults set
        # and optional values
        try:
            api_response = api_instance.filemanagerdelete(
                access_token, _async, filelist, ondup=ondup)
            print(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling FilemanagerApi->filemanagerdelete: %s\n" % e)


if __name__ == '__main__':
    copy()
    move()
    rename()
    delete()
