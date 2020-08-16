from util.handle_excel import HandleExcel
from jsonpath_rw import parse


excel = HandleExcel()


def split_data(data):
    case_ids = data.split("<")
    return case_ids


def depend_data(data):
    case_ids = split_data(data)
    datas = list()
    for id in case_ids:
        datas.append()



