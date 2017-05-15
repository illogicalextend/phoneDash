import getQueueData
import urllib2
import json
import extmap

def fakeData():
    return getQueueData.getdata()


def realData():
    data = urllib2.urlopen("http://url/loaddata")
    dataAsDict = json.loads(data.read())
    return dataAsDict

def processedFakeAgents():
    fakedata = fakeData()['agents']
    newlist = sorted(fakedata, key=lambda k: k['idleTime'])
    return newlist

def processedRealAgents():
    realdata = realData()['agents']
    realdata.reverse()
    return realdata

def processedTier1RealAgents():
    newlist = []
    realdata = realData()['agents']
    for agent in realdata:
        if agent['queueName'] == "tier1":
            newlist.append(agent)
    return newlist

def onTopQueue():
    for agent in processedRealAgents():
        if agent['status'] == "Idle" and agent['queueName'] == "tier1":
            return agent['extension']
    #onTop = extmap.getTop(processedRealAgents()[0]['extension'])
    #return onTop

def onTopQueueName():
    for agent in processedRealAgents():
        if agent['status'] == "Idle" and agent['queueName'] == "tier1":
            return agent['name']

def agentFreeCount():
    agentList = processedRealAgents()
    count = 0
    for agent in agentList:
        #if agent['queueName'] == "tier1":
        count = count + 1
    return count
