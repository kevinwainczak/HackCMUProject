from firstTest.models import *

#returns true if the demographics are equal,
# otherwise false. Also checks that roasts are the same
def demographicEqual(person, looker):
    if (person.gender == looker.gender
        && person.age == looker.age
        && person.race == looker.race
        && person.sexuality == looker.sexuality) return true
    if person.roast != looker.roast: return true
    return false


# given the parameters of name, gender, age, race, sexuality,
# and roast, will create an instance of a person
# see below for field keys
def createPerson(n, g, a, r, s, rst, t, d):
    result = Person(name=n, gender=g, age=a, race=r, sexuality=s, roast=rst, topic=t, distance=d, location=-1)
    result.save()
    return result

def checkForConvo():
    convo = []
    allElements = Person.objects.all()
    if len(allElements) < 3: return "no"
    for person in allElements:
        flag = 0
        for x in convo:
            if demographicEqual(person, x):
                flag = 1
        if flag == 0:
            convo.append(person)
        if len(convo) == 3:
            break
    return "yes"
# n = name, String
# g = gender, String
# a = age, Integer
# r = race, String
# s = sexuality, String
# rst = roast, String
# l = location
# topic = String
# maxP = max # of people in conversation, Int

# def newConversation(host,topic, maxP):
#     p = People(host=host, person1=NULL, person2=NULL)
#     p.save()
#     c = OpenConversations(conversationTopic=topic, people=p, maxPeople=maxP, peoplePresent=1)
#     c.save()
#     return

# # Returns an array of entires to the conversation table
# def findConversations(looker):
#     result=[]
#     qSet = OpenConversations.objects.all()
#     addFlag = 0
#     for (convo in qSet):
#         for (person in convo.people.objects.all()):
#             if demographicEqual(person, looker):
#                 addFlag = 1
#         if (addFlag == 0):
#             result.append(convo)
#     return result

# def addPersonToConvo(person, convo):
#     convo.peoplePresent += 1
#     if (convo.peoplePresent == 2):
#         convo.people.person1 = person
#     if (convo.peoplePresent == 3):
#         convo.people.person2 = person
#     if (convo.peoplePresent == 4):
#         convo.people.person3 = person
#     if (convo.peoplePresent == 5):
#         convo.people.person4 = person
#     return
#
# def conversationReady(convo):
#     return convo.peoplePresent == convo.maxPeople
#
# def removeConversation(convo):
#     return convo.delete()
