# On Windows with `conda install pexpect`
from pexpect.popen_spawn import PopenSpawn 
 

python_module = r"examples\uno.py"
command = r"C:\Users\ropf\Anaconda3\python.exe -m pdb " + python_module
pdb = PopenSpawn(command)
pdb.expect("\(Pdb\) ")
response = pdb.before.decode("utf-8")
print(response)
pdb.sendline('n')
pdb.expect("\(Pdb\) ")
response = pdb.before.decode("utf-8")
print(response)
