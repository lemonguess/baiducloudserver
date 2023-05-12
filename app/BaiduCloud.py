# -*- coding: UTF-8 -*-
"""=========================================================
@Project -> File: BaiduCloudServer -> BaiduCloud
@IDE: PyCharm
@author: lxc
@date: 2023/5/5 下午 5:37
@Desc:
1-功能描述：

2-实现步骤
    1-
"""
import os, json
import openapi_client
from openapi_client.api import fileinfo_api
from openapi_client.api import auth_api
from openapi_client.api import fileupload_api
from utils.log_util import Logger
logger = Logger().get_logger()


# 百度网盘上传
class BaiduApi:
    config_file = os.path.abspath(os.path.join(__file__, "../../config/baidu_config.json"))
    client_id = "MsfpdXyapWkNsNll1tC37AadjnzqvCQN"
    client_secret = "CvaijgF9FPOEDxeKD21p69LoCfLBIsSl"
    AppID = "33195921"
    Signkey = "9M@@rQ=wQeIs!m!VtU4G~q#2pHz^hHV7"

    def __init__(self, token) -> None:
        self.token = token
        self.access_token, self.refresh_token = self.get_access_token()
        logger.info(self.access_token)
    def get_access_token(self):
        if not os.path.exists(self.config_file):
            data = self.oauthtoken_authorizationcode()
            with open(self.config_file, "w") as f:
                f.write(json.dumps(data))
        with open(self.config_file, "r") as f:
            data = json.loads(f.read())
        return data['access_token'], data['refresh_token']

    def oauthtoken_authorizationcode(self):
        """
        authorizationcode
        get token by authorization code
        """
        # Enter a context with an instance of the API client
        with openapi_client.ApiClient() as api_client:
            # Create an instance of the API class
            api_instance = auth_api.AuthApi(api_client)
            code = self.token  # str |
            client_id = self.client_id  # str |
            client_secret = self.client_secret  # str |
            redirect_uri = "oob"  # str |

            # example passing only required values which don't have defaults set
            try:
                api_response = api_instance.oauth_token_code2token(code, client_id, client_secret, redirect_uri)
                logger.info(api_response)
                return api_response.to_dict()
            except openapi_client.ApiException as e:
                logger.error("Exception when calling AuthApi->oauth_token_code2token: %s\n" % e)
                raise TimeoutError(
                    "token已超时(10分钟)，请登录链接重新获取token\n"
                    "https://openapi.baidu.com/oauth/2.0/authorize?client_id=MsfpdXyapWkNsNll1tC37AadjnzqvCQN&device_id=33195921&errmsg=Auth+Login+Sucess&errno=0&redirect_uri=oob&response_type=code&scope=basic%2Cnetdisk&ssnerror=0&stoken=gCsoTP1rsRonRGY574eXas8UjVy0Xk7cB6X7%2F0SAyzDZWv1GX2AKmAckWu%2BDNPLyojOHjPXQS7I4dQTMJhE2A%2Be42QejrcI6%2FEzM2YqJfkyhXntC5qndIohj9UhkSjoFCE8qh%2BAK4gkhmQmHYAHVeo3jlcn80Eq9ZPoud4aw2BIcskPs5V85iXaI%2FDGrfJve4Jf3x640YsAhWGBAgLtF1AO6K3Gn3U%2FK%2BhF5wO07yZuCcScipKTVP4LM7rcSwzFclnmQJ5pZV2cs4InuRMlBPQ"
                )

    def oauthtoken_refreshtoken(self):
        """
        refresh access token
        """
        # Enter a context with an instance of the API client
        with openapi_client.ApiClient() as api_client:
            # Create an instance of the API class
            api_instance = auth_api.AuthApi(api_client)
            refresh_token = self.refresh_token  # str |
            client_id = self.client_id  # str |
            client_secret = self.client_secret  # str |
            # example passing only required values which don't have defaults set
            try:
                api_response = api_instance.oauth_token_refresh_token(refresh_token, client_id, client_secret)
                logger.info(api_response)
            except openapi_client.ApiException as e:
                logger.error("Exception when calling AuthApi->oauth_token_refresh_token: %s\n" % e)

    def search(self, **kwargs):
        """
        search
        """
        # Enter a context with an instance of the API client
        key = kwargs.get('key')  # str |
        if not key:
            raise Warning("key为空，请输入查询参数！")
        web = kwargs.get('web', "1")  # str |  (optional)
        num = kwargs.get('num', "2")  # str |  (optional)
        page = kwargs.get('page', "1")  # str |  (optional)
        dir = kwargs.get('dir', "/")  # str |  (optional)
        recursion = kwargs.get('web', "1")  # str |  (optional)
        with openapi_client.ApiClient() as api_client:
            # Create an instance of the API class
            api_instance = fileinfo_api.FileinfoApi(api_client)
            access_token = self.access_token  # str |

            # example passing only required values which don't have defaults set
            # and optional values
            try:
                api_response = api_instance.xpanfilesearch(
                    access_token, key, web=web, num=num, page=page, dir=dir, recursion=recursion)
                logger.info(api_response)
                return api_response
            except openapi_client.ApiException as e:
                logger.info("Exception when calling FileinfoApi->xpanfilesearch: %s\n" % e)
    def upload(self):
        """
        upload
        """
        # Enter a context with an instance of the API client
        with openapi_client.ApiClient() as api_client:
            # Create an instance of the API class
            api_instance = fileupload_api.FileuploadApi(api_client)
            access_token = self.access_token  # str |
            partseq = "0"  # str |
            path = "/数据库备份/"  # str |
            uploadid = "N1-MTA2LjEzLjc2LjI0MDoxNjU0NTAwMDE0OjE3NDEzNzMyMTUxNTY1MTA2MQ=="  # str |
            type = "tmpfile"  # str |
            try:
                file = open(r'D:\workspace\爬虫相关文件\oceanspider文档\cookies池的搭建.zip', 'rb') # file_type | 要进行传送的本地文件分片
            except Exception as e:
                print("Exception when open file: %s\n" % e)
                exit(-1)

            # example passing only required values which don't have defaults set
            # and optional values
            try:
                api_response = api_instance.pcssuperfile2(
                    access_token, partseq, path, uploadid, type, file=file)
                logger.info(api_response)
            except openapi_client.ApiException as e:
                logger.error("Exception when calling FileuploadApi->pcssuperfile2: %s\n" % e)

