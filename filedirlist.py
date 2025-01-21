import os

output = os.popen('cd ../ ; ls -ll').read()

print(output.strip())
