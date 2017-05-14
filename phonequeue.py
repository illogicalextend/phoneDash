import getQueueData
import urllib2
import json

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
