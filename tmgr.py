import argparse
import matplotlib.pyplot as plt
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument("FILE")
parser.add_argument("RANGE")
parser.add_argument('-xl', action='store_true')
parser.add_argument('-yl', action='store_true')
parser.add_argument('-i', action='store_true')
args = parser.parse_args()

file = args.FILE
ran = args.RANGE.split(",")
intin = args.i
xlog = args.xl
ylog = args.yl

x=[]
y=[]

if xlog:
    if len(ran) == 3:
        st = float(ran[0])
        en = float(ran[1])
        ju = float(ran[2])
    elif len(ran) == 2:
        st = float(ran[0])
        en = float(ran[2])
        ju = 1
    elif len(ran) == 1:
        en = float(ran[0])
        st = 1
        ju = 1
    else:
        print("Error wrong number of inputs in range")
        exit
    i = st
    while i < en:
        if intin:
            inp = int(i)
        else:
            inp = i
        x.append(inp)
        start_time = time.perf_counter()
        res = subprocess.run([file, str(inp)], capture_output=True, text=True)
        end_time = time.perf_counter()
        elapsed_ms = (end_time - start_time)      
        if res.returncode != 0:
            print("Error on input", i)
            exit
        y.append(elapsed_ms)
        i*=ju
else:
    for i in range(*map(int, ran)):
        if intin:
            inp = int(i)
        else:
            inp = i
        x.append(inp)
        start_time = time.perf_counter()
        res = subprocess.run([file, str(inp)], capture_output=True, text=True)
        end_time = time.perf_counter()
        elapsed_ms = (end_time - start_time)
        if res.returncode != 0:
            print("Error on input", i)
            exit
        y.append(elapsed_ms)

plt.plot(x, y, marker = 'o')

plt.xlabel('x - Input')
plt.ylabel('y - Time in ms')

plt.title('Time graph!')

plt.show()