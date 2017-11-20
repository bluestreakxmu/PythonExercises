class Person:
    """人员信息。"""

    def __init__(self, name, identity, email, phone):
        """初始化人员信息。"""
        self.name = name  # 姓名
        self.identity = identity  # 身份：如朋友、家人、同事
        self.email = email  # 邮件地址
        self.phone = phone  # 电话号码
