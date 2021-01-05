# Imports
import cv2
import os

# Program Description
# This program will take a video file as an input, and will output a trimmed version of the file
# Speed is not a concern
# The frames that need to be deleted are one's with no footage of the recorded tests

# Algorithm Description
# This algorithm will iterate through each frame of the video
# Ex: Frame 1-3 need to be kept, frame 4-6 needs to be skipped, frame 7-8 kept
# Frame 1 - Frame 2 = Difference, keep frame 1
# Frame 2 - Frame 3 = Difference, keep frame 2
# Frame 4 - Frame 3 = Difference, keep frame 3
# Frame 5 - Frame 4 = No Difference, discard frame 4
# Frame 6 - Frame 5 = No difference, discard frame 5
# Frame 7 - Frame 6 = Difference, but frame 6 is last frame so discard
# ** Will need to check that if the previous frame was discarded, and there is now a frame with a difference,
# to discard that last frame **
# Frame 8 - Frame 7 = Difference, keep frame 7
# If last frame in whole video, keep it

def convertVideoToImages():
    # eventually, user will be able to select multiple videos at once to process
    print("test")
    # cap = cv2.VideoCapture('Add file path')
    # i = 0
    # # save each frame to its corresponding folder
    # while cap.isOpened():
    #     ret, frame = cap.read()
    #     if not ret:
    #         break
    #     cv2.imwrite('frame' + str(i) + '.jpg', frame)
    #     i += 1
    # cap.release()
    # cv2.destroyAllWindows()

def removeUnwantedFrames():
    # algorithm here
    print("Got here")

def makeVideo():
    # take all cleaned up frames and make into video
    print("Got here")

def main():
    print("Hello and Welcome to Video Cleaner!")
    print("Please input the file directory in convertVideoToFrames() method before running")
    input("Press Enter to start")

    print("Splitting video...")
    convertVideoToImages()
    print("Done")

    input("Press Enter to continue")

    print("Removing all unwanted frames...")
    removeUnwantedFrames()
    print("Done")

    print("Exporting into video, please don't halt the program until process is complete")
    makeVideo()
    print("Process Finished")


main()

