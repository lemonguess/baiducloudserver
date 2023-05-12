# -*- coding: UTF-8 -*-
"""=========================================================
@Project -> File: BaiduCloudServer -> upload
@IDE: PyCharm
@author: lxc
@date: 2023/5/6 下午 5:13
@Desc:
1-功能描述：

2-实现步骤
    1-
"""
import hashlib
import json
import os
import sys
import urllib
from urllib import parse
from openapi_client.api import fileupload_api
import openapi_client
import logging
logger = logging.getLogger('log')
from io import BufferedReader, BytesIO

class BaiduUpload:
    def __init__(self, **kwargs):
        self.remote_path = kwargs.get("remote_path")
        self.file_path = kwargs.get("file_path")
        self.access_token = "121.9e0c308cf787c62576144c588201b4ae.YGVefo2fL-cKOtmLHwxyn4ZCime2I2LfGXE-2HQ.Gbci_Q"
        self.isdir = 0
        self.uploadid = ""
        self.block_list = ""
        self.size = 0
    def main(self):
        """
        主运行
        :return:
        """
        self.size = os.path.getsize(self.file_path)
        if self.size == 0:
            raise TypeError("文件为空")
        block_list = []
        block_data = []
        with open(self.file_path, "rb") as f:
            while True:
                buffer = f.read(4 * 1024 * 1024)
                if not buffer:
                    break
                block_list.append(self._md5(buffer))
                block_data.append(buffer)
        self.block_list = json.dumps(block_list, ensure_ascii=False)
        self.block_data = block_data
        self.precreate()
        self.upload()
        self.create()
    @staticmethod
    def _md5(data):
        return hashlib.md5(data).hexdigest()

    def precreate(self):
        """
        precreate
        """
        #    Enter a context with an instance of the API client
        with openapi_client.ApiClient() as api_client:
            # Create an instance of the API class
            api_instance = fileupload_api.FileuploadApi(api_client)
            access_token = self.access_token  # str |
            path = self.remote_path  # str | 对于一般的第三方软件应用，路径以 "/apps/your-app-name/" 开头。对于小度等硬件应用，路径一般 "/来自：小度设备/" 开头。对于定制化配置的硬件应用，根据配置情况进行填写。
            isdir = self.isdir  # int | isdir
            size = self.size  # int | size
            autoinit = 1  # int | autoinit
            block_list = self.block_list  # str | 由MD5字符串组成的list
            rtype = 3  # int | rtype (optional)

            # example passing only required values which don't have defaults set
            # and optional values
            try:
                api_response = api_instance.xpanfileprecreate(
                    access_token, path, isdir, size, autoinit, block_list, rtype=rtype)
                logger.info(api_response)
                self.uploadid = api_response.get('uploadid')
                self.block_seq_list = api_response.get('block_list', [0])
            except openapi_client.ApiException as e:
                logger.error("Exception when calling FileuploadApi->xpanfileprecreate: %s\n" % e)

    def upload(self):
        """
        upload
        """
        # Enter a context with an instance of the API client
        with openapi_client.ApiClient() as api_client:
            # Create an instance of the API class
            for partseq in self.block_seq_list:
                api_instance = fileupload_api.FileuploadApi(api_client)
                access_token = self.access_token  # str |
                partseq = str(partseq)  # str |
                # partseq = partseq # str |
                # path = urllib.parse.quote(self.remote_path)  # str |
                path = self.remote_path  # str |
                uploadid = self.uploadid  # str |
                type = "tmpfile"  # str |
                try:
                    if len(self.block_seq_list) == 1:
                        file = open(self.file_path, 'rb')  # file_type | 要进行传送的本地文件分片
                    elif len(self.block_seq_list) > 1:
                        bytes_io = BytesIO(self.block_data[int(partseq)])
                        bytes_io.name = ''
                        bytes_io.mode = 'rb'
                        file = BufferedReader(bytes_io)
                    else:
                        raise FileExistsError
                except Exception as e:
                    logger.error("Exception when open file: %s\n" % e)
                    exit(-1)

                # example passing only required values which don't have defaults set
                # and optional values
                try:
                    api_response = api_instance.pcssuperfile2(
                        access_token, partseq, path, uploadid, type, file=file)
                    logger.info(api_response)
                except openapi_client.ApiException as e:
                    logger.error("Exception when calling FileuploadApi->pcssuperfile2: %s\n" % e)

    def create(self):
        """
        create
        """
        # Enter a context with an instance of the API client
        with openapi_client.ApiClient() as api_client:
            # Create an instance of the API class
            api_instance = fileupload_api.FileuploadApi(api_client)
            access_token = self.access_token  # str |
            path = self.remote_path  # str | 与precreate的path值保持一致
            isdir = self.isdir  # int | isdir
            size = self.size  # int | 与precreate的size值保持一致
            uploadid = self.uploadid  # str | precreate返回的uploadid
            block_list = self.block_list  # str | 与precreate的block_list值保持一致
            rtype = 3  # int | rtype (optional)

            # example passing only required values which don't have defaults set
            # and optional values
            try:
                api_response = api_instance.xpanfilecreate(
                    access_token, path, isdir, size, uploadid, block_list, rtype=rtype)
                logger.info(api_response)
            except openapi_client.ApiException as e:
                logger.error("Exception when calling FileuploadApi->xpanfilecreate: %s\n" % e)
if __name__ == '__main__':
    # 小于 4M 的文件测试
    # BaiduUpload(file_path='../demo/uploadtestdata/a.txt', remote_path='/apps/数据库备份/文档测试/c.txt').main()
    # 大于 4M 的文件测试
    # BaiduUpload(file_path=r'../demo/uploadtestdata/uninstall.exe', remote_path='/apps/数据库备份/文档测试/uninstall.exe').main()
    # 文件夹 上传测试
    BaiduUpload(file_path=r'../demo/uploadtestdata/', remote_path='/apps/数据库备份/文档测试/uploadtestdata', isdir=1).main()