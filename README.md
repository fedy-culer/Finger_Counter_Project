# Finger_Counter_Project

This script, FingerCounter.py, counts the number of fingers displayed using a webcam and overlays an image corresponding to the count on the video feed. Below is an overview of the script along with instructions on how to run it.

Script Overview :
The FingerCounter.py script captures video frames from the webcam using OpenCV and detects hand gestures using the HandTrackingModule library. It counts the number of fingers displayed by the user's hand and overlays an image corresponding to the finger count on the video feed.

Usage :

Upon execution, the script will open a window displaying the video feed from the webcam. As you display different numbers of fingers, the corresponding images will be overlaid on the video feed.

Dependencies :
The script requires the following Python libraries:

cv2 (OpenCV)
HandTrackingModule (Custom module for hand tracking)

Notes :
Make sure you have a working webcam connected to your system.
Ensure that your hand is well-illuminated and clearly visible to the webcam for accurate finger detection.
The images used for overlaying should be stored in a folder named FingersPics located in the same directory as the script.

The script will automatically resize the overlay images to fit the video feed.
That's it! You should now be able to count fingers and see the corresponding images overlaid on the video feed using the FingerCounter.py script.
