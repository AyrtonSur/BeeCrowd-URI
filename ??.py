arraySize = int(input())
array = list(map(int, input().split()))

left = 0
right = arraySize - 1
counterLeft = 1
counterRight = 1
greatestInLeft = left
greatestInRight = right
while (left + 1 < arraySize) and (right - 1 > 0) and (right - 1 > greatestInLeft) and (left + 1 < greatestInRight):
    if (array[greatestInLeft]) + counterLeft < array[left + 1]:
        counterLeft = 1
        left += 1
        greatestInLeft = left
    
    else:
        counterLeft += 1
        left += 1
    
    if (array[greatestInRight] + counterRight) < array[right - 1]:
        counterRight = 1
        right -= 1
        greatestInRight = right
    
    else:
        counterRight += 1
        right -= 1
        
maiorTam = array[greatestInRight] + array[greatestInLeft] + greatestInRight - greatestInLeft

print(maiorTam)
#Sorry, don't really remember from where this problem came from
