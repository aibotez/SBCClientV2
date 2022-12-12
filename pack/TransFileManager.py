import os,time
from . import DBManager
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class TransFileManager():
    # def __init__(self,DownRecordFile,UpRecordFile,FinishRcordFile):
    def __init__(self,MainUi):
        self.dbManager = DBManager.DBManager()
        self.MainUi = MainUi
        # self.DownRecordFile = DownRecordFile
        # self.UpRecordFile = UpRecordFile
        # self.FinishRcordFile = FinishRcordFile



    def AddDownRecord(self,DownInfo):
        AdW = self.dbManager.AddUserDownRecord(DownInfo)
        if AdW == 'Have':
            reply = QMessageBox.question(self.MainUi,'提示', '该文件正在下载，重新下载？',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                pass

        # while True:
        #     try:
        #         with open(self.DownRecordFile,'a+') as f:
        #             f.write(DownInfo['FileName']+'\t'+DownInfo['FileMd5']+'\t'+DownInfo['FilePath']+'\t'+DownInfo['RoFilePath']+'\n')
        #         break
        #     except Exception as e:
        #         print('TranspFile')
        #         print(e)

    def GetDownRecord(self):
        DownInfo = self.dbManager.GetUserDownRecord()
        # DownInfo = []
        # with open(self.DownRecordFile,'r') as f:
        #     Rd = f.readline()
        # if Rd:
        #     for i in Rd:
        #         if len(Rd) >2:
        #             DownInfoi = i.split('\a')
        #             DownInfo.append({'FileName':DownInfoi[0],'FileMd5':DownInfoi[1],'FilePath':DownInfoi[2],'RoFilePath':DownInfoi[3]})
        return DownInfo

