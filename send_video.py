import socket
import numpy as np
import cv2
UDP_IP = '127.0.0.1'                  
UDP_PORT = 999        
cap = cv2.VideoCapture('drop.avi')
while(True):
   ret, frame = cap.read()
   cv2.imshow('frame',frame)
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   d = frame.flatten ()
   s = d.tostring ()
   for i in range(20):
        sock.sendto (s[i*184320:(i+1)*184320],(UDP_IP, UDP_PORT))

        if cv2.waitKey(1) & 0xFF == ord('q'):
          break

cap.release()
cv2.destroyAllWindows()