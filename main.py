# Imports
import cv2
import os
import glob
import numpy as np

# Program Description
# This program will take a video file as an input, and will output a trimmed version of the file
# Speed is not a concern
# The frames that need to be deleted are one's with no footage of the recorded tests

# Algorithm Description

# Algo 1

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

# Algo 2

# This one is much simpler, since we know for sure that a if a certain area of the screen
# is Completly black, then that is a frame we want to discard, hence the "No picture" seconds
# of the video. 
# Open file with cv2, crop it to [250:300, 250:300] [y1, y2], [x1, x2] where
# (x1,y1) is the top left of the image, the (x2,y2) is the bottom right
# By cropping and getting this specific area, and summing up the pixel values of the image
# if the value is = 0, then that is a frame we want to discard
# This removes any issues that might happen with double iterations, and deleting files as the algorithm
# works


def convertVideoToImages():
    # eventually, user will be able to select multiple videos at once to process
    cap = cv2.VideoCapture('C:/Users/Roman/Desktop/videos/vid1.avi')
    path = 'C:/Users/Roman/Desktop/videos/frames'
    i = 0
    # save each frame to its corresponding folder
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(os.path.join(path, 'frame' + str(i) + '.jpg'), frame)
        i += 1
    cap.release()
    cv2.destroyAllWindows()


def removeUnwantedFrames():
    path = 'C:/Users/Roman/Desktop/videos/frames/'

    # set i = number of frames
    listofframes = os.listdir(path)  # dir is your directory path
    count = len(listofframes)
    # print(count)
    # list of all frames that need to be deleted
    framestodelete = []

    # look at specific region in image, if it's black, then we want to delete it
    for i in range(0, count - 1):
        img = cv2.imread(path + 'frame' + str(i) + '.jpg')
        region = img[250:300, 250:300]
        sumofpixels = np.sum(region)

        if sumofpixels == 0:
            framestodelete.append('frame' + str(i))

    # delete all frames from list
    for i in range(0, len(framestodelete)):
        os.remove('C:/Users/Roman/Desktop/videos/frames/' + str(framestodelete[i]) + '.jpg')
        print(str(framestodelete[i]))


def makeVideo():
    # take all cleaned up frames and make into video
    frame_array = []
    for filename in glob.glob('C:/Users/Roman/Desktop/videos/frames/*.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        frame_array.append(img)

    output = cv2.VideoWriter('C:/Users/Roman/Desktop/videos/frames/trimmed.avi', cv2.VideoWriter_fourcc(*'DIVX'), 20, size)

    for i in range(len(frame_array)):
        output.write(frame_array[i])

    output.release()


def main():
    newpath = r'C:\Users\Roman\Desktop\videos\frames'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    print("Please input the file directory in convertVideoToFrames() method before running")
    input("Press Enter to start")

    print("Splitting video...")
    convertVideoToImages()
    print("Done")

    print("Removing all unwanted frames...")
    removeUnwantedFrames()
    print("Done")

    print("Exporting into video, please don't halt the program until process is complete")
    makeVideo()
    print("Process Finished")


main()
