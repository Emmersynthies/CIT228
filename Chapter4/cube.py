cube = [1,8,27,64,125,216,343,512,729,1000]
print(cube)

for cube in range(1-10):
    cube.append(cube**3)
    print(cube)


cube = [cube**3 for cube in range(1-10)]
print(cube)