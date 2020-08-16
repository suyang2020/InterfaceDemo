# coding=utf-8
from util.handle_json import HandleJson


class HandleCookie:
    def __init__(self, file_path):
        self.file_path = file_path
        self.hj = HandleJson(self.file_path)

    def get_cookie(self, cookie_key):
        data = self.hj.read_json()
        try:
            cookie_data = data[cookie_key]
        except KeyError:
            print("请检查：%s" % cookie_key)
        else:
            return cookie_data

    def write_cookie(self, data):
        self.hj.update_value(data)


if __name__ == '__main__':
    rj = HandleCookie("../data/cookie.json")
    data = {
        "sql": {"123": "123333333333"},
        "4444": {"dd": "ee"}
    }

    print(rj.write_cookie(data))

