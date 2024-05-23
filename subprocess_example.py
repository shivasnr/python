# import subprocess
# result = subprocess.run(['ls', '-al'])
# result

# Running shell commands
import subprocess
result = subprocess.run(['ls -al | head -n 1'], shell=True)

thedir = input()

result = subprocess.run([f'ls -al {thedir}'], shell=False)