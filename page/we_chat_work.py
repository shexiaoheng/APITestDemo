from page.base_api import BaseAPI


class WeChatWork(BaseAPI):
    ID = 'xxx'

    def get_token(self, secret):
        req = {
            'method': 'get',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'params': {
                'corpid': self.ID,
                'corpsecret': secret
            }
        }
        return self.send_api(req)['access_token']
