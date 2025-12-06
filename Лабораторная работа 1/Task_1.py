numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
total_sum = sum(x for x in numbers if x is not None)
# TODO заменить значение пропущенного элемента средним арифметическим
total_count = len(numbers)
average = total_sum / total_count
numbers = [average if x is None else x for x in numbers]
print("Измененный список:", numbers)
