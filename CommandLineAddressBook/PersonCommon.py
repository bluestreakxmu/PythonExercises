"""人员公用方法"""
import pickle
import os

filePath = "personDictionary/"


def savePerson(person):
    """持久化保存人员"""
    filename = filePath + person.name
    file = open(filename, "wb")  # 以“二进制写”模式打开文件
    pickle.dump(person, file)  # 转储对象至文件
    file.close()


def readPerson(name):
    """从文件中读取电话簿并返回相应的人员"""
    filename = filePath + name
    file = open(filename, "rb")  # 以“二进制读”模式打开文件
    return pickle.load(file)


def removePerson(name):
    """移除电话簿对应人员"""
    filename = filePath + name
    os.remove(filename)
