import json

from util.handle_json import HandleJson
import os
from deepdiff import DeepDiff

base_url = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.split(base_url)[0]
json_path = os.path.join(project_path, 'data/code_message.json')
read_json = HandleJson(json_path)


def handle_result(url, code):
    try:
        res = read_json.get_value(url)[str(code)]
    except KeyError:
        return None
    except TypeError:
        print("请检查url")
        raise
    else:
        return res


def handle_result_json(json1, json2):
    if isinstance(json1, str) and isinstance(json2, str):
        dict1 = json.loads(json1)
        dict2 = json.loads(json2)
    else:
        dict1 = json1
        dict2 = json2

    # DeepDiff() 可以比较两个字典，如果字典相同，返回一个空字典，如果字典不相同，返回不相同的键
    compare_result = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
    print(compare_result)
    if compare_result.get("dictionary_item_added"):
        return False
    elif compare_result.get("dictionary_item_removed"):
        return False
    else:
        return True


if __name__ == '__main__':

    # print(handle_result('/pos/order/submitOrder', '1001'))
    json1 = '{"aa": {"bb": "BB", "aa": "AA"}, "bb": "BB", "cc": [1, 2]}'
    json2 = '{"bb": "Bc", "aa": {"bb": "BB", "aa": "AA"}, "cd": [1, 2], "ee": "EE"}'
    handle_result_json(json1, json2)
