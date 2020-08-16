#coding=utf-8
import os
import uuid
import requests
import json
from util.read_config import ReadConfig


class BaseRequest:

    def get_uuid(self):
        """获取uuid（16字节随机数，模拟银行唯一号）"""
        uid = str(uuid.uuid4())
        # suid = "".join(uid.split('-'))
        suid = uid.replace('-', '')
        return suid

    def send_post(self, url, data, headers=None, files=None, cookies=None):
        """发送post请求"""
        res = requests.post(url=url, data=data, headers=headers, files=files, cookies=cookies).text
        return res

    def send_get(self, url, data, headers=None, cookies=None):
        """发送get请求"""
        try:
            res = requests.get(url=url, params=data, headers=headers, cookies=cookies).text
        except TimeoutError:
            print("TimeoutError")
        else:
            return res

    def send_img(self, img_path, img_type="image/jpeg"):
        """上传图片文件"""
        file_name = os.path.split(img_path)[1]
        files = {"facadeImage": (file_name, open(img_path, "rb"), img_type, {})}

        return files

    def run_main(self, method, url, data=None, headers=None, files=None, cookies=None):
        """发送请求的方法"""
        if method == "get" or method == "GET":
            res = self.send_get(url, data, headers, cookies)
        elif method == "post" or method == "POST":
            res = self.send_post(url, data, headers, files, cookies)
        else:
            return
        return json.loads(res)


if __name__ == '__main__':
    br = BaseRequest()
    print(br.get_uuid())
    url = "https://open.weixin.qq.com/connect/oauth2/authorize"
    data = {
        "appid": "wxa0d72b6dff4ff3dd",
        "redirect_uri": ":https://cp.hengbao.net.cn/",
        "response_type": "code",
        "scope": "snsapi_base ",
        "": "#wechat_redirect"
    }

    # re = br.send_get(url, data)


