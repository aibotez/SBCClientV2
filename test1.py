import psutil,os
# #
# #
# # #描述当前磁盘使用情况
# #
# # def describeDisk(path):
# #     diskInfo = psutil.disk_usage(path)
# #     total = diskInfo.total
# #     used = diskInfo.used
# #     free = diskInfo.free
# #     usedPercent = diskInfo.percent
# #     print(total,used)
# # print(os.path.isdir('H:/'))
# # describeDisk('C:/')

import zipfile
import os

import py7zr


def un_zip(file_name, dst):
    archive = py7zr.SevenZipFile(file_name, mode='r')
    archive.extractall(path=dst)
    archive.close()
    # """解压 zip 文件"""
    # zip_file = zipfile.ZipFile(file_name)
    # if os.path.isdir(dst):
    #     pass
    # else:
    #     os.mkdir(dst)
    # for names in zip_file.namelist():
    #     zip_file.extract(names, dst)
    # zip_file.close()



if __name__ == '__main__':
    file_name = r"D:\SBCDown\WinSCP.7z"
    dst = r"D:\SBCDown"
    un_zip(file_name, dst)
