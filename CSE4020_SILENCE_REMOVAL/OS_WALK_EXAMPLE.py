import os
print("Hello World")
for root, dirs, files in os.walk("/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_HINDI_SPEECH_DATA"):
    for filename in files:
        #print(filename)
        print(os.path.join(root, filename),"----",root)
    for dirname in dirs:
        print(dirname)
        #print(str(os.path.join(root, dirname)))s