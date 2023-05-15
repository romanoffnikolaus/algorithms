def bubble_sort(nums):
    # Устанавливаем check параметр в True, чтобы цикл запустился хотя бы один раз
    check = True
    while check:
        check = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем check в True для следующей итерации
                check = True

random_list_of_nums = [5, 2, 1, 8, 4, 50, 8, 1, 180, 6, 66]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)