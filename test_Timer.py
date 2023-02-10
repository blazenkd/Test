import time
import subprocess

file_path = "test_Blank.py"

start_time = time.time()
# subprocess.run(["code", file_path, "--new-window"], shell = True)
subprocess.run(["code", file_path, "--reuse-window"], shell = True)

# Mac
# subprocess.run(['code', "-n", "Visual Studio Code"], file_path)

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

