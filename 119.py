import cv2

video=cv2.VideoCapture("119/footvolleyball.mp4")



returned,myimage=video.read()

Tracker=cv2.TrackerCSRT_create()
print(Tracker)

bbox=cv2.selectROI("tracking",myimage,False)
print("what is bbox: ",bbox)

Tracker.init(myimage,bbox)

def draw_box(image,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]), int(bbox[3])
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(image,"Tracking",(300,200),cv2.FONT_HERSHEY_COMPLEX,0.7,(9,0,255),2)


while True:
    dummy, frame=video.read()
    success,mybox=Tracker.update(frame)


    if success==True:
        draw_box(frame,mybox)
    else:
        cv2.putText(frame,"lost",(300,200),cv2.FONT_HERSHEY_COMPLEX,0.7,(9,0,255),2)





    cv2.imshow("basketballllll", frame)

    if cv2.waitKey(1)==29:
 
        break
video.release()
cv2.destroyAllWindows()