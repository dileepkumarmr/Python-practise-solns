import sys
print("length of argv ",len(sys.argv))
count = len(sys.argv)
print('Number of arguments: ',count)

for x in sys.argv:
    print(x)