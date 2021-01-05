# Imports

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
