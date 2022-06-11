from pydub import AudioSegment
import os
import re
def convert(path,filename):
    sound = AudioSegment.from_file(path)
    # print("----------Before Conversion--------")
    # print("Frame Rate", sound.frame_rate)
    # print("Channel", sound.channels)
    # print("Sample Width",sound.sample_width)
    try:
        # Change Frame Rate
        sound = sound.set_frame_rate(48000)
        # Change Channel
        sound = sound.set_channels(1)
        # Change Sample Width
        sound = sound.set_sample_width(2)
        # Export the Audio to get the changed content
        sound.export(path, format ="wav")
    except:
        print("----------Before Conversion--------")
        print("Frame Rate", sound.frame_rate)
        print("Channel", sound.channels)
        print("Sample Width",sound.sample_width)
        print(path)
        sound = sound.set_frame_rate(48000)
        # Change Channel
        sound = sound.set_channels(1)
        # Change Sample Width
        sound = sound.set_sample_width(2)
        # Export the Audio to get the changed content
        sound.export(path, format ="wav")

for root, dirs, files in os.walk("/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_HINDI_SPEECH_DATA"):
    for filename in files:
        #print(filename)
        convert(os.path.join(root, filename),filename)
    # for dirname in dirs:
    #     print(dirname)
    #     #print(str(os.path.join(root, dirname))