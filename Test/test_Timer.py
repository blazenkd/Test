import time
import subprocess

# Start Script to start timer
# Use Debug instead of Running python script to keep timer going
# Then stop timer by responding to question

# Create path for blank test
file_path = "./test/test_Blank.py"

# Initialize Start Time
start_time = time.time()

# For PC
subprocess.run(["code", file_path, "--new-window"], shell = True)
# subprocess.run(["code", file_path, "--reuse-window"], shell = True)

# Mac
# subprocess.run(['code', "-n", "Visual Studio Code"], file_path)

# Finish Input
def finished():
    # Create Input
    answer = input('Are you finished? ')
    print("Congrats!")
finished()

# Time End
end_time = time.time()

# Time Splits
elapsed_time = end_time - start_time
minutes, seconds = divmod(elapsed_time, 60)
hours, remainder = divmod(elapsed_time, 3600)

print("Time elapsed: {:.2f} seconds".format(elapsed_time))
print(f"Elapsed time: {int(minutes)} minutes and {int(seconds)} seconds")
print("Elapsed Time: {:02}:{:02}:{:05.2f}".format(int(hours), int(minutes), seconds))
