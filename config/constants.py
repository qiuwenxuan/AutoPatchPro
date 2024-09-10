import os
from datetime import datetime

"""全局常量global constants"""
# 工作目录
WORKSPACE = os.getcwd()
# 当前脚本路径
CURRENT_PATH = os.path.abspath(__file__)
# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试报告目录
REPORT_DIR = os.path.join(ROOT_DIR, 'report')
# 日志配置文件所在目录
LOG_INPUT_DIR = os.path.join(ROOT_DIR, 'logs')
# 输出日志文件目录
LOG_PATH = os.path.join(ROOT_DIR, 'config', 'logger.yaml')
# 测试数据所在目录
DATA_PATH = os.path.join(ROOT_DIR, 'data', 'tcData.xlsx')
# 当前时间
CURRENT_TIME = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    print("工作目录:" + WORKSPACE)
    print("当前脚本路径:" + CURRENT_PATH)
    print("项目根目录:" + ROOT_DIR)
    print("测试报告目录:" + REPORT_DIR)
    print("配置文件所在目录:" + LOG_PATH)
    print("输出日志文件目录:" + LOG_INPUT_DIR)
    print("测试数据所在目录:" + DATA_PATH)
    print("当前时间:" + CURRENT_TIME)
