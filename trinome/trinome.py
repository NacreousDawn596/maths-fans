import os
from math import *
import sys

def solutions(delta, a, b, c):
    if delta > 0:
        return {"S": [(-1*b - delta*0.5)/2*a, (-1*b + delta*0.5)/2*a]}
    elif delta == 0:
        return {"S": [-1*b/2*a]}
    else:
        return {"S": ["this equation doesn't have any solution :/", '', '']}

try:
    a = float(os.popen(f'python3 -c "from math import *; print({input("a: ")})"').read())
    b = float(os.popen(f'python3 -c "from math import *; print({input("b: ")})"').read())
    c = float(os.popen(f'python3 -c "from math import *; print({input("c: ")})"').read())
    print(f"({a}x²) + ({b}x) + ({c}) = 0")
except:
    print("please enter numbers!")
    sys.exit()

print("delta: ", float(pow(b, 2) - 4*a*c))

idk = solutions(float(pow(b, 2) - 4*a*c), float(a), float(b), float(c))

print(idk)

if (len(idk['S']) == 2):
    print(f"factorisation: {a}(x - ({idk['S'][0]}))(x - ({idk['S'][1]}))")
if (len(idk['S']) == 1):
    print(f"factorisation: {a}(x - ({idk['S'][0]}))²")
else: 
    pass