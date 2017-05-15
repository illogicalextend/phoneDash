import getQueueData
import urllib2
import json
import extmap

# use fake local data when not querying prod queue.
fake = True

def realData():
    if fake is True:
        return getQueueData.getdata()
    else:
        data = urllib2.urlopen("http://url/loaddata")
        dataAsDict = json.loads(data.read())
        return dataAsDict

def processedRealAgents():
    realdata = realData()['agents']
    newlist = sorted(realdata, key=lambda k: k['idleTime'])
    newlist.reverse()
    return newlist

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
            return extmap.getTop(agent['extension'])
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
        if agent['queueName'] == "tier1":
            count = count + 1
    return count
