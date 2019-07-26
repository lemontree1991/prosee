import logging

from core.algorithms.base import BaseAlgorithm
from core.algorithms.fibonacci.tools import fib

logger = logging.getLogger(__name__)

class FibTask(BaseAlgorithm):
    """
    计算斐波那契数列
    """

    def init(self):
        logger.info(f"entering init function")
        return True

    def dowork(self):
        """
        接受两个位置参数
        第一位为第几个斐波那契数列
        第二位为计算多少个斐波那契数列
        :return:
        """

        start_num = int(self.args[0])
        num_count = int(self.args[1])
        result = []
        for i in range(num_count):
            result.append(fib(start_num+i))

            self.report((i+1)*10)
        self.report(100,"SUCCESS")
        return True


    def finish(self):
        logger.info(f"entering finish function")
        return True