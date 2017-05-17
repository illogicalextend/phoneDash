import getQueueData
import urllib2
import json
import extmap
import datetime

# use fake local data when not querying prod queue.
fake = False

def realData():
    if fake is True:
        return getQueueData.getdata()
    else:
        data = urllib2.urlopen("http://spbpbxmon02.amust.local/loaddata")
        dataAsDict = json.loads(data.read())
        return dataAsDict

def processedRealAgents():
    realdata = realData()['agents']
    # don't call timedelta if no agents present.
    if realdata:
        for agent in realdata:
            agent['idleTime'] = str(datetime.timedelta(seconds=agent['idleTime']))
        newlist = sorted(realdata, key=lambda k: k['idleTime'])
        newlist.reverse()
        return newlist

def processedOnCalls():
    calls = realData()['calls']
    # don't call timedelta if no agents present.
    for call in calls:
        call['duration'] = str(datetime.timedelta(seconds=call['duration']))
    newlist = sorted(calls, key=lambda k: k['duration'])
    newlist.reverse()
    return newlist

def processedRealInbound():
    realdata = realData()['calls']
    newlist = sorted(realdata, key=lambda k: k['duration'])
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
        if agent['queueName'] == "tier1" and agent['status'] == "Idle":
            count = count + 1
    return count
