wound_area = [100,95,91,88,84,20,67]
print(wound_area[-8]) #index error even for +8

print(wound_area)

wound_area.append(47)
print(wound_area)

wound_area.append(58)
print(wound_area)
wound_area.append(67)
print(wound_area)
wound_area.append(76)
print(wound_area)
wound_area.append(6)
print(wound_area)
wound_area.append(7)
print(wound_area)

wound_area.remove(47) #uses value
print(wound_area)

print(wound_area.pop(0)) # uses index
print(wound_area)                                        

print(len(wound_area)) # prints number of items
