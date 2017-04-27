#coding=utf-8
#�����㷨��Pythonʵ��
a = [12,32,4,23,5,65,65,67,45,39]
print a

#ð������
def BubbleSort(a):
    for i in range(10):
        for j in range(9,0,-1):
            if  a[j] < a[j-1] :
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp
    return a

print BubbleSort(a)
####################################
#ѡ������
a = [12,32,4,23,5,65,65,67,45,39]
def SelectSort(a):
    for i in range(len(a)):
        minIndex = i
        for j in range(i+1,len(a)):
            if a[j] < a[minIndex] :
                minIndex = j
                
        if minIndex != i:
            temp = a[i]
            a[i] = a[minIndex]
            a[minIndex] = temp

    return a
print SelectSort(a)
#************************************
#��������
a = [12,32,4,23,5,65,65,67,45,39]
def InsertSort(a):
    for i in range(1,len(a)):
        j = i
        target = a[i]
        while target < a[j-1]:
            a[j] = a[j-1]
            j    = j-1
            if j < 1 :
                break
        a[j] = target
        
    return a
print InsertSort(a)
######################################
#��������
#a = [12,32,4,23,5,65,65,67,45,39]
def Partition(a,left,right):
    pivot = a[left]
    i = left+1
    j = right
    while i < j:
        while a[j] >= pivot:
            j = j-1
            if j == 0:
                break
        while a[i] <  pivot:
            i = i+1
            if i ==len(a):
                break
        a[i],a[j] = a[j],a[i]
    if i == j:
        left = i+1
    else:
        left = i
    return left

def QuickSort(a,left,right):
    if left > right:
        return
    Partition(a,left,right)
    QuickSort(a,left,right)
    QuickSort(a,0,left-1)
    return a
print QuickSort(a,0,len(a)-1)
########################################
a = [12,32,4,23,5,65,65,67,45,39]
def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort(array,low,high):
     if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)

quick_sort(a,0,len(a)-1)
print a
#################################################
    
    


















