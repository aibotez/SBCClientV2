import os,time,requests,json,hashlib

class DownFile():
    def __init__(self,ui,DownPath):
        self.ui = ui
        self.DownPath = DownPath
    def GetFileMd5(self,filename):
        if not os.path.isfile(filename):
            return
        myhash = hashlib.md5()
        f = open(filename,"rb")
        while True:
            b = f.read(2*1024*1024)
            if not b:
                break
            myhash.update(b)
        f.close()
        return myhash.hexdigest()
    def checkLoFile(self,info):
        exist = 0
        FileStart = 0
        fepath = self.DownPath + info['RoFilePathdif'] + '/' + info['FileMD5']
        if os.path.exists(fepath):
            exist = 1
            FileStart = os.path.getsize(fepath)
        return FileStart

    def checkDown(self,info):
        fepath = self.DownPath + info['RoFilePathdif'] + '/' + info['FileMD5']
        if info['FileMD5'] == self.GetFileMd5(fepath):
            return 1
        return 0

    def Down(self,info):
        downinfo = {
            'fename': info['FileName'],
            'fepath': info['RoFilePath'],
            'feseek': self.checkLoFile(info),
            'shareinfo': ''
        }
        data = {
            'downinfo': downinfo
        }
        fepath = self.DownPath + info['RoFilePathdif'] + '/' + info['FileMD5']
        if not os.path.isdir(self.DownPath + info['RoFilePathdif']):
            os.makedirs(self.DownPath + info['RoFilePathdif'])
        url_fileDown = 'http://' + self.ui.host + '/FileDown1/'
        r = requests.post(url_fileDown, data=json.dumps(data), headers=self.ui.SBCRe.headers, stream=True)
        with open(fepath, 'ab') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

        if self.checkDown(info):
            if os.path.exists(self.DownPath + info['RoFilePathdif'] + '/' + info['FileName']):
                os.remove(self.DownPath + info['RoFilePathdif'] + '/' + info['FileName'])
            os.rename(fepath,self.DownPath + info['RoFilePathdif'] + '/' + info['FileName'])
            return 1
        else:
            fepath = self.DownPath + info['RoFilePathdif'] + '/' + info['FileMD5']
            os.remove(fepath)
            return 0