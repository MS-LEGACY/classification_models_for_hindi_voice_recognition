from pyAudioAnalysis import MidTermFeatures as aF
import os
import numpy as np
import pandas as pd 

dirs = ['/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AliaBhatt', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/NanaPatekar', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Ayush', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/NikhilNair', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/VijayKashyap', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/PrateekSoni', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Nandini', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AbhishekSingh', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/RishiGarg', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AbhishekGupta', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AbhishekJha', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/SnehaSoni', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/YatiSharma', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/MohitChandani', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/SiddharthSingh', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Aadiksha', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/SalmanKhan', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AartiDa', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AmitSingh', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/IrfanKhan', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Eknath', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Govinda', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/RachitKhare', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/SrishtiBhatnagar', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/SanjayDutt', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/SanyamGarg', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/NutanBhatnagar', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/TraptiDa', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AlokSharma', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/SavanA', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Arindam', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/PraveenChaturvedi', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/JyotiRathore', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/SiddharthPandey', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/MayankTripathi', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AbhinandanBhatnagar', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AnupamKher', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/RahulGarg', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/DhirendraYadav', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Abhay', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/LuvkushVerma', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/BrishtiGanguly', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/SunnyDeol', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/PalakSharma', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AnweshaMohanty', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/ShubhamChabra', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Suman', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AkanshaSingh', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AdityaBajpayee', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AditiGiri', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/ShivamY', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/JyotiDa', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/SumitPandey', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Rupanshi', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Prabhakar', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Meher', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/ApporvaBajpayee', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AnamAquil', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AdityaMishra', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/DebomitraDas', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AlokMishra', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/VaishanaviGupta', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/BhartiYadav', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/NavneetKhurana', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Rishika', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/VarshaShukla', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/SiddhiTondon', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Kapisharma', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Shivani', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Vaibhav', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/ShubhiTiwari', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AkshayKumar', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/JyotiShukla', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/RajatSharma', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/MayankAnand', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/YogiAdityanath', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/ShishirMishra', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/ShahrukhKhan', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AkshajKul', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/NarendraModi', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AmanTripathi', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/VirendraGarg', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Navnidhi', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/NikhilAnil', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AamirKhan', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/RachnaSharma', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/PrayagMishra', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/SoumyaBhaduria', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/ShivamPujara', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/DivyanshKul', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AshishPatel', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/GurnoorKaur', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/VirartKohli', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Rutvi', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/SomyaSingh', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/Raghavi', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/ShikhaNamdev', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/ShivangiGarg', '/home/mrigank/Public/Fall_Semester_2021_22/CSE4020_MACHINE_LEARNING/CSE4020_PROJECT/CSE4020_SILENCE_REMOVAL/SILENCE_REMOVED_FILES/AbhimanyuBaghel']
class_names = [os.path.basename(d) for d in dirs]
m_win, m_step, s_win, s_step = 1, 1, 0.1, 0.05 
features = {}
for d in dirs:
    f, files, fn = aF.directory_feature_extraction(d, m_win, m_step,s_win, s_step) 
    features[str(os.path.basename(d))]=f
for i in features:
    print(i)
# features_data_frame = pd.DataFrame(columns=fn)
li = []
print(features)
for i in features:
    audio_files_array_of_dir = features[i]
    row = []
    for j in audio_files_array_of_dir:
        j.append(i)
        li.append(j)
    print(audio_files_array_of_dir)
for i in li:
    print(i)
        



