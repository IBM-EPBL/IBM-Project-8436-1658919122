import cv2
import numpy as np
import time
import pyzbar.pyzbar as puzbar
from ibmcloudant.cloudant_v1 import cloudantv1
from ibmcloudant import couchDbsessionAuthenticator
from ibm_cloud_sdk_core.Authenticators import BasicAuhtenticator

authenticator=BasicAuthenticator('apikey-v2-16u3crmdpkghhxefdikvpssoh5fwezrmuup5fv5g3ubz','b0ab119f45d3e6255eabb978')
service =cloudantv1(authenticator=authenticator)
service.set_service_url('https://apikey-v2-16u3crmdpkghhxefdikvpssoh5fwezrmuup5fv5g3ubz:b0ab119f45d3e6255eabb978')

cap = cv2.videoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read(0)
    decodeObjects = pyzbar.decode(frame)
    for obj in decodeObjects:
        #print("Data",obj.data)
        a=obj.data.decode('UTF-8')
        cv2.putText(frame,"Ticket",(50, 50),font, 2,
                    (255,0, 0), 3)
        #print(a)
        try:
             responce = service.get_document (
                  db='booking',
                  doc_id = a
                  ).get_result()
             print(response)
             time.sleep(5)
        except Exception as e:
            print ("Not valid Ticket")
            time.sleep(5)

    cap.imshow("Frame", frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()
client.disconnect()
