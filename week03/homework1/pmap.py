import argparse
from multiprocessing import Pool,Queue,Lock
import os
import subprocess
from time import time,sleep
import random

def argsdel():
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('-n', type=int, default = 1)
    parser.add_argument('-f', type=str, default=None)
    parser.add_argument('-ip', type=str, default=None)
    parser.add_argument('-w', type=str, default=None)
    args = parser.parse_args()
    print(args.n)
    print(args.f)
    print(args.ip)
    print(args.w)
    return args
def delip(ip):
    if '-' in ip:
        lines = ip.split('-')
        fanwei = []
        wangduan = ''
        for strs in lines[1].split('.')[0:3]:
            wangduan = wangduan+strs+'.' 
        for ip in lines:
            fanwei.append(int(ip.split('.')[3]))    
        print(fanwei)
        print(wangduan)
        return [wangduan+f'{ips}' for ips in range(fanwei[0],fanwei[1])]
    else:
        return [ip]

def pingip(q,l,ip):
    # l.acquire()
    # print('开始子进程')
    cmd = f"ping -w 1 {ip}|findstr ms"
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout
    print(cmd+'|'+str(pipe.read().decode('gbk')))
    
    # l.release()

def run(name):
    print("%s子进程开始，进程ID：%d" % (name, os.getpid()))
    start = time()
    sleep(random.choice([1, 2, 3, 4]))
    end = time()
    print("%s子进程结束，进程ID：%d。耗时%0.2f" % (name, os.getpid(), end-start))

if __name__ == "__main__":
    q = Queue()
    l = Lock()
    inputargs = argsdel()

    iplist = delip(inputargs.ip)
    print(iplist)
    # pingip(iplist[1],q,l)
    # with Pool(processes=inputargs.n) as pool:
    p = Pool(inputargs.n)

    for ip in iplist:
        # print('+'*20)
        p.apply_async(pingip,args=(q,l,ip,))
        # p.apply_async(run,args=(ip,))
        # print('-'*20)
    p.close()
    p.join()
    # p.terminate()

    