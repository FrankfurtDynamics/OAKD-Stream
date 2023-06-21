import os
print("[0] Mono")
print("[1] Color")

val = input("Choose color mode: ")
print(val)
if int(val) == 0:
    os.system('python3 mono.py')

elif int(val) == 1:
    os.system('python3 color.py')

else:
    print("No such color mode")