import os,time

class TransFileManager():
    def __init__(self,DownRecordFile,UpRecordFile,FinishRcordFile):
        self.DownRecordFile = DownRecordFile
        self.UpRecordFile = UpRecordFile
        self.FinishRcordFile = FinishRcordFile


    def AddDownRecord(self,DownInfo):
        while True:
            try:
                with open(self.DownRecordFile,'a+') as f:
                    f.write(DownInfo['FileName']+'\a'+DownInfo['FileMd5']+'\a'+DownInfo['FilePath']+'\a'+DownInfo['RoFilePath']+'\n')
                break
            except Exception as e:
                print('TranspFile')
                print(e)

    def GetDownRecord(self):
        DownInfo = []
        with open(self.DownRecordFile,'r') as f:
            Rd = f.readline()
        if Rd:
            for i in Rd:
                if len(Rd) >2:
                    DownInfoi = i.split('\a')
                    DownInfo.append({'FileName':DownInfoi[0],'FileMd5':DownInfoi[1],'FilePath':DownInfoi[2],'RoFilePath':DownInfoi[3]})
        return DownInfo

