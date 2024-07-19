import cv2
# import pickle 
import pickle 

# image = cv2.imread('resources/photos/car slot.png')
width,height = 89 ,39
# check if the slots are populated
try:
    with open('parking_slot','rb') as j:
    #if yes the add the initial values to the position list using pickle.load
        posList = pickle.load(j)    
except:
    # else populate with new values
    posList = [ ]

def mouseClick(event,x,y,flags,params):
    if event ==  cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if event == cv2.EVENT_RBUTTONDOWN:
        for i, p  in enumerate(posList):
            x1, y1 = p
            if x1 <x <x1+width and y1<y<y1+height:
                posList.pop(i)

    # createa pickle object to store our parking slot space
    with open('parking_slot','wb') as j:
        # call pickle and give it the position list and j as its parameters
        pickle.dump(posList, j)    

while True:
    # imort the image within the loop so as to eneble the deletion of unwanted rectangles 
    image = cv2.imread('resources/photos/car slot.png')
    for p in posList:
        cv2.rectangle(image , p,(p[0]+width, p[1]+height),(200,0,255),2)
    
    cv2.imshow("Packing",image)
    cv2.setMouseCallback("Packing",mouseClick)
    cv2.waitKey(1)