import os

output = os.popen('ip a').read()

print(output.strip())
