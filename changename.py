import os

os.chdir(r'C:\Users\student\change\SSAFY지원자')

for filename in os.listdir(".") :
    atfter_name = filename.replace("SAMSUNG","SSAFY")


    os.rename(filename, atfter_name)