import os

def next_line(numbers):
    count = 0
    val = numbers[0]
    res = ""
    for n in numbers:
        if n == val:
            count += 1
        else:
            res += "%s%s" %(count, val)
            count = 1
            val = n
 
    res += "%s%s" %(count, val)
    return res
 
s = "1"
print(s)
for i in range(100):
    s = next_line(s)
    print(s)
    os.system(f"echo {s} >> algo.txt")