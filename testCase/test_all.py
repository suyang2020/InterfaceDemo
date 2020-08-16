import unittest
import ddt
import json
from util.handle_excel import HandleExcel
from base.base_request import BaseRequest
from util.read_config import ReadConfig
from util.handle_result import handle_result
from util.handle_result import handle_result_json
from util.Log import MyLog as Log

excel = HandleExcel()
datas = excel.get_all_data()
rf = ReadConfig()
request = BaseRequest()
log = Log.get_log()
logger = log.get_logger()

# value[0], value[2], value[3], value[4], value[5], value[7], value[9], value[10]

@ddt.ddt
class TestAll(unittest.TestCase):
    def setup(self):
        pass

    @ddt.data(*datas)
    def test_all(self, value):
        # case编号  功能  是否执行  前置条件   url   method  测试目的
        # data    cookie操作    预期结果方式   预期结果   实际结果    是否通过
        case_id, is_run, condition, url, method, data, except_method, except_result = \
            value[0], value[2], value[3], value[4], value[5], value[7], value[9], value[10]
        logger.info("***********开始测试:%s***********" % case_id)
        logger.info("请求的地址>>>url:%s, method:%s" % (url, method))
        logger.info("***********测试参数data:%s***********" % data)
        logger.info("***********测试预期结果:%s***********" % except_result)

        row = excel.get_row_number(case_id)
        headers = rf.get_server("headers")
        headers = json.loads(headers)

        try:
            file = None
            if url == "/pos/order/submitOrder":
                headers = None
                data = json.loads(data)
                data['bankSerialNumber'] = request.get_uuid()
                data_temp = data['facadeImage']
                file = request.send_img(data_temp)
                data.pop('facadeImage')

            host = rf.get_server("host")
            all_url = host + url
            res = request.run_main(method, all_url, data, headers=headers, files=file)

            logger.info("响应结果：%s" % res)
            excel.write_excel(row, 12, res)
            try:
                code = str(res['code'])
                message = res['message']
            except KeyError:
                logger.error("响应结果中没有code或message")
            else:
                if except_method == "mess_err":
                    expect_message = handle_result(url, code)
                    try:
                        self.assertEqual(message, expect_message)
                        excel.write_excel(row, 13, "P")
                    except AssertionError as e:
                        excel.write_excel(row, 13, "F")
                        logger.error("code或者message不正确：%s" % str(e))
                        raise e
                elif except_method == "errorcode":
                    except_result = str(except_result)
                    try:
                        self.assertEqual(except_result, code)
                        excel.write_excel(row, 13, "P")
                    except AssertionError as e:
                        excel.write_excel(row, 13, "F")
                        logger.error("code不正确：%s" % str(e))
                        raise e
                else:
                    com_res = handle_result_json(except_result, res)
                    try:
                        assert com_res
                        excel.write_excel(row, 13, "P")
                    except AssertionError as e:
                        excel.write_excel(row, 13, "F")
                        logger.error("返回的响应信息不正确：%s" % str(e))
                        raise
        except Exception as e:
            excel.write_excel(row, 13, "F")
            logger.error("未知错误：%s" % str(e))
            raise e
        logger.info("***********结束测试:%s***********" % case_id)


if __name__ == '__main__':
    unittest.main()




