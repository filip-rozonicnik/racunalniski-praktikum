def TwoSum(list, target):
    list2 = list.copy()
    prva = 0
    while prva <= len(list)-1:
        druga = 0
        while druga <= len(list)-1:
            if prva == druga:
                druga +=1
                if druga > len(list)-1:
                    break
            if list[prva] + list[druga] == target:
                return [prva, druga]
            else:
                druga += 1
        prva += 1
    return None
        





   
nums = [3,2,4]
target = 6
print(TwoSum(nums, target))

