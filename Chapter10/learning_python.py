filename = "Chapter10/learning_python.txt"

with open(filename) as fi:
     info = fi.read()
print("--- Reading Output-----")
print(info)

print("--- Loop---")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n--- readline----")
with open(filename) as fi:
    l = fi.readlines()
for line in l:
    print(line.rstrip())

print("----replace---")

with open(filename) as fi:
    for line in fi:
        print(line.replace('Python', 'CIT'))