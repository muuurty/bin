import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("TIMES")
parser.add_argument("X")
args = parser.parse_args()

y = args.TIMES.split(",")
x = args.X.split(",")

# print(len(x), len(y))
plt.plot(x, y)

plt.xlabel('x - Input')
plt.ylabel('y - Time in ms')

plt.title('Time graph!')

plt.show()