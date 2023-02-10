import os,time,requests,json
from requests_toolbelt import MultipartEncoder,MultipartEncoderMonitor

class UpFile2SBC():
    def __init__(self,ui):
        self.ui = ui
        self.s = requests.Session()
    def chunked_file_reader(self,info,block_size=60*1024 * 1024):
        """生成器函数：分块读取文件内容
        """
        file = info['LoFilePath']
        FileSeekStart = info['FileSeekStart']
        with open(file, 'rb') as f:
            f.seek(FileSeekStart,os.SEEK_SET)
            while True:
                c = f.read(block_size)
                if c:
                    yield c
                else:
                    break
    def CheckRoFile(self,info):
        url = 'http://' + self.ui.host + '/CheckFile/'
        data = info
        res = self.s.post(url, data=data,headers=self.ui.SBCRe.headers)
        return json.loads(res.text)
    def UpFile(self,info):

        r = 'error'
        RoCheckFile = self.CheckRoFile(info)
        if RoCheckFile['exist']:
            return 'finsh'
        FileSeekStart = RoCheckFile['FileStart']
        info['FileSeekStart'] = FileSeekStart

        for chunk in self.chunked_file_reader(info):
            e = MultipartEncoder(
                fields={
                    'FileInfo': json.dumps(info),
                    'file': (info['FileName'], chunk, 'application/octet-stream'),  # 文件1
                }
            )
            # url_fileUp = 'http://' + self.ui.host + '/SycFileUp/'
            url_fileUp = 'http://' + self.ui.host + '/Upfile1/'
            m = MultipartEncoderMonitor(e)
            headers = self.ui.SBCRe.headers
            headers1 = {}
            headers1['Cookie'] = headers['Cookie']
            headers1['Content-Type'] = m.content_type
            r = self.s.post(url_fileUp, data=m, headers=headers1).text
        return r
