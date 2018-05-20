'''
windows下打印正在使用的ip，网关，子网掩码
'''
import os


currentIp = [a for a in os.popen('route print').readlines() if ' 0.0.0.0 ' in a][0].split()[-2]
print(currentIp)


lines = os.popen('ipconfig').readlines()
for index,line in enumerate(lines):
    if currentIp in line:
        currentMask = lines[index+1].split()[-1]
        print(currentMask)
        currentGateway = lines[index+2].split()[-1]
        print(currentGateway)

