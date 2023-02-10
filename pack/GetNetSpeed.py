from win32com.client import GetObject,Dispatch
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject, pyqtSignal
import time,threading
# 定义命名空间是cimv2
wmi = GetObject('winmgmts:/root/cimv2')
# 创建 SWbemRefresher 刷新器对象
objRefresher = Dispatch('WbemScripting.SWbemRefresher')
# 使用从 Win32_PerfFormattedData派生的预计算数据类 Win32_PerfFormattedData_Tcpip_Networkinterface
# 要注意的是调用了AddEnum之后需要再调用objRefresher.Refresh()来获取初始性能数据，下方因为在循环开头已经做了这步了所以跳过。
NetInterfaces = objRefresher.AddEnum(wmi,"Win32_PerfFormattedData_Tcpip_Networkinterface")




def size_format(size):
    if size < 1024:
        return '%i' % size + 'B'
    elif 1024 <= size < 1024 * 1024:
        return '%.1f' % round(float(size / 1024),2) + 'KB'
    elif 1024 * 1024 <= size < 1024 * 1024 * 1024:
        return '%.1f' % round(float(size / (1024 * 1024)),2) + 'MB'
    elif 1024 * 1024 * 1024 <= size < 1024 * 1024 * 1024 * 1024:
        return '%.1f' % round(float(size / (1024 * 1024 * 1024)),2) + 'GB'
    elif 1024 * 1024 * 1024 * 1024 <= size:
        return '%.1f' % float(size / (1024 * 1024 * 1024 * 1024)) + 'TB'
class NetSpeed(QObject):
    signalUpdateNetShow = pyqtSignal(list)
    def __init__(self,ui):
        super().__init__()
        self.ui = ui
        self.signalUpdateNetShow.connect(self.Updateact)
        self.UpdateNetShow()

    def GetSpeed(self):
        UpSpeed = 0
        DownSpeed = 0
        objRefresher.Refresh()
        # 循环访问刷新器集合对象
        for NetInterface in NetInterfaces.ObjectSet:
            UpSpeed += int(NetInterface.BytesSentPersec)
            DownSpeed += int(NetInterface.BytesReceivedPersec)
        return [DownSpeed,UpSpeed]
    def Updateact(self,info):
        self.ui.FloatWind.label_10.setText(size_format(info[1])+'/S')
        self.ui.FloatWind.label_11.setText(size_format(info[0])+'/S')

    def ThreadRun(self):
        while True:
            info = self.GetSpeed()
            self.signalUpdateNetShow.emit(info)
            time.sleep(1)

    def UpdateNetShow(self):
        t = threading.Thread(target=self.ThreadRun)
        t.setDaemon(True)
        t.start()
        # self.ui.FloatWind.