
array = list(map(int, input('введите числа через пробел: ').split()))

print(array)

for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]
print(array)

element = int(input('Введите число в рамках последовательности: '))
while element:
    if element not in range(min(array) + 1,max(array)):
        print('Некорректное число')
        element = int(input('введите число в рамках последовательности: '))
    else:
        break

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print(binary_search(array, element, 0, len(array)-1))
