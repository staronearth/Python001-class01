import subprocess
cmd = "ping -w 192.168.222.129|findstr ms"
fhandle = open(r"a.txt", "w")
pipe = subprocess.Popen(cmd, shell=True, stdout=fhandle).stdout
fhandle.close()