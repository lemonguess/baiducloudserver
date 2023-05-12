# !/usr/bin/env python3
"""
    xpan upload
    include:
        precreate
        upload
        create
"""
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from pprint import pprint
from openapi_client.api import fileupload_api
import openapi_client

def precreate():
    """
    precreate
    """
    #    Enter a context with an instance of the API client
    with openapi_client.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = fileupload_api.FileuploadApi(api_client)
        access_token = "121.9e0c308cf787c62576144c588201b4ae.YGVefo2fL-cKOtmLHwxyn4ZCime2I2LfGXE-2HQ.Gbci_Q"  # str |
        path = "/apps/数据库备份/a.txt"  # str | 对于一般的第三方软件应用，路径以 "/apps/your-app-name/" 开头。对于小度等硬件应用，路径一般 "/来自：小度设备/" 开头。对于定制化配置的硬件应用，根据配置情况进行填写。
        isdir = 0  # int | isdir
        size = 271  # int | size
        autoinit = 1  # int | autoinit
        block_list = '["d05f84cf5340d1ef0c5f6d6eb8ce13b8"]' # str | 由MD5字符串组成的list
        rtype = 3  # int | rtype (optional)

        # example passing only required values which don't have defaults set
        # and optional values
        try:
            api_response = api_instance.xpanfileprecreate(
                access_token, path, isdir, size, autoinit, block_list, rtype=rtype)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling FileuploadApi->xpanfileprecreate: %s\n" % e)


def upload():
    """
    upload
    """
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = fileupload_api.FileuploadApi(api_client)
        access_token = "123.56c5d1f8eedf1f9404c547282c5dbcf4.YmmjpAlsjUFbPly3mJizVYqdfGDLsBaY5pyg3qL.a9IIIQ"  # str |
        partseq = "0"  # str |
        path = "/apps/hhhkoo/a.txt"  # str |
        uploadid = "N1-MTA2LjEzLjc2LjI0MDoxNjU0NTAwMDE0OjE3NDEzNzMyMTUxNTY1MTA2MQ=="  # str |
        type = "tmpfile"  # str |
        try:
            file = open('./uploadtestdata/a.txt', 'rb') # file_type | 要进行传送的本地文件分片
        except Exception as e:
            print("Exception when open file: %s\n" % e)
            exit(-1)

        # example passing only required values which don't have defaults set
        # and optional values
        try:
            api_response = api_instance.pcssuperfile2(
                access_token, partseq, path, uploadid, type, file=file)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling FileuploadApi->pcssuperfile2: %s\n" % e)


def create():
    """
    create
    """
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = fileupload_api.FileuploadApi(api_client)
        access_token = "123.56c5d1f8eedf1f9404c547282c5dbcf4.YmmjpAlsjUFbPly3mJizVYqdfGDLsBaY5pyg3qL.a9IIIQ"  # str |
        path = "/apps/hhhkoo/a.txt"  # str | 与precreate的path值保持一致
        isdir = 0  # int | isdir
        size = 271 # int | 与precreate的size值保持一致
        uploadid = "N1-MTA2LjEzLjc2LjI0MDoxNjU0NTAwMDE0OjE3NDEzNzMyMTUxNTY1MTA2MQ=="  # str | precreate返回的uploadid
        block_list = '["d05f84cf5340d1ef0c5f6d6eb8ce13b8"]'  # str | 与precreate的block_list值保持一致
        rtype = 3  # int | rtype (optional)

        # example passing only required values which don't have defaults set
        # and optional values
        try:
            api_response = api_instance.xpanfilecreate(
                access_token, path, isdir, size, uploadid, block_list, rtype=rtype)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling FileuploadApi->xpanfilecreate: %s\n" % e)


if __name__ == '__main__':
    precreate()
    upload()
    create()
