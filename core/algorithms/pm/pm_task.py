# -*- coding: UTF-8 -*-
import logging
import os
import time

import pandas as pd
import numpy as np

from core.algorithms.base import BaseAlgorithm
from core.algorithms.pm.tools import get_grade

logger = logging.getLogger("default")

class PMTask(BaseAlgorithm):

    # def __init__(self,task):
    #     super(PMTask,self).__init__(task,name="pm2.5 task")

    def init(self):
        logger.info(f"entering init function")
        return True

    def dowork(self):

        source_path = os.path.join(self.path,self.args[0])
        target_path = os.path.join(self.path, self.args[1])
        if os.path.exists(target_path):
            print(f"{target_path}已存在，删除")
            os.remove(target_path)
        for i in range(100):

            df = pd.read_csv(source_path,encoding="ISO-8859-1",chunksize=1000,iterator=True)
            for chunk in df:
                chunk.columns = ['Year', 'Month', 'Day', 'Hour', 'Value', 'QC']
                # 把错误值置为空值
                chunk.loc[chunk.Value < 0, 'Value'] = np.nan
                # 删除空值记录
                chunk.dropna(inplace=True)

                chunk.loc[:, 'Grade'] = chunk['Value'].apply(get_grade)

                chunk.to_csv(target_path,index=False,header=False,mode="a")
            self.report(i+1)
            # time.sleep(20)
        self.report(100,"SUCCESS")
        return True


    def finish(self):
        logger.info(f"entering finish function")
        return True