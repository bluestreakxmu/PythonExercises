"""人员公用方法"""
import pickle
import os

fileName = "AddressBookDictionary"


def savePerson(person):
    """持久化保存人员"""
    # 获取人员列表
    addressbook = {}
    if os.path.isfile(fileName):
        file = open(fileName, "rb")  # 以“二进制读”模式打开文件
        addressbook = pickle.load(file)
        file.close()

    # 给列表增加人员，覆盖同名人员
    addressbook[person.name] = person

    # 持久化人员列表
    file = open(fileName, "wb")  # 以“二进制写”模式打开文件
    pickle.dump(addressbook, file)  # 转储对象至文件
    file.close()


def readPerson(name):
    """从文件中读取电话簿并返回相应的人员"""
    if not os.path.isfile(fileName):
        return None

    file = open(fileName, "rb")  # 以“二进制读”模式打开文件
    addressbook = pickle.load(file)
    return addressbook[name] if name in addressbook else None


def readAllPerson():
    """查找所有人员"""
    if not os.path.isfile(fileName):
        return None
    file = open(fileName, "rb")  # 以“二进制读”模式打开文件
    return pickle.load(file)


def removePerson(name):
    """移除电话簿对应人员"""
    # 获取人员列表
    addressbook = {}
    if os.path.isfile(fileName):
        file = open(fileName, "rb")  # 以“二进制读”模式打开文件
        addressbook = pickle.load(file)
        file.close()

    # 删除对应人员
    if name not in addressbook:
        return
    del addressbook[name]

    # 持久化人员列表
    file = open(fileName, "wb")  # 以“二进制写”模式打开文件
    pickle.dump(addressbook, file)  # 转储对象至文件
    file.close()
