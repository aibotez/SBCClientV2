import os,py7zr

class Update():
    def __init__(self):
        pass

    def GetRoVersion(self):
        return 201

    def GetLoVersion(self):
        felist = os.listdir('Ver/')
        Vers = [int(i.replace('.','')) for i in felist]
        Vers.sort()
        Ver = Vers[-1]
        return Ver

    def DownSoft(self):
        pass

    def un_zip(self,file_name, dst):
        archive = py7zr.SevenZipFile(file_name, mode='r')
        archive.extractall(path=dst)
        archive.close()

    def OpenSoft(self):
        pass

    def Main(self):
        pass
Update = Update()
Update.GetLoVersion()