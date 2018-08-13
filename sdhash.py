import sys, subprocess

arguments = sys.argv
arguments.pop(0)

result = subprocess.run(['./sdhash'] + arguments, stdout=subprocess.PIPE)
resultString = result.stdout.decode('utf-8')
print(resultString)
