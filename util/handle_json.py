#coding=utf-8
import json
import os


class HandleJson:
    def __init__(self, json_path=None):
        self.json_path = json_path

    def read_json(self):
        """读取json文件内容并返回"""
        if os.path.exists(self.json_path):
            with open(self.json_path, encoding='utf-8') as f:
                data = json.load(f)
                return data
        else:
            raise FileNotFoundError("找不到json文件")

    def get_value(self, key):
        """获取json文件中某key对应的值"""
        data = self.read_json()
        try:
            return data[key]
        except KeyError:
            return None

    def update_value(self, data):
        """写入json文件"""
        keys = data.keys()
        data_old = self.read_json()
        for key in keys:
            data_old[key] = data[key]
        data_new = json.dumps(data_old, indent=2)
        with open(self.json_path, "w") as f:
            f.write(data_new)


if __name__ == '__main__':
    rj = HandleJson("../data/cookie.json")
    data = {
        "sql": 22,
        "12": 34
    }

    print(rj.update_value(data))






