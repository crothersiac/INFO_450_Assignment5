#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''

#Partitioning the numbers frim within the text file, 'Numbers', with the pivot becoming the first value within the list.
def partition(numbers, begin, final):
    pivot = numbers[begin]
    low = begin + 1
    high = final
    
    while True:
        while low <= high and numbers[high] >= pivot:
            high = high -1
            
        while low <= high and numbers[low] <= pivot:
            low = low + 1
            
        if low <= high:
            numbers[low], numbers[high] = numbers[high], numbers[low]
            
        else:
            break
        
    numbers[begin], numbers[high] = numbers[high], numbers[begin]
    
    return high
    
#Begin the quicksort process, shifting the int values around after the partition is complete.
def quicksort(numbers, begin, final):
    if begin >= final:
        return
    
    p = partition(numbers, begin, final)
    quicksort(numbers, begin, p-1)
    quicksort(numbers, p+1, final)
   

def main():
    print("\nThe text file 'numbers' is going to be processed and sorted.")
   #Read in the numbers.txt file to begin the function
    with open("numbers.txt","r") as file:
        y = file.read()
        for i in y:
                if i.isdigit() == True:
                    print(i)
                    
    #numbers = rough_numbers.read()
    
    #numbers = [24,56,23,65,23,6,65,67,23,45,67,87,34,23,21,2,6564]#test
    
    quicksort(numbers, 0, len(numbers)-1)
    print(numbers)

    with open('sorted.txt', 'w') as f:
        for item in numbers:
            f.write("%s\n" % item)
    print("\nNumbers have been sorted and written to the 'sorted.txt' file to review.")
    return #return the properly sorted list, and then write said list to the sorted text file.


if __name__ == "__main__":
    main()





##### SOURCES:
##### https://stackabuse.com/quicksort-in-python/
##### 