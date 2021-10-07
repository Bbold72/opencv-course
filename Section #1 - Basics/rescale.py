import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # images, videos, live video
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # live video
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture("..\\Resources\\Videos\\dog.mp4")

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame, scale=0.2)

    if isTrue:    
        cv.imshow('Video', frame)
        cv.imshow('Video Resized', frame_resized)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()


img = cv.imread("..\\Resources\\Photos\\cats.jpg")
img_resized = rescaleFrame(img)
cv.imshow('Cats', img)
cv.imshow('Cats', img_resized)

# waits infinite amount of time for keypress
cv.waitKey(0)