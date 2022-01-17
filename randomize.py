import yaml
import random
from time import sleep

def strike_out(text):
    s = ''.join(chr(822)+t for t in text + " ")
    return s

sleep(1)
for i in range(1, 4):
    print(" 🥁 "*i, end="\r")
    sleep(1)
print("\n")

with open("names.yaml", 'r') as f:
    names = yaml.safe_load(f)

names = [n.lower() for n in names]

if "last is last" in names:
    names.remove("last is last")
    last = names[-1]
    names.remove(last)
    random.shuffle(names)
    names.append(last)
else:
    random.shuffle(names)

for i, name in enumerate(names):
    i = str(i) + ":"
    i = i.ljust(3)
    print(f"{i} {name.title()}")

sleep(1)
print("\n 🎊 🎊 🎊 🎊 🎊 🎊 🎊 🎊 🎊 🎊")
