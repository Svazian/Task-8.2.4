def sort(array_sort):
    for i in range(len(array_sort)):
        for j in range(len(array_sort) - i - 1):
            if array_sort[j] > array_sort[j+1]:
                array_sort[j], array_sort[j+1] = array_sort[j+1], array_sort[j]
    return array_sort


def binary_search(array, element, left, right):
    if left > right:
        return left

    middle = (right + left) // 2
    if array[middle] == element:
        if middle == 0:
            print("В последовательности нет элемента меньше введенного числа")
        else:
            return middle

    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


again = True
while again:
    try:
        input_array = input("Введите последовательность целых чисел через пробел: ")
        input_number = int(input("Введите целое число: "))
        array_list = list(map(int, input_array.split()))
    except ValueError:
        print("Вы ввели некорректные данные, попробуйте еще раз\n")
    else:
        again = False

sort_list = sort(array_list)
if min(sort_list) <= input_number <= max(sort_list):
    findex = binary_search(sort_list, input_number, 0, len(sort_list) - 1)
    print(findex - 1)
else:
    print("Число вне диапозона")