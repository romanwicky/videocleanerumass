# Imports
import cv2
import os
import glob
import shutil
import numpy as np
import tkinter as tk
from tkinter import filedialog


# ** IMPORTANT NOTICE **
# Please run this program as administrator, otherwise the cleanup process will not be able to delete the remaining files

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

# This class will hold the file location of the video to process, the path of the frames folder
# The path to the output video, and the frames per second of the video to process
class DirectoryInformation:
    def __init__(self, videotoprocess, pathtoframes, outputvideopath, fps):
        self.videotoprocess = videotoprocess
        self.pathtoframes = pathtoframes
        self.outputvideopath = outputvideopath
        self.fps = fps


# Instance of empty DirectoryInformation
mainDir = DirectoryInformation(None, None, None, None)


def convertVideoToImages(dirinfo):
    # eventually, user will be able to select multiple videos at once to process
    cap = cv2.VideoCapture(dirinfo.videotoprocess)
    framespersecond = cap.get(cv2.CAP_PROP_FPS)
    mainDir.fps = framespersecond

    path = dirinfo.pathtoframes
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


def removeUnwantedFrames(dirinfo):
    path = dirinfo.pathtoframes

    # set i = number of frames
    listofframes = os.listdir(path)  # dir is your directory path
    count = len(listofframes)
    # array of all frames that need to be deleted
    framestodelete = []

    # look at specific region in image, if it's black, then we want to delete it
    # This obviously isn't the best way to differenciate a frame we want to keep and want to delete,
    # especially if the resolution of the video feed changes, but because all the videos are the same size
    # it does the job well.
    for i in range(0, count - 1):
        img = cv2.imread(path + '/frame' + str(i) + '.jpg')
        region = img[250:300, 250:300]
        sumofpixels = np.sum(region)

        if sumofpixels == 0:
            framestodelete.append('frame' + str(i))

    # delete all frames from list
    for i in range(0, len(framestodelete)):
        os.remove(dirinfo.pathtoframes + str(framestodelete[i]) + '.jpg')


def makeVideo(dirinfo):
    videoname = filedialog.asksaveasfilename(
        parent=window,
        title="Save File",
        initialdir=mainDir.outputvideopath,
        filetypes=[
            ("All files", "*")])

    # take all cleaned up frames and make into video
    frame_array = []
    size = 0

    # Because of the way glob.glob works, need to have separate for looks for frame names
    # Here, assuming that the program won't exceed 999,999 total frames, and if it does get that large,
    # Just add another for loop with more ?'s.
    # so frame? = frame[0-9], frame?? = frame[10-99], frame??? = frame[100-999], etc
    for filename in glob.glob(dirinfo.pathtoframes + 'frame?.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        frame_array.append(img)

    for filename in glob.glob(dirinfo.pathtoframes + 'frame??.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        frame_array.append(img)

    for filename in glob.glob(dirinfo.pathtoframes + 'frame???.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        frame_array.append(img)

    for filename in glob.glob(dirinfo.pathtoframes + 'frame????.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        frame_array.append(img)

    for filename in glob.glob(dirinfo.pathtoframes + 'frame?????.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        frame_array.append(img)

    for filename in glob.glob(dirinfo.pathtoframes + 'frame??????.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        frame_array.append(img)

    for filename in glob.glob(dirinfo.pathtoframes + 'frame???????.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        frame_array.append(img)

    # Create a videowriter with size and framerate we want

    output = cv2.VideoWriter(videoname + '.avi', cv2.VideoWriter_fourcc(*'DIVX'), mainDir.fps,
                             size)

    # This loop adds each frame into the videowriter, creating the video

    for i in range(len(frame_array)):
        output.write(frame_array[i])

    # Release all the frames from memory
    output.release()

    # Delete the frames folder that contains all the frames, since the video is made and complete, we don't need it
    # anymore. This will sometimes throw an error about "Permission denied - read only", which will mean the folder
    # will have to be deleted manually. Most of the time this line works, as I ignore. Main functionality
    # of the program remains, and this will not stop the final video from being made properly.
    shutil.rmtree(mainDir.pathtoframes, ignore_errors=True, onerror=None)


def main():
    newpath = mainDir.outputvideopath + '/frames/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    mainDir.pathtoframes = newpath
    convertVideoToImages(mainDir)
    removeUnwantedFrames(mainDir)
    makeVideo(mainDir)


# Tkinter Stuff
window = tk.Tk()
window.geometry("500x300")


# Open File
def open_file():
    rep = filedialog.askopenfile(
        parent=window,
        title="Select TIFF File to Process",
        initialdir='/',
        filetypes=[
            ("All files", "*")])
    mainDir.videotoprocess = rep.name
    return rep.name


# Save file
def save_file():
    rep = filedialog.askdirectory(
        parent=window,
        title="Select Directory to Save File",
        initialdir='/'
    )
    mainDir.outputvideopath = rep
    return rep


frame_1 = tk.Frame()
frame_2 = tk.Frame()
frame_3 = tk.Frame()
button = tk.Button(
    master=frame_1,
    text="Select File",
    font="Nunito",
    width=15,
    height=5,
    bg="#32a889",
    fg="black",
    command=lambda: open_file()
)
button2 = tk.Button(
    master=frame_2,
    text="Select Destination",
    font="Nunito",
    width=15,
    height=5,
    bg="#32a889",
    fg="black",
    command=lambda: save_file()
)
button3 = tk.Button(
    master=frame_2,
    text="Process",
    font="Nunito",
    width=15,
    height=5,
    bg="#32a889",
    fg="black",
    command=lambda: main()
)
frame_1.pack()
frame_2.pack()
frame_3.pack()
button.pack()
button2.pack()
button3.pack()
window.mainloop()
