import wmi #wmi依赖pywin32,python3.5以上版本安装pywin32需要手动安装
s = wmi.WMI()
#cpu 序列号
def get_CPU_info():
    cpu = []
    cp = s.Win32_Processor()
    for u in cp:
        cpu.append(
            {
                "Name": u.Name,
                "Serial Number": u.ProcessorId,
                "CoreNum": u.NumberOfCores
            }
        )
    return cpu
#硬盘序列号
def get_disk_info():
    disk = []
    for pd in s.Win32_DiskDrive():
        disk.append(
            {
                "Serial": s.Win32_PhysicalMedia()[0].SerialNumber.lstrip().rstrip(), # 获取硬盘序列号，调用另外一个win32 API
                "ID": pd.deviceid,
                "Caption": pd.Caption,
                "size": str(int(float(pd.Size)/1024/1024/1024))+"G"
            }
        )
    return disk
#mac 地址（包括虚拟机的）
def get_network_info():
    network = []
    for nw in s.Win32_NetworkAdapterConfiguration ():  # IPEnabled=0
        if nw.MACAddress != None:
            network.append(
                {
                    "MAC": nw.MACAddress,  # 无线局域网适配器 WLAN 物理地址
                    "ip": nw.IPAddress
                }
            )
    return network

#主板序列号
def get_mainboard_info():
    mainboard = []
    for board_id in s.Win32_BaseBoard():
        mainboard.append(board_id.SerialNumber.strip().strip('.'))
    return mainboard[0]

# print(get_mainboard_info()[0])