import os

output = os.popen('cd ../ ; cd opt ; ls -ll').read()

print(output.strip())
