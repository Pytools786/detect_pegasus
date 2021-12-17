import subprocess

cmd = 'netstat -ano | findStr 587'
 
result = subprocess.check_output(cmd, shell=True)

de = result.decode()
proc_id = " "

for i in range (103, 110):
	proc_id = proc_id + de[i]
print(proc_id)

cmd_2= 'tasklist /fi "pid eq' + proc_id + '"'
op = subprocess.check_output(cmd_2, shell=True)
op = op.decode()
print("				Found malacious request ......")
print(op)

kill = 'taskkill /F /PID' + proc_id

kill_task = subprocess.check_output(kill, shell=True)

print("..........Terminating process ......")

print(kill_task.decode())