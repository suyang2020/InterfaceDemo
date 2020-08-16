import os
from base import HTMLTestRunner
import unittest
from util.Log import MyLog

base_path = os.path.dirname(os.path.abspath(__file__))


class RunAll:
    def __init__(self):
        global result_path, proDir
        proDir = os.path.dirname(os.path.abspath(__file__))
        result_path = os.path.join(proDir, "result")

        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def set_case_suit(self):
        """将case装入到suit中"""
        test_suite = unittest.TestSuite()
        suite_model = []
        case_file = os.path.join(proDir, "testCase")
        discover = unittest.defaultTestLoader.discover(case_file, pattern='test_*.py', top_level_dir=None)
        suite_model.append(discover)
        if len(suite_model) > 0:
            for suite in suite_model:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        logger = self.logger
        try:
            suit = self.set_case_suit()
            print(suit)
            if suit is not None:
                logger.info("************test start**************")
                report_path = os.path.join(result_path, 'report.html')
                fp = open(report_path, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='TestReport', description='TestDescription')
                runner.run(suit)
                fp.close()
            else:
                logger.info("Have no case to test")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("****************test end********************")


if __name__ == '__main__':
    RunAll().run()

