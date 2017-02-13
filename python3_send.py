#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re #正则
import os #python 对系统的模块
import sys #python 对系统的模块
import json #python 封装json字符串的模块
import socket #python 套接字模块
import psutil #python 监控模块
# import urllib  #python 向http服务器发起请求的模块
# import urllib2 #python 向http服务器发起请求的模块
import urllib.request # python3\
import urllib.parse # python3
from subprocess import PIPE,Popen  #子进程模块


class AgentClient(object):
    def __init__(self,IpAddr,serverHost,serverPort=8000):
        """
        ipaddr 用来传递本机的IP地址
        serverHost 用来传递服务器的地址
        """
        self.result = {
                # "system":"Linux",
                "ip":IpAddr
            }#作为采集数据的总的数据容器
        self.host = serverHost
        self.port = serverPort
        self.url = "http://%s:%s/api/savedata"%(self.host,self.port) #拼接接口地址
        print(self.url)#用于调试
        self.headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
            }#请求的头信息
    def getSystem(self):
        command = "uname"
        with os.popen(command) as f:
            content = f.read()
            self.result["system"] = content.strip()
        
        # command = "cat /etc/issue"
        # with os.popen(command) as f:
            # try:
                # content = f.read().split(r'\n')[0].split('\l')[0]
            # except Exception as e:
                # content = f.read()
            # self.result["system"] = content.strip()


    def getHostName(self):
        """
            获取主机名称的
        """
        with os.popen("hostname") as f:
             self.result["hostname"] = f.read().split('\n')[0]
    def getMac(self):
        """
            获取mac地址
            ifconfig | awk -F' ' '/ether/{print $2}'
        """
        p = Popen(["ifconfig"],shell=False,stdout=PIPE) #开启子进程执行ifconfig命令，并且不适用shell,
                                                            #讲输出从定向到管道
        stdout,stderr = p.communicate() #获取输出内容
        data = stdout.strip()  #对输出的内容进行两端去空
        # mac = re.compile(r"ether\s[0-9a-fA-F\:]{17}") #形成匹配mac地址的正则
        mac = re.compile(r"\s[0-9a-fA-F\:]{17}") # 可以匹配中文，形成匹配mac地址的正则
        for line in data.decode("utf-8").split("\n\n"): #对去空一行的内容进行切分
            # print(type(mac))
            macs = mac.findall(line) #对切分后的内容机械匹配
            # print('macs',macs)
            if macs:
                for macinfo in macs:
                    # print(len(macinfo))
                    if len(macinfo.strip())==17:
                        self.result["mac"] = macs[0].strip() #得到结果

    def getCpu(self):
        command = "cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c"
        with os.popen(command) as f:
            content = f.read()
            self.result["cpu"] = content.strip()
    def getMem(self):
        command = "free -m | awk '{print $4}'| sed -n '2p'"
        with os.popen(command) as f:
            content = f.read()
            self.result["mem"] = content.strip()+"M"
    def getDisk(self):
        command = "df -h | awk '{print $4}'|sed -n '2p'"
        with os.popen(command) as f:
            content = f.read()
            self.result["disk"] = content.strip()
    def getModel(self):
        command = "uname -r"
        with os.popen(command) as f:
            content = f.read()
            self.result["model"] = content.strip()
    def sendData(self):
        self.getCpu()
        self.getDisk()
        self.getHostName()
        self.getMac()
        self.getMem()
        self.getModel()
        self.getSystem()
                    
        agentData = urllib.parse.urlencode(self.result).encode("utf-8")# python3，对数据进行json封装
        req = urllib.request.Request(url=self.url,data=agentData,headers=self.headers)## python3，携带请求头和请求数据发起请求
        red = urllib.request.urlopen(req)
        print(red.read().decode("utf-8"))
        # 将请求返回的内容以文件的形式进行保存
        # 打开请求返回内容
        return red



if __name__ == "__main__":

    host = sys.argv[1]
    port = sys.argv[2]
    ourIp = sys.argv[3]
    s = AgentClient(ourIp,host,port)
    s.sendData()

    # s.getCpu()
    # s.getDisk()
    # s.getHostName()
    # s.getMac()
    # s.getMem()
    # s.getModel()
    # s.getSystem()
    print(s.result)
