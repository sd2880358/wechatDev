import requests
import yaml
import urllib
import os
from wx.logging_config import logger
class FromBaidu:
    def __init__(self, **args) -> None:
        self.api_key = args['api_key']
        self.api_secret = args['api_secret']
        self.image_url = args['image_url']
        self.endpoint = args['params_dic']['endpoint']
        self.header = args['params_dic']['header']
        self.api_params = args['params_dic']['api_params']
        self.params_dic = args['params_dic']
        

    def main(self):
        '''
        Get access token and call baidu text extract API
        '''
        try:
            url =f"{self.endpoint['accurate_text']}{self.get_access_token()}"
            self.api_params['url'] = self.image_url
            payload = urllib.parse.urlencode(self.api_params, quote_via=urllib.parse.quote)
            print(payload)
            #TODO: change token to parameters instead.
            response = requests.request("POST", url, headers=self.header, data=payload)
            logger.info(response.json())
            return response.json()
        except Exception as e:
            logger.error(e)
            raise e
    
    def get_access_token(self):
        """
        使用 AK，SK 生成鉴权签名（Access Token）
        :return: access_token，或是None(如果错误)
        """
        #TODO: change this to dynamic variables
        params = {"grant_type": "client_credentials", "client_id": self.api_key, "client_secret": self.api_secret}
        return str(requests.post(self.endpoint['access_token'], params=params).json().get("access_token"))

'''
imageAsDic
'''
if __name__ == '__main__':
    with open('./baidu_api.yaml', 'r') as f:
        env_variables = yaml.safe_load(f)
    image_url = 'http://mmbiz.qpic.cn/sz_mmbiz_jpg/CJGa2MRlibIvK93xs3rXaVr0rBB4WduBrRicK38tM9MPlqrncZ0lEnEon96pOnyEpyOyJFIu9eZOqC5eAHob2Q4Q/0'
    API_KEY = os.environ['baiduAPIKey']
    SECRET_KEY = os.environ['baiduAPISecret']
    baidu_test = FromBaidu(image_url=image_url,api_key=API_KEY,api_secret=SECRET_KEY,params_dic=env_variables)
    baidu_test.main()

