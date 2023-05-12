import requests, os, json


# 百度网盘上传
class BaiduApi:
    config_file = os.path.abspath(os.path.join(__file__, "../baidu_config.json"))
    client_id = "AppKey",
    client_secret = "SecretKey"

    def __init__(self, token) -> None:
        self.token = token
        self.access_token = self.get_access_token()
        self.refresh_token()

    def get_access_token(self):
        if not os.path.exists(self.config_file):
            data = requests.get("https://openapi.baidu.com/oauth/2.0/token", params={
                "grant_type": "authorization_code",
                "code": self.token,
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "redirect_uri": "oob"
            })
            if data.status_code != 200:
                raise ValueError(data.content)

            with open(self.config_file, "w") as f:
                f.write(data.content.decode())
            return data.json()
        with open(self.config_file, "r") as f:
            return json.loads(f.read())

    def refresh_token(self):
        data = requests.get("https://openapi.baidu.com/oauth/2.0/token", params={
            "grant_type": "refresh_token",
            "refresh_token": self.access_token["refresh_token"],
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": "oob"
        })
        if data.status_code != 200:
            raise ValueError(data.content)

        with open(self.config_file, "w") as f:
            f.write(data.content.decode())

    def _api(self, url, data):
        return requests.post(f"https://pan.baidu.com{url}", data=data, params={
            "access_token": self.access_token['access_token']
        })

    def _md5(self, data):
        return hashlib.md5(data).hexdigest()

    def precreate(self, block_list, fileSize, path):
        data = self._api("/rest/2.0/xpan/file?method=precreate", data={
            "path": path,
            'rtype': '1',
            "size": fileSize,
            "isdir": 0,
            "block_list": json.dumps(block_list),
            "autoinit": 1
        })
        if data.status_code != 200:
            raise ValueError(data.content)
        return data.json()

    def superfile2(self, precreateData, block_data, block_list):

        for i in precreateData['block_list']:
            data = requests.post("https://d.pcs.baidu.com/rest/2.0/pcs/superfile2?method=upload",
                                 params={
                                     "access_token": self.access_token['access_token'],
                                     "method": "upload",
                                     "type": "tmpfile",
                                     "path": precreateData["path"],
                                     "uploadid": precreateData["uploadid"],
                                     "partseq": i
                                 },
                                 files=[
                                     ("file", block_data[i])
                                 ]
                                 )
            if data.status_code != 200:
                raise ValueError(data.content)

            m5 = data.json()["md5"]
            if not m5:
                raise ValueError(data.content)
            block_list[i] = m5
        return block_list

    def uploadFile(self, path, remotePth="/ATestApp/"):

        fileSize = os.path.getsize(path)
        if fileSize == 0:
            return "文件为空"
        block_list = []
        block_data = []
        with open(path, "rb") as f:
            while True:
                buffer = f.read(4 * 1024 * 1024)
                if not buffer:
                    break
                block_list.append(self._md5(buffer))
                block_data.append(buffer)

        # ATestApp
        path = remotePth + os.path.basename(path)

        updata = self.precreate(block_list, fileSize, path)

        updata["path"] = path

        block_list = self.superfile2(updata, block_data, block_list)
        data2 = requests.post("https://pan.baidu.com/rest/2.0/xpan/file?method=create", params={
            "access_token": self.access_token['access_token']
        },
                              data={
                                  "path": updata["path"],
                                  "size": fileSize,
                                  "isdir": 0,
                                  "block_list": json.dumps(block_list),
                                  "uploadid": updata["uploadid"],
                                  "rtype": 3
                              })
        if data2.status_code != 200:
            raise ValueError(data2.content)
        return data2.json()

    def upDir(self, dir, remotePth):
        for home, dirs, files in os.walk(dir):
            for filename in files:
                f = os.path.abspath(os.path.join(home, filename))
                r = os.path.normpath(os.path.join(remotePth, "." + home.replace(dir, "").replace("\\", "/"))).replace(
                    "\\", "/")
                print(self.uploadFile(f, r))


# 使用方法
# 授权的token
a = BaiduApi("f62e1dbb7eaf1fc8a31433a0f0b31866")
# 上传目录
a.upDir(r"E:/code/test", "/code/2022-10-14/")
# 上传文件
a.uploadFile("文件路径", "远程文件路径")


