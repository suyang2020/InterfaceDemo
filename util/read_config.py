import os
import configparser

base_url = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.split(base_url)[0]


class ReadConfig:

    def __init__(self, file_path='config.ini'):
        self.file_path = os.path.join(project_dir, file_path)
        if self.file_path:
            self.cf = configparser.ConfigParser()
            self.cf.read(self.file_path, encoding='UTF-8')
        else:
            raise FileNotFoundError("config不存在，请检查路径")

    def get_server(self, name):
        return self.cf.get("server", name)

    def get_case(self, name):
        return self.cf.get("case", name)


if __name__ == '__main__':
    read_config = ReadConfig()
    print(read_config.get_server("host"))

