import math

my_list = [1,3,4,5,7,8,9]

def binary_search(list, item):
    low = 0;
    high = len(list) - 1

    print(f"low: {low} high: {high}")

    while low <= high:
        mid = math.floor((high + low) / 2)
        guess = list[mid]        
        
        print(f"mid: {mid} guess: {guess} high: {high} low: {low}")
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    
    return False;




print(binary_search(my_list,3))
print(binary_search(my_list,1))
print(binary_search(my_list,9))
print(binary_search(my_list,99))

