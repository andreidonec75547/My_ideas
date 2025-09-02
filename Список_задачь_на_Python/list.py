task_list = [
    
]

list_of_completed_tasks = [
    
]

the_list_if_there_is_time = [
    
]

n = 0
while n < len(list_of_completed_tasks):
    n += 1
    for tl in task_list:
        for ls in list_of_completed_tasks:
            if tl == ls:
                task_list.remove(tl)

k = 0
while k < len(list_of_completed_tasks):
    k += 1
    for tlitit in the_list_if_there_is_time:
        for ls in list_of_completed_tasks:
            if tlitit == ls:
                the_list_if_there_is_time.remove(tlitit)

i = 0
print("Задачи:", len(task_list))
for tl in task_list:
    i += 1
    print("   ", i, tl)

j = 0
print('------------------------------')
print("Если будет время:", len(the_list_if_there_is_time))
for tlitit in the_list_if_there_is_time:
    j += 1
    print("   ", j, tlitit)

print('------------------------------')
print("Выполнено:", len(list_of_completed_tasks))
for loct in list_of_completed_tasks:
    print("   ", "*", loct)
