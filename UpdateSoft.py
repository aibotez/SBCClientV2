import os,py7zr,requests,hashlib,time
import shutil,re
from py7zr import unpack_7zarchive
import multivolumefile

class Update():
    def __init__(self):
        self.path = '../SBCUPDATETEMP/'
    def un7z_file(self,zip_file,extract_dir):
        with py7zr.SevenZipFile(zip_file, 'r') as archive:
            fies = archive.getnames()
            files = [i for i in fies if 'UpdateSoft' not in fies and 'UserDB' not in fies]
            archive.extract(path=extract_dir,targets = files)

    def GetMaxVer(self,client = 'windows'):
        path = ''
        if client == 'windows':
            path = self.path
        felist = os.listdir(path)
        felist = [i for i in felist if 'SBC' in i]
        Vers = [i.split('_')[1] for i in felist]
        Versint = [int(i.replace('.', '')) for i in Vers]
        VerMax = Versint[-1]
        VerStrMax = ''
        for i in Vers:
            if int(i.replace('.', '')) == VerMax:
                VerStrMax = i
        return VerStrMax
    def OpenSoft(self):
        pass
    def Main(self):
        print('解压中...')
        VerMax = self.GetMaxVer()
        srcpath = '{}SBC_{}_.7z'.format(self.path,VerMax)
        self.un7z_file(srcpath,'./')
        os.system('start SBCclient0.exe &')

time.sleep(2)
Update = Update()
Update.Main()