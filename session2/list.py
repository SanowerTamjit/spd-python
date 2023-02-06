# fuel_level : [287, 290, 250, 100, "200", 120, 200, "null", -99, null]

fuel_level = [287, 290, 250, 100, "200", 120, 200, "null", -99]
fuel_copy = fuel_level.copy()
fuel_level1 = [287, 290, 250, 100, "200", 120, 200, "null", -99]
print(fuel_level[3:7])
fuel_level.append(32)
fuel_level.extend(fuel_level1)
print(fuel_level)

del fuel_level[-1]
fuel_level.remove(290)
print(fuel_level)
#count()
#clear()
#sort()
#reverse()
for level in fuel_level:
    print(level)