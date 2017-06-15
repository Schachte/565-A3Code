'''
@Author: Ryan Schachte
@Description:   nlogn sorting algorithm. Partitions data elements into buckets
                and performs insertion sort on each bucket to yield a master
                sorted array.
@565 A1 Testing Implementation
@Implementation Ideas for Algorithm Gathered from the following sources:
    - http://www.programming-algorithms.net/article/41160/Bucket-sort
    - https://www.youtube.com/watch?v=VuXbEb5ywrU
    - https://stackoverflow.com/questions/10892677/optimal-bucket-size-and-no-of-buckets
    - https://www.youtube.com/watch?v=geVyIsFpxUs
'''
import math

def check_list_of_numerics(input_list):
    '''Function to ensure all input elements are numerics'''
    for data in input_list:
        if (not (isinstance(data, (int, float)) and not isinstance(data, bool) and not isinstance(data, str))):
            raise TypeError("All inputs must be numerical values")
    return True

def bucket_sort(input_data):
    '''Sorts the data using bucket sort algorithm'''

    #Input type must be a list
    if (not isinstance(input_data, list)):
        raise TypeError("Input must be a list!")

    #Ensure that all input values in the list are numerics
    check_list_of_numerics(input_data)

    #Handle the base-case (Already sorted)
    if (len(input_data) == 0 or len(input_data) == 1):
        return input_data

    #Get min and max out of the input array
    minVal, maxVal = min(input_data), max(input_data)

    #Get the size of each bucket
    numBucket = math.ceil((maxVal - minVal)/len(input_data)+1)

    #Compute the range for each bucket
    rngBucket = math.ceil((maxVal + 1) / numBucket)

    #List of lists that will contain the buckets to be sorted
    buckets = [[] for i in range(int(numBucket))]

    #Data distribution into buckets
    for x in range(0, len(input_data)):
        buckets[int(math.floor((input_data[x] - minVal) / rngBucket))].append(input_data[x])

    #Sorting buckets
    sorted_data = []
    for bucket in buckets:
        sorted_list = sorted(bucket)
        for item in sorted_list:
            sorted_data.append(item)

    return (sorted_data)
