import wiotp.sdk.device
import time
import random
myConfig = {
    "identity": {
        "orgId":"i63nvt",
        "devicetypeId":"GPS1",
        "deviceId":"i2345"
    },
    "auth":{
            "token":"abcdefghij"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IOT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

'client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)'
'client.connect()'

def pub (data):
    'client.publishEvent(eventId="status", msgFormat="json",data=mydata, qos=0, onPublish=None)'
    print("published data successfully: %s", mydata)

while True:
                        
    mydata={'name':'Train1','lat':17.6387448,'lon': 78.4754336}
    pub(mydata)
    time.sleep(3)
    #mydata={'name':'Train2','lat':17.6387448,'lon': 78.4754336}
    #pub(mydata)
    #time.sleep(3)
    mydata={'name':'Train1','lat':17.6341908,'lon': 78.4744722}
    pub(mydata)
    time.sleep(3)
    mydata={'name':'Train1','lat':17.6340889,'lon': 78.4745052}
    pub(mydata)
    time.sleep(3)
    mydata={'name':'Train1','lat':17.6248626,'lon': 78.4720259}
    pub(mydata)
    time.sleep(3)
    mydata={'name':'Train1','lat':17.6188577,'lon': 78.4698726}
    pub(mydata)
    time.sleep(3)
    mydata={'name':'Train1','lat':17.6132382,'lon': 78.4707318}
    pub(mydata)
    time.sleep(3)
client.commandCallback=mycommanCallbak
client.disconnect()
