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
    print(key.title())

print("***Countries***")
for value in rivers.values():
    print(value)