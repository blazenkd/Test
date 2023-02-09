import time
import subprocess

start_time = time.time()
subprocess.run(["code","test_Blank.py", "--new-window"], shell = True)

def finished(answer):
    # Create Input
    answer = input('Are you finished? ')
    print("Congrats!")
finished("")

end_time = time.time()

elapsed_time = end_time - start_time
minutes, seconds = divmod(elapsed_time, 60)
hours, remainder = divmod(elapsed_time, 3600)

print("Time elapsed: {:.2f} seconds".format(elapsed_time))
print(f"Elapsed time: {int(minutes)} minutes and {int(seconds)} seconds")
print("Elapsed Time: {:02}:{:02}:{:05.2f}".format(int(hours), int(minutes), seconds))

with open('file.py', 'a') as f:
    lines = f.readlines()
new_item = 'new item'
lines.append(new_item)
with open('file.py', 'w') as f:
    f.seek(0)
    f.writelines(lines)