if __name__ == '__main__':
    # 仅10分钟有效期，请登录链接获取最新token值
    # url: https://openapi.baidu.com/oauth/2.0/authorize?client_id=MsfpdXyapWkNsNll1tC37AadjnzqvCQN&device_id=33195921&errmsg=Auth+Login+Sucess&errno=0&redirect_uri=oob&response_type=code&scope=basic%2Cnetdisk&ssnerror=0&stoken=gCsoTP1rsRonRGY574eXas8UjVy0Xk7cB6X7%2F0SAyzDZWv1GX2AKmAckWu%2BDNPLyojOHjPXQS7I4dQTMJhE2A%2Be42QejrcI6%2FEzM2YqJfkyhXntC5qndIohj9UhkSjoFCE8qh%2BAK4gkhmQmHYAHVeo3jlcn80Eq9ZPoud4aw2BIcskPs5V85iXaI%2FDGrfJve4Jf3x640YsAhWGBAgLtF1AO6K3Gn3U%2FK%2BhF5wO07yZuCcScipKTVP4LM7rcSwzFclnmQJ5pZV2cs4InuRMlBPQ
    TOKEN = "b065786d9896d9e3f90981e5f0417708"
    # 搜索 search
    BaiduCloud = BaiduApi(TOKEN)
    # BaiduCloud.upload()
    search_res = json.dumps(BaiduCloud.search(key='python', page="1", dir='/视频课程/买的资源/AI/0000黑马【年度钻石会员】人工智能AI进阶2022年/【课外拓展】05、阶段五 阶段一 python基础（更新）/第一章 1-python基础编程/'), indent=4, ensure_ascii=False)
    print(search_res)
    # print(BaiduCloud.oauthtoken_authorizationcode())
# 使用方法
# 授权的token

# # 上传目录
# BaiduCloud.upDir(r"E:/code/test", "/code/2022-10-14/")
# # 上传文件
# BaiduCloud.uploadFile("文件路径", "远程文件路径")
