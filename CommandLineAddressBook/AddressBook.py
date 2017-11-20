"""电话簿实现类"""
from CommandLineAddressBook import PersonCommon
from CommandLineAddressBook.Person import Person


def addPerson(name, identity, email, phone):
    """添加人员"""
    person = Person(name, identity, email, phone)
    PersonCommon.savePerson(person)


def deletePerson(name):
    """删除人员"""
    PersonCommon.removePerson(name)


def editPerson(name):
    """修改人员"""
    # TODO
    pass


def getPerson(name):
    """查找人员"""
    return PersonCommon.readPerson(name)


addPerson("lixibo", "family", "2324234234@gmail.com", "18050056054")
print(getPerson("lixibo"))
deletePerson("lixibo")
