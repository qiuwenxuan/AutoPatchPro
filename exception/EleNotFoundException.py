class EleNotFoundException(Exception):
    """自定义异常，用于处理元素未找到的情况"""

    def __init__(self, message="Element not found"):
        # 调用基类的构造方法，传入异常信息
        super().__init__(message)
