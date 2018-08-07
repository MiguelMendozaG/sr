import numpy as np
import cv2

cap = cv2.VideoCapture(0)
i = 0
TRUE = 1
while TRUE:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("/home/miguelmg/dlib/tools/imglab/tmp/test/gesture/right/2/imagen" + str(i) + ".jpg", frame)
        #print ("/home/miguelmg/dlib/tools/imglab/tmp/images/imagen" + str(i) + ".jpg")
        i = i + 1
        #cTRUE = 0

    if cv2.waitKey(1) & 0xFF == ord('c'):
        print ("bye")
        TRUE = 0

# When everything done, release the capture
print (i)
cap.release()
cv2.destroyAllWindows()
