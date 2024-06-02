#Напишите программу для печати всех уникальных
#значений в словаре.

dic1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {" VIII": "S007"}]

unique_values = set()
for item in dic1:
    unique_values.update(item.values())
print(unique_values)
