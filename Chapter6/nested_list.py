rivers={
    "Nile": ["Egypt", "Sudan", "Burundi", "Tanzania", "Rwanda", "Congo", "Kenya", "Uganda", "Sudan", "Ethiopia", "South Sudan"],
    "Mississippi River":["United States"],
    "Chang": ["China"],
}

print("***Rivers & Country***")
for key, value in rivers.items():
    print(f"The {key.title()} river flows through {value}")

print("***Rivers***")
for key in rivers.keys():
    if type(value)==list:
        print(f"The {key.title()} river flows through: ")
        for v in value:
            print("\t\t\t\t",v)
    else:    
           print(f"The {key.title()} river flows through {v.title()}")

print("***Countries***")
for value in rivers.values():
    print(value)