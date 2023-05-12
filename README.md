## 1. 授权管理

- 官方文档地址：[百度网盘开放平台简介 (baidu.com)](https://pan.baidu.com/union/doc/nksg0sbfs?menuKey=union-support-document)

- 官方接口文档：**[获取用户信息 (baidu.com)](https://pan.baidu.com/union/doc/pksg0s9ns)**
- 官方SDK：[Python SDK使用入门 (baidu.com)](https://pan.baidu.com/union/doc/Kl4gsu388)

获取code(最好是先登录百度账号，可以直接获取用户信息，否则还需要先登录认证)，下面的链接即获取code的链接(如果没有回调的话，redirect_uri默认为oob)：

```url
GET http://openapi.baidu.com/oauth/2.0/authorize?
response_type=code&
client_id=您应用的AppKey&
redirect_uri=您应用的授权回调地址&
scope=basic,netdisk&
device_id=您应用的AppID

以上链接示例中参数仅给出了必选参数，其中device_id为硬件应用下的必选参数。
关于应用的相关信息，您可在控制台，点进去您对应的应用，查看应用详情获得。
```


参数：

- client_id：必须参数，注册应用时获得的API Key。
- response_type：必须参数，此值固定为“code”。
- redirect_uri：必须参数，授权后要回调的URI，即接收Authorization Code的URI。如果用户在授权过程中取消授权，会回调该URI，并在URI末尾附上error=access_denied参数。对于无Web Server的应用，其值可以是“oob”，此时用户同意授权后，授权服务会将Authorization Code直接显示在响应页面的页面中及页面title中。非“oob”值的redirect_uri按照如下规则进行匹配：
  - （1）如果开发者在“授权安全设置”中配置了“授权回调地址”，则redirect_uri必须与“授权回调地址”中的某一个相匹配；
  - （2）如果未配置“授权回调地址”，redirect_uri所在域名必须与开发者注册应用时所提供的网站根域名列表或应用的站点地址（如果根域名列表没填写）的域名相匹配

### 1. 获取授权码

```
GET http://openapi.baidu.com/oauth/2.0/authorize?response_type=code&client_id=MsfpdXyapWkNsNll1tC37AadjnzqvCQN&redirect_uri=oob&scope=basic,netdisk&device_id=33195921
```

![image-20230505160902746](https://lemon-guess.oss-cn-hangzhou.aliyuncs.com/img/image-20230505160902746.png)

`5be61f064f4d0eed45cae5bf1edf192a`

这个有点傻，输入账号密码并通过旋转验证得到的授权，在服务器端玩个p呢

应该可以刷新token的，后面再试下,先换取AccessToken凭证

### 2. 换取AccessToken凭证

通过上述 1 拿到的用户授权码 Code 换取 Access Token 凭证。

换取 Access Token，依赖于以下链接：

```go
GET https://openapi.baidu.com/oauth/2.0/token?
grant_type=authorization_code&
code=用户授权码 Code 值&
client_id=您应用的AppKey&
client_secret=您应用的SecretKey&
redirect_uri=您应用设置的授权回调地址

以上链接示例中参数仅给出了必选参数。
关于应用的相关信息，您可在控制台，点进去您对应的应用，查看应用详情获得。
```

我的：

```
https://openapi.baidu.com/oauth/2.0/token?grant_type=authorization_code&code=5be61f064f4d0eed45cae5bf1edf192a&client_id=MsfpdXyapWkNsNll1tC37AadjnzqvCQN&client_secret=CvaijgF9FPOEDxeKD21p69LoCfLBIsSl&redirect_uri=oob
```

浏览器输入即可。

![image-20230505164013745](https://lemon-guess.oss-cn-hangzhou.aliyuncs.com/img/image-20230505164013745.png)

```json
{
    "expires_in": 2592000,
    "refresh_token": "122.78d3afc8dcc8306d8266e003176c9bd9.Y7wjChgKRLMxxaA6m8Uch1t_5Y1U5KA2S6jMvDS.jU2PHg",
    "access_token": "121.735c6353301ce30a0a0edbdb2aea84d6.Y7hQIfMXBqPpmm3eFeF6tJCeBIYNf5ONwbete0p.8pwFVA",
    "session_secret": "",
    "session_key": "",
    "scope": "basic netdisk"
}
```

官方Python示例：

```python
import requests

url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=authorization_code&code=d5a53cd0ca7799d033399487b23ec992&client_id=EVaI5x0U6lEmP125G0Su55ROEXZtItdD&client_secret=VPgfmrt8UBM5kgkeUemwRVmr5AjhFuEV&redirect_uri=oob"

payload = {}
headers = {
  'User-Agent': 'pan.baidu.com'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
```



### 3. 刷新授权码

```
GET https://openapi.baidu.com/oauth/2.0/token?
grant_type=refresh_token&
refresh_token=Refresh Token的值&
client_id=您应用的AppKey&
client_secret=您应用的SecretKey
```

以上链接示例中参数仅给出了必选参数。
关于应用的相关信息，您可在控制台，点进去您对应的应用，查看应用详情获得。
关于 Refresh Token的值，在换取 Access Token 凭证时，您可在响应信息中拿到。


```
https://openapi.baidu.com/oauth/2.0/token?grant_type=refresh_token&refresh_token=122.78d3afc8dcc8306d8266e003176c9bd9.Y7wjChgKRLMxxaA6m8Uch1t_5Y1U5KA2S6jMvDS.jU2PHg&client_id=MsfpdXyapWkNsNll1tC37AadjnzqvCQN&client_secret=CvaijgF9FPOEDxeKD21p69LoCfLBIsSl
```

![image-20230505164322338](https://lemon-guess.oss-cn-hangzhou.aliyuncs.com/img/image-20230505164322338.png)

```json
{
    "expires_in": 2592000,
    "refresh_token": "122.f7045bd6e2d9f7128a495bfd14607ab5.Y3UbvhApRWfZKsQiu9FA-SKdIJgtsZn7zGArW9O.qB6LFw",
    "access_token": "121.b1115977fd33f6d39de045c6565739f6.YBS4690TbRYaA2-PXNsP15xofeTixe-omHvLpEw.r048Hg",
    "session_secret": "",
    "session_key": "",
    "scope": "basic netdisk"
}
```



所以，理论上登陆一次就应该可以了

**获取用户access_token后，是否可以将文件上传到用户的网盘？**

作为开发者在获取到用户access_token后，是可以将文件上传到用户的网盘而非开发者的网盘。

更多帮助内容可查看https://pan.baidu.com/union/doc/0ksg0sbig

## 2. 接口验证

- 官方接口文档：**[获取用户信息 (baidu.com)](https://pan.baidu.com/union/doc/pksg0s9ns)**
- 官方SDK：[Python SDK使用入门 (baidu.com)](https://pan.baidu.com/union/doc/Kl4gsu388)

直接下载SDK，参考接口文档，用上面获取到的access_token进行测试：

![image-20230505165710871](https://lemon-guess.oss-cn-hangzhou.aliyuncs.com/img/image-20230505165710871.png)

通的。

后面就用代码编写即可。

贴一下接口列表吧，还是功能丰富的

| 接口功能                                            | 类                | 方法                                                         | HTTP 请求                                                    |
| --------------------------------------------------- | ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| *授权码模式-用户授权码 Code 换取 Access Token 凭证* | AuthApi           | [oauth_token_code2token](https://pan.baidu.com/union/doc/al0rwqzzl?from=open-sdk-go) | **GET** /oauth/2.0/token?grant_type=authorization_code&openapi=xpansdk |
| *设备码模式-获取设备码、用户码*                     | AuthApi           | [oauth_token_device_code](https://pan.baidu.com/union/doc/fl1x114ti?from=open-sdk-go) | **GET** /oauth/2.0/device/code?response_type=device_code&openapi=xpansdk |
| *设备码模式-用 Device Code 轮询换取 Access Token*   | AuthApi           | [oauth_token_device_token](https://pan.baidu.com/union/doc/fl1x114ti?from=open-sdk-go) | **GET** /oauth/2.0/token?grant_type=device_token&openapi=xpansdk |
| *授权码模式-刷新 Access Token*                      | AuthApi           | [oauth_token_refresh_token](https://pan.baidu.com/union/doc/al0rwqzzl?from=open-sdk-go) | **GET** /oauth/2.0/token?grant_type=refresh_token&openapi=xpansdk |
| *获取文件信息-获取文档列表*                         | FileinfoApi       | [xpanfiledoclist](https://pan.baidu.com/union/doc/Eksg0saqp?from=open-sdk-go) | **GET** /rest/2.0/xpan/file?method=doclist&openapi=xpansdk   |
| *获取文件信息-获取图片列表*                         | FileinfoApi       | [xpanfileimagelist](https://pan.baidu.com/union/doc/bksg0sayv?from=open-sdk-go) | **GET** /rest/2.0/xpan/file?method=imagelist&openapi=xpansdk |
| *获取文件信息-获取文件列表*                         | FileinfoApi       | [xpanfilelist](https://pan.baidu.com/union/doc/nksg0sat9?from=open-sdk-go) | **GET** /rest/2.0/xpan/file?method=list&openapi=xpansdk      |
| *获取文件信息-搜索文件*                             | FileinfoApi       | [xpanfilesearch](https://pan.baidu.com/union/doc/zksg0sb9z?from=open-sdk-go) | **GET** /rest/2.0/xpan/file?method=search&openapi=xpansdk    |
| *管理文件-文件复制*                                 | FilemanagerApi    | [filemanagercopy](https://pan.baidu.com/union/doc/mksg0s9l4?from=open-sdk-go) | **POST** /rest/2.0/xpan/file?method=filemanager&opera=copy&openapi=xpansdk |
| *管理文件-文件删除*                                 | FilemanagerApi    | [filemanagerdelete](https://pan.baidu.com/union/doc/mksg0s9l4?from=open-sdk-go) | **POST** /rest/2.0/xpan/file?method=filemanager&opera=delete&openapi=xpansdk |
| *管理文件-文件移动*                                 | FilemanagerApi    | [filemanagermove](https://pan.baidu.com/union/doc/mksg0s9l4?from=open-sdk-go) | **POST** /rest/2.0/xpan/file?method=filemanager&opera=move&openapi=xpansdk |
| *管理文件-文件重命名*                               | FilemanagerApi    | [filemanagerrename](https://pan.baidu.com/union/doc/mksg0s9l4?from=open-sdk-go) | **POST** /rest/2.0/xpan/file?method=filemanager&opera=rename&openapi=xpansdk |
| *文件上传-预上传*                                   | FileuploadApi     | [xpanfileprecreate](https://pan.baidu.com/union/doc/3ksg0s9r7?from=open-sdk-go) | **POST** /rest/2.0/xpan/file?method=precreate&openapi=xpansdk |
| *文件上传-分片上传*                                 | FileuploadApi     | [pcssuperfile2](https://pan.baidu.com/union/doc/nksg0s9vi?from=open-sdk-go) | **POST** /rest/2.0/pcs/superfile2?method=upload&openapi=xpansdk |
| *文件上传-创建文件*                                 | FileuploadApi     | [xpanfilecreate](https://pan.baidu.com/union/doc/rksg0sa17?from=open-sdk-go) | **POST** /rest/2.0/xpan/file?method=create&openapi=xpansdk   |
| *获取文件信息-递归获取文件列表*                     | MultimediafileApi | [xpanfilelistall](https://pan.baidu.com/union/doc/Zksg0sb73?from=open-sdk-go) | **GET** /rest/2.0/xpan/multimedia?method=listall&openapi=xpansdk |
| *获取文件信息-查询文件信息*                         | MultimediafileApi | [xpanmultimediafilemetas](https://pan.baidu.com/union/doc/Fksg0sbcm?from=open-sdk-go) | **GET** /rest/2.0/xpan/multimedia?method=filemetas&openapi=xpansdk |
| *获取网盘容量信息*                                  | UserinfoApi       | [apiquota](https://pan.baidu.com/union/doc/Cksg0s9ic?from=open-sdk-go) | **GET** /api/quota?openapi=xpansdk                           |
| *获取用户信息*                                      | UserinfoApi       | [xpannasuinfo](https://pan.baidu.com/union/doc/pksg0s9ns?from=open-sdk-go) | **GET** /rest/2.0/xpan/nas?method=uinfo&openapi=xpansdk      |

## 3. 上传

上传流程是指，用户将本地文件上传到百度网盘云端服务器的过程。文件上传分为三个阶段：[预上传](https://pan.baidu.com/union/doc/3ksg0s9r7)、[分片上传](https://pan.baidu.com/union/doc/nksg0s9vi)、[创建文件](https://pan.baidu.com/union/doc/rksg0sa17)。第二个阶段`分片上传`依赖第一个阶段`预上传`的结果，第三个阶段`创建文件`依赖第一个阶段`预上传`和第二阶段`分片上传`的结果，串行完成这三个阶段任务后，本地文件成功上传到网盘服务器。

 ![截屏2022-03-08 下午4.27.54.png](https://lemon-guess.oss-cn-hangzhou.aliyuncs.com/img/%E6%88%AA%E5%B1%8F2022-03-08%20%E4%B8%8B%E5%8D%884.27.54_2d8dc85.png)

dict_values(['d05f84cf5340d1ef0c5f6d6eb8ce13b8', 2960608591428628250])
