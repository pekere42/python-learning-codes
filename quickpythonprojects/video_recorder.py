import cv2 #importing opencv library 
import pyautogui #importing pyautogui for screenshot
import numpy as np


#identify resolution
resolution = (1920,1080)

#identify video codec 
codec = cv2.VideoWriter_fourcc(*"XVID")

#identify name of output file
filename = r"C:\Users\Enes\Desktop\Recording.avi"


#specify the frames rate(fps)
fps = 30.0

#creating a VideoWriter object
out = cv2.VideoWriter(filename,codec,fps,resolution)

#create an empty window
cv2.namedWindow("Live",cv2.WINDOW_NORMAL)
#resize the window
cv2.resizeWindow("Live",480,270)


while True:
    #take screenshots using pyautogui
    img = pyautogui.screenshot()

    #convert the screenshots to a numpy array
    frame = np.array(img)

    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


    # Write it to the output file
    out.write(frame)

    # Optional: Display the recording screen
    cv2.imshow('Live', frame)

    if cv2.waitKey(1) == ord('q'):
        break

# release the video writer
out.release()

#destroy all the windows
cv2.destroyAllWindows()


#optional you can add voice recorder 
