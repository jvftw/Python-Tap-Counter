import time
import sys
import msvcrt

start_time = time.time()
elapsed_time = 0
count1 = 0
count2 = 0

while elapsed_time < 60:
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8')
        if key == "z":
            count1 += 1
        elif key == "x":
            count2 += 1
    elapsed_time = time.time() - start_time

print("key1 was pressed", count1, "times")
print("key2 was pressed", count2, "times")
