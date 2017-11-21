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


def editPerson(name, identity, email, phone):
    """修改人员"""
    person = Person(name, identity, email, phone)
    PersonCommon.savePerson(person)


def getPerson(name):
    """查找人员"""
    person = PersonCommon.readPerson(name)
    if person:
        print("{}'s information is as follow:".format(name))
        print("name:{},identity:{},email:{},phone:{}".format(person.name, person.identity, person.email, person.phone))
    else:
        print("Can not find person: {}!".format(name))


def browseAll():
    addreddbook = PersonCommon.readAllPerson()
    for name, person in addreddbook.items():
        print("name:{},identity:{},email:{},phone:{}".format(person.name, person.identity, person.email, person.phone))


# Test Code
addPerson("alan1", "family", "111111111@gmail.com", "180111111111")
addPerson("alan2", "friend", "222222222@gmail.com", "180222222222")
addPerson("alan3", "friend", "333333333@gmail.com", "180333333333")
print("====print all people==========================================")
browseAll()
print("====test find someone========================================")
getPerson("alan1")
print()
getPerson("alan11111")
print("====test edit=================================================")
print("====before edit alan3")
getPerson("alan3")
print("====after edit alan3")
editPerson("alan3", "family", "aaaaaaaaa@gmail.com", "18099999999")
getPerson("alan3")
print("====test delete===============================================")
print("====before delete alan2")
getPerson("alan2")
deletePerson("alan2")
print("====after delete alan2")
getPerson("alan2")
