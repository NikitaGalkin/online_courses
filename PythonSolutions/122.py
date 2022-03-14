objects = [1, 2, 1, 2, 3]
unique = []
for obj in objects:
    if not obj in unique:
        unique.append(obj)

print(len(unique))