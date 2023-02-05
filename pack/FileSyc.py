import os,time,shutil,requests
from pack import DBManager
import threading,json,hashlib
from pack import UpFile2SBC



def str_trans_to_md5(src):
    src = src.encode("utf-8")
    myMd5 = hashlib.md5()
    myMd5.update(src)
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest
def getfileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename, "rb")
    while True:
        b = f.read(2*1024*1024)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()
class FileSyc():
    def __init__(self,ui):
        self.ui = ui
        self.dbManager = DBManager.DBManager()
        self.UpFile2SBCs = UpFile2SBC.UpFile2SBC(self.ui)

    def GetClientInfo(self):
        self.ClientInfo = self.dbManager.GetClientSetting()


    def GetAllFilesFromSBC(self,path):
        data = {
            'path': path
        }
        FilesRo = self.ui.SBCRe.GetAllFilesSyc(json.dumps(data))
        return FilesRo
    def GetAllFilesfromFolder(self,path):
        Files = {}
        for root, dirs, files in os.walk(path):
            root += '/'
            root = root.replace('\\', '/').replace('//', '/')
            fapath = root.replace(path, '')
            if '__pycache__' not in fapath:
                for i in files:
                    fepath = path + fapath + i
                    FileInfo = {}
                    FileInfo['rofapath'] = self.ClientInfo['BackupRoPath'][0:-1] + os.path.dirname(fepath).replace(path[0:-1],'/')
                    FileInfo['fename'] = os.path.basename(fepath)
                    FileInfo['fepath'] = fepath
                    FileInfo['rofepath'] = self.ClientInfo['BackupRoPath'][0:-1] + fepath.replace(path,'/')
                    FileInfo['size'] = os.path.getsize(fepath)
                    FileInfo['date'] = os.stat(fepath).st_mtime
                    # FileInfo['fepath1'] = fepath.replace(path,'/')
                    Files[str_trans_to_md5(FileInfo['rofepath'])] = FileInfo
        return Files


    def SycMode1act(self):
        while True:
            print('Mode1 Start Scan')
            if self.ClientInfo['BackupLoPath'] and self.ClientInfo['BackupRoPath']:
                FilesLo = self.GetAllFilesfromFolder(self.ClientInfo['BackupLoPath'])
                FilesRo = self.GetAllFilesFromSBC(self.ClientInfo['BackupRoPath'])
                for i in FilesLo:
                    if i not in FilesRo or FilesLo[i]['date']>FilesRo[i]['date']:
                        info ={}
                        info['LoFilePath'] = FilesLo[i]['fepath']
                        info['RoFilePath'] = FilesLo[i]['rofepath']
                        info['FileSize'] = FilesLo[i]['size']
                        info['RoFileFaPath'] = FilesLo[i]['rofapath']
                        info['FileName'] = FilesLo[i]['fename']
                        info['LoMD5'] = getfileMd5(FilesLo[i]['fepath'])
                        checkinfo = self.ui.SBCRe.SycCheckSBCFile(json.dumps(info))
                        info['FileSeekStart'] = checkinfo['FileStart']
                        self.UpFile2SBCs.UpFile(info)
                        print(FilesLo[i]['rofepath'],checkinfo)
                        time.sleep(1)
                    else:
                        print('Have',FilesLo[i]['rofepath'])
            time.sleep(self.timeFre)
    def SycMode3act(self):
        while True:
            print('Mode3 Start Scan')
            if self.ClientInfo['BackupLoPath'] and self.ClientInfo['BackupRoPath']:
                FilesLo = self.GetAllFilesfromFolder(self.ClientInfo['BackupLoPath'])
                FilesRo = self.GetAllFilesFromSBC(self.ClientInfo['BackupRoPath'])
                for i in FilesRo:
                    if i not in FilesLo or FilesRo[i]['date'] > FilesLo[i]['date']:
                        pass
            time.sleep(self.timeFre)
    def SycMode2act(self):
        while True:
            print('Mode2 Start Scan')
            if self.ClientInfo['BackupLoPath'] and self.ClientInfo['BackupRoPath']:
                FilesLo = self.GetAllFilesfromFolder(self.ClientInfo['BackupLoPath'])
                FilesRo = self.GetAllFilesFromSBC(self.ClientInfo['BackupRoPath'])
                for i in FilesRo:
                    if i not in FilesLo or FilesRo[i]['date'] > FilesLo[i]['date']:
                        info ={}
                        # info['LoFilePath'] = FilesLo[i]['fepath']
                        # info['RoFilePath'] = FilesLo[i]['rofepath']
                        # info['FileSize'] = FilesLo[i]['size']
                        # info['RoFileFaPath'] = FilesLo[i]['rofapath']
                        # info['FileName'] = FilesLo[i]['fename']
            time.sleep(self.timeFre)
    def GetSycFre(self):
        SycFre = self.ClientInfo['SycFre']
        self.timeFre = 0
        if not SycFre:
            return
        if '5分钟' in SycFre:
            self.timeFre = 5*60
        elif '10分钟' in SycFre:
            self.timeFre = 10 * 60
        elif '30分钟' in SycFre:
            self.timeFre = 30 * 60
        elif '1小时' in SycFre:
            self.timeFre = 60 * 60
        elif '2小时' in SycFre:
            self.timeFre = 2 * 60 * 60

    def SycMode3(self):
        self.GetSycFre()
        t = threading.Thread(target=self.SycMode3act)
        t.setDaemon(True)
        t.start()
    def SycMode2(self):
        self.GetSycFre()
        t = threading.Thread(target=self.SycMode2act)
        t.setDaemon(True)
        t.start()
    def SycMode1(self):
        self.GetSycFre()
        t = threading.Thread(target=self.SycMode1act)
        t.setDaemon(True)
        t.start()
    def SycMain(self):
        self.GetClientInfo()
        if not self.ClientInfo['SycOpen']:
            return
        if self.ClientInfo['SycMode'] == 1:
            self.SycMode1()
        elif self.ClientInfo['SycMode'] == 2:
            self.SycMode2()
        elif self.ClientInfo['SycMode'] == 3:
            pass