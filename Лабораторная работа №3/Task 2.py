# TODO Напишите функцию find_common_participants
def find_common_participants(participants1, participants2,separator=',') -> list:
    participants_1 = (participants1.split(separator))
    participants_2 = (participants2.split(separator))

    common = set(participants_1) .intersection(participants_2)
    return sorted(list(common))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group))

# TODO Провеьте работу функции с разделителем отличным от запятой
# Проверка с разделителем ' '
participants_first_group2 = "Иванов Петров Сидоров"
participants_second_group2 = "Петров Сидоров Смирнов"
print(find_common_participants(participants_first_group2, participants_second_group2, separator =' '))