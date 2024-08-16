from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

def object_detection_with_bounding_boxes(filename, model="yolov3", confidence=0.2):
 
  # Read the image into a numpy array
    #img = cv2.imread(filename)
     
    # Perform the object detection
    bbox, label, conf = cv.detect_common_objects(filename, confidence=confidence, model=model)
     
    # Print current image's filename
    print(f"========================\nImage processed: {filename}\n")
     
    # Print detected objects with confidence level
    for l, c in zip(label, conf):
        print(f"Detected object: {l} with confidence level of {c}\n")
     
    # Create a new image that includes the bounding boxes
    output_image = draw_bbox(filename, bbox, label, conf)
    return (output_image)
    # Save the image in the directory images_with_boxes
    #cv2.imwrite(f'images_with_boxes/{filename}', output_image)
     
    # Display the image with bounding boxes
    #display(Image(f'images_with_boxes/{filename}'))

camera = PiCamera()

camera.resolution=(640,480)

camera.framerate=2

raw_capture=PiRGBArray(camera,size=(640,480))

time.sleep(0.1)

for frame in camera.capture_continuous(raw_capture,format="bgr",use_video_port=True):
    image=frame.array
    #print(image)
    img2 = object_detection_with_bounding_boxes(image)
    cv2.imshow("Frame",img2)
    key=cv2.waitKey(1) & 0xFF
    raw_capture.truncate(0)
    if key==ord("q"):
        break