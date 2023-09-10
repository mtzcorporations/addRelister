import os

class fileUploader:
    def __init__(self):
        #self.path=os.path.dirname(os.path.abspath(__file__)) + "\\Fotografije\\"
        self.path="C:\\Work\\Bolha\\Fotografije\\"
        self.name = "nic"
        self.pictures=[]
    def listFilesForName(self,Naslov):
        self.name = self.path + Naslov
        files=os.listdir(self.name)
        for f in files:
            fullN=self.name + "\\" + f
            self.pictures.append(fullN)
        return  self.pictures
#path="Fotografije/Asus tuf A15 ryzen 7 5800h, Rtx 3060, 16Gb ram, 512 ssd, 144hz zaslon"
#dir_list = os.listdir(path)
#for file in dir_list:
 #   name
#naslov="4x Lenovo m73  ohišje DVD enota + 1x napajalnik"

#files=fileUploader().listFilesForName(naslov)
#print(files)
