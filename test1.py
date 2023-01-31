import os,time,socket,struct


def wake_up(mac=None):
    MAC = mac
    BROADCAST = "192.168.2.255"
    if len(MAC) != 17:
        raise ValueError("MAC address should be set as form 'XX-XX-XX-XX-XX-XX'")
    mac_address = MAC.replace("-", '')
    data = ''.join(['FFFFFFFFFFFF', mac_address * 20])  # 构造原始数据格式
    send_data = b''
    # 把原始数据转换为16进制字节数组，
    for i in range(0, len(data), 2):
        send_data = b''.join([send_data, struct.pack('B', int(data[i: i + 2], 16))])
    print(send_data)

    # 通过socket广播出去，为避免失败，间隔广播三次
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(send_data, (BROADCAST, 9))
        time.sleep(1)
        sock.sendto(send_data, (BROADCAST, 9))
        time.sleep(1)
        sock.sendto(send_data, (BROADCAST, 9))
        time.sleep(1)
        sock.sendto(send_data, (BROADCAST, 9))
        print("Done")
    except Exception as e:
        print(e)


# from wakeonlan import send_magic_packet
# send_magic_packet('cc:2d:21:63:ae:d0')
wake_up('4C-ED-FB-75-8C-9B')