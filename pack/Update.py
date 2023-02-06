import requests,os,json,hashlib,sys,threading
import subprocess

class Update():

    def __init__(self,ui):
        self.ui = ui
    def GetFileMd5(self,filename):
        if not os.path.isfile(filename):
            return
        myhash = hashlib.md5()
        f = open(filename, "rb")
        while True:
            b = f.read(2 * 1024 * 1024)
            if not b:
                break
            myhash.update(b)
        f.close()
        return myhash.hexdigest()
    def GetRoVersion(self):
        url = 'http://'+self.ui.host+'/GetCurVer/'
        data = { 'client':'windows'}
        res = requests.post(url,data=data).text
        res = json.loads(res)
        return res

    def Downact(self,signalUpdateProgress,signalexit):
        t = threading.Thread(target=self.Downact1,args=(signalUpdateProgress,signalexit,))
        t.setDaemon(True)
        t.start()

    def Downact1(self,signalUpdateProgress,signalexit):
        data = {'client': 'windows'}
        url_fileDown = 'http://' + self.ui.host + '/DownClient/'
        r = requests.post(url_fileDown, data=data,stream=True)
        if not os.path.isdir('../SBCUPDATETEMP'):
            os.mkdir('../SBCUPDATETEMP')
        fepath = '../SBCUPDATETEMP/{}'.format(r.headers['FileName'])

        DownSize = 0
        TotlSize = int(r.headers['size'])
        with open(fepath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    DownSize += len(chunk)
                    progess = str(int(DownSize/TotlSize*100))
                    signalUpdateProgress.emit(progess+'%')
                    f.write(chunk)
        LoFIleMD5 = self.GetFileMd5(fepath)
        if LoFIleMD5 == r.headers['FileMd5']:
            os.system('start UpdateSoft.py &')
            # subprocess.Popen('start D:/项目/SBCClientV2/UpdateSoft.py')
            signalexit.emit()
            # sys.exit()
        else:
            os.remove(fepath)