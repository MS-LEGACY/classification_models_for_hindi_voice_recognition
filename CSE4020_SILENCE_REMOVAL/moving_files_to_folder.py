import os
import shutil
import re
list_names = []
for root,dirs,files in os.walk("/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES",topdown=True):
    for name in files:
        if (re.match(r"[a-zA-Z]+_1",name)):
            list_names.append(re.match(r"[a-zA-Z]+",name).group(0))
# for root,dirs,files in os.walk("/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_TESTING",topdown=True):
#     for name in files:
#         if (re.match(r"[a-zA-Z]+_6",name)):
#             list_names.append(re.match(r"[a-zA-Z]+",name).group(0))
print(len(list_names))
list_names.sort()
print(list_names)
# shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# for i in list_names:
#     os.mkdir("/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/"+i)
# for i in list_names:
#     os.mkdir("/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_TESTING/"+i)

# for i in list_names:
#     for root,dirs,files in os.walk("/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES",topdown=True):
#         for name in files:
#             if (re.match(r"%s\_[0-5]" % i,name)):
#                 #shutil.move
#                 print(os.path.join(root,name))#,"/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/"+i+"/"+str(name))
                
# for i in list_names:
#     for root,dirs,files in os.walk("/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_TESTING",topdown=True):
#         for name in files:
#             if (re.match(r"%s\_6" % i,name)):
#                 shutil.move(os.path.join(root,name),"/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_TESTING/"+i+"/"+str(name))
                