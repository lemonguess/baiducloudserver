# !/usr/bin/env python3
"""
    xpan auth
    include:
        authorization_code, just get token by code
        refresh_token
        device_code
"""
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import openapi_client
from openapi_client.api import auth_api
from openapi_client.model.oauth_token_authorization_code_response import OauthTokenAuthorizationCodeResponse
from openapi_client.model.oauth_token_refresh_token_response import OauthTokenRefreshTokenResponse
from openapi_client.model.oauth_token_device_code_response import OauthTokenDeviceCodeResponse
from openapi_client.model.oauth_token_device_token_response import OauthTokenDeviceTokenResponse
from pprint import pprint


def oauthtoken_authorizationcode():
    """
    authorizationcode
    get token by authorization code
    """
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = auth_api.AuthApi(api_client)
        code = "3ce3370c960ce929306c419d32f92df1" # str | 
        client_id = "R2Ai3Qcsq2IYP2EXC3A8lmpkQ22iujVh" # str | 
        client_secret = "KMbyNtHpPkPq7KGGGKrQqunHRi2LMYjU" # str | 
        redirect_uri = "oob" # str | 

        # example passing only required values which don't have defaults set
        try:
            api_response = api_instance.oauth_token_code2token(code, client_id, client_secret, redirect_uri)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling AuthApi->oauth_token_code2token: %s\n" % e)


def oauthtoken_refreshtoken():
    """
    refresh access token
    """
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = auth_api.AuthApi(api_client)
        refresh_token = "122.5d587a6620cf03ebd221374097d5342a.Y3l9RzmaC4A1xq2F4xQtCnhIb4Ecp0citCARk0T.Uk3m_w" # str | 
        client_id = "R2Ai3Qcsq2IYP2EXC3A8lmpkQ22iujVh" # str | 
        client_secret = "KMbyNtHpPkPq7KGGGKrQqunHRi2LMYjU" # str | 

        # example passing only required values which don't have defaults set
        try:
            api_response = api_instance.oauth_token_refresh_token(refresh_token, client_id, client_secret)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling AuthApi->oauth_token_refresh_token: %s\n" % e)


def oauthtoken_devicecode():
    """
    devicecode 
    get device code 
    """
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = auth_api.AuthApi(api_client)
        client_id = "R2Ai3Qcsq2IYP2EXC3A8lmpkQ22iujVh" # str | 
        scope = "basic,netdisk" # str | 

        # example passing only required values which don't have defaults set
        try:
            api_response = api_instance.oauth_token_device_code(client_id, scope)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling AuthApi->oauth_token_device_code: %s\n" % e)


def oauthtoken_devicetoken():
    """
    get token by device code
    """
# Enter a context with an instance of the API client
    with openapi_client.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = auth_api.AuthApi(api_client)
        code = "1dc8cf189c863f094d25843dbbd3f633" # str | 
        client_id = "R2Ai3Qcsq2IYP2EXC3A8lmpkQ22iujVh" # str | 
        client_secret = "KMbyNtHpPkPq7KGGGKrQqunHRi2LMYjU" # str |

        # example passing only required values which don't have defaults set
        try:
            api_response = api_instance.oauth_token_device_token(code, client_id, client_secret)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling AuthApi->oauth_token_device_token: %s\n" % e)

if __name__ == '__main__':
    """
    main
    """
    oauthtoken_authorizationcode()
    # oauthtoken_refreshtoken()
    #
    # oauthtoken_devicecode()
    # oauthtoken_devicetoken()
