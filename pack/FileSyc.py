import os,time,shutil,requests
from pack import DBManager
import threading,json,hashlib
from pack import UpFile2SBC
from pack import DownFIleFromSBC
from pynput import keyboard
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import *





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
class FileSyc(QObject):
    signalUpdateProgress = pyqtSignal(list)
    signalScan = pyqtSignal(int)
    signalUpDow = pyqtSignal(int)
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
        self.dbManager = DBManager.DBManager()
        self.UpFile2SBCs = UpFile2SBC.UpFile2SBC(self.ui)
        self.signalUpdateProgress.connect(self.UpdateProgress)
        self.signalScan.connect(self.Scancon)
        self.signalUpDow.connect(self.SUpDownCon)
        self.dbManager = DBManager.DBManager()

    def SUpDownCon(self,judge):
        if judge:
            self.ui.FloatWind.label_8.setText('↑')
        else:
            self.ui.FloatWind.label_8.setText('↓')
    def Scancon(self,judge):
        if judge:
            self.ui.FloatWind.label_9.setPixmap(QtGui.QPixmap('img/scan.png'))
            self.ui.FloatWind.label_9.setScaledContents(True)
        else:
            self.ui.FloatWind.label_9.setPixmap(QtGui.QPixmap(""))
    def UpdateProgress(self,progess):
        Uped = str(progess[0])
        total = str(progess[-1])
        self.ui.FloatWind.label_6.setText(Uped)
        self.ui.FloatWind.label_7.setText(total)
    def on_press(self,key):
        print(key)
    def Listen(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


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
            if '__pycache__' not in fapath and '~$' not in fapath:
                for i in files:
                    try:
                        fepath = path + fapath + i
                        FileInfo = {}
                        FileInfo['rofapath'] = self.ClientInfo['BackupRoPath'][0:-1] + os.path.dirname(fepath).replace(path[0:-1],'/')
                        FileInfo['fename'] = os.path.basename(fepath)
                        FileInfo['fepath'] = fepath
                        FileInfo['rofepath'] = self.ClientInfo['BackupRoPath'][0:-1] + fepath.replace(path,'/')
                        FileInfo['size'] = os.path.getsize(fepath)
                        FileInfo['date'] = os.stat(fepath).st_mtime
                        FileInfo['filemd5'] = getfileMd5(fepath)
                        # FileInfo['fepath1'] = fepath.replace(path,'/')
                        Files[str_trans_to_md5(FileInfo['rofepath'])] = FileInfo
                    except Exception as e:
                        print(e)
                        continue
        return Files


    def SycMode1act_(self,FilesLo,FilesRo):
        # loFilesdb = self.dbManager.GetSycRecordAll()
        # FilesRo = loFilesdb
        # dbFilesWaitDel = [loFilesdb[i] for i in loFilesdb if i not in FilesLo]
        # self.dbManager.DelSycRecords(dbFilesWaitDel)
        FilesLo_ = [i for i in FilesLo if i not in FilesRo or FilesLo[i]['filemd5'] != FilesRo[i]['filemd5']]
        FileWaits = [i for i in FilesLo_ if i not in FilesRo or FilesLo[i]['date'] > FilesRo[i]['date']]
        # dbFilesWaitUpdate = []
        # dbFilesWaitAdd = []
        self.signalUpdateProgress.emit([0,len(FileWaits)])
        self.signalUpDow.emit(1)
        SycUped = 0
        for i in FileWaits:
            try:
                # print(FilesLo[i]['filemd5'],FilesRo[i]['filemd5'])
                info = {}
                info['LoFilePath'] = FilesLo[i]['fepath']
                info['CurPath'] = FilesLo[i]['rofapath']+'/'
                info['RoFilePath'] = FilesLo[i]['rofepath']
                info['FileSize'] = FilesLo[i]['size']
                info['RoFileFaPath'] = FilesLo[i]['rofapath']
                info['FileName'] = FilesLo[i]['fename']
                info['LoMD5'] = FilesLo[i]['filemd5']
                info['FileMd5'] = FilesLo[i]['filemd5']
                info['webkitRelativePath'] = ''
                # checkinfo = self.ui.SBCRe.SycCheckSBCFile(json.dumps(info))
                # info['FileSeekStart'] = checkinfo['FileStart']

                res = self.UpFile2SBCs.UpFile(info)
                # if res =='finsh':
                #     if i in FilesRo:
                #         dbFilesWaitUpdate.append(FilesLo[i])
                #     else:
                #         dbFilesWaitAdd.append(FilesLo[i])

                SycUped += 1
                self.signalUpdateProgress.emit([SycUped, len(FileWaits)])
            except Exception as e:
                self.ui.OutErrorInfo(str(e) + '#' + FilesLo[i]['fepath'])
                continue
            time.sleep(0.2)
        # self.dbManager.UpdataSycRecords(dbFilesWaitUpdate)
        # self.dbManager.AddSycRecords(dbFilesWaitAdd)
        self.signalUpdateProgress.emit([0, 0])

    # def judgeloFile(self,FilesLo):
    #     loFilesdb = self.dbManager.creatSycFileRecords()
    #     FileWaits = [i for i in FilesLo if i not in loFilesdb or FilesLo[i]['date'] > loFilesdb[i]['date']]
    #     self.SycMode1act_(FileWaits,loFilesdb,FilesLo)

    def SycMode1act(self):
        while True:
            print('Mode1 Start Scan')
            if self.ClientInfo['BackupLoPath'] and self.ClientInfo['BackupRoPath']:
                self.signalScan.emit(1)
                FilesLo = self.GetAllFilesfromFolder(self.ClientInfo['BackupLoPath'])
                FilesRo = self.GetAllFilesFromSBC(self.ClientInfo['BackupRoPath'])
                # for i in FilesRo:
                #     # print(FilesRo[i]['fepath'])
                #     if '/home/新建' in FilesRo[i]['fepath']:
                #         print(FilesRo[i]['fepath'])
                # return
                # print(FilesRo)
                # print(FilesLo)
                self.signalScan.emit(0)
                self.SycMode1act_(FilesLo,FilesRo)

            time.sleep(self.timeFre)
            # time.sleep(10)


    def SycMode3act(self):
        while True:
            print('Mode3 Start Scan')
            if self.ClientInfo['BackupLoPath'] and self.ClientInfo['BackupRoPath']:
                self.signalScan.emit(1)
                FilesLo = self.GetAllFilesfromFolder(self.ClientInfo['BackupLoPath'])
                FilesRo = self.GetAllFilesFromSBC(self.ClientInfo['BackupRoPath'])
                self.signalScan.emit(0)
                self.SycMode1act_(FilesLo,FilesRo)
                self.SycMode2act_(FilesLo,FilesRo)

            # time.sleep(10)
            time.sleep(self.timeFre)

    def SycMode2act_(self,FilesLo,FilesRo):
        FilesRo_ = [i for i in FilesRo if i not in FilesLo or FilesLo[i]['filemd5'] != FilesRo[i]['filemd5']]
        FileWaits = [i for i in FilesRo_ if i not in FilesLo or FilesRo[i]['date'] > FilesLo[i]['date']]
        self.signalUpdateProgress.emit([0,len(FileWaits)])
        self.signalUpDow.emit(0)
        SycUped = 0
        for i in FileWaits:
            try:
                info = {}
                # info['LoFilePath'] = FilesLo[i]['fepath']
                info['RoFilePath'] = FilesRo[i]['fepath']
                # info['FileSize'] = FilesLo[i]['size']
                info['RoFilePathdif'] = FilesRo[i]['fapath1']
                info['FileName'] = FilesRo[i]['fename']
                info['FileMD5'] = FilesRo[i]['filemd5']
                self.DownFileFromSBC.Down(info)
                SycUped += 1
                self.signalUpdateProgress.emit([SycUped, len(FileWaits)])
            except Exception as e:
                self.ui.OutErrorInfo(str(e) + '#' + FilesRo[i]['fepath'])
                continue
            time.sleep(0.2)
        self.signalUpdateProgress.emit([0, 0])
    def SycMode2act(self):
        while True:
            print('Mode2 Start Scan')
            if self.ClientInfo['BackupLoPath'] and self.ClientInfo['BackupRoPath']:
                self.signalScan.emit(1)
                FilesLo = self.GetAllFilesfromFolder(self.ClientInfo['BackupLoPath'])
                FilesRo = self.GetAllFilesFromSBC(self.ClientInfo['BackupRoPath'])
                self.signalScan.emit(0)
                self.SycMode2act_(FilesLo,FilesRo)

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
        # t = threading.Thread(target=self.Listen)
        # t.setDaemon(True)
        # t.start()
        self.GetClientInfo()
        self.DownFileFromSBC = DownFIleFromSBC.DownFile(self.ui,self.ClientInfo['BackupLoPath'])
        if not self.ClientInfo['SycOpen']:
            return
        if self.ClientInfo['SycMode'] == 1:
            self.SycMode1()
        elif self.ClientInfo['SycMode'] == 2:
            self.SycMode2()
        elif self.ClientInfo['SycMode'] == 3:
            self.SycMode3()