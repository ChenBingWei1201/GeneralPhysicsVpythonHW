a = [0, 1, 3, 9.0, "n", 100]
a[0] = 100
a[-1] = 0
a[2:5] = ["z", "y", "x"]
a.append("c")
b = a
for i in b:
    print(i)
print("a = ", a)   
