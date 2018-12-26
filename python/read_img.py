
"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""

import cv2


def show_webcam(mirror=False):
		
    #cam = cv2.VideoCapture("rtsp://admin:admin@192.168.1.108:554/cam/realmonitor?channel=1&subtype=2")
    cam = cv2.VideoCapture("rtsp://192.168.8.204:5000")
    while True:
        ret_val, img = cam.read()
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()
