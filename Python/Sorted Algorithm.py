# -*- coding: cp936 -*-
def bubble_sort(l):
    n = len(l)
    for i in xrange(0,n-1,1):
        for j in xrange(0,n-i-1,1):
            if l[j] > l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    
def partition(l,low,high):
    key = l[low]
    while (low<high) and (l[high]>=key):
        high -= 1
    l[low],l[high] = l[high],l[low]

    while (low<high) and (l[low]<=key):
        low += 1
    l[low],l[high] = l[high],l[low]
    return low

def quick_sort(l,low,high):
    mid = partition(l,low,high)
    if low<mid-1:
        quick_sort(l,low,mid-1)
    if mid+1<high:
        quick_sort(l,mid+1,high)

def insert_sort(l):
    for i in xrange(1,len(l),1):
        key = l[i]
        j = i-1
        while key<l[j] and j>=0:
            l[j+1]=l[j]
            j -= 1               
        l[j+1]=key

def shell_insert_sort(l,interval):
    for i in xrange(interval, len(l), interval):
        key = l[i]
        j = i-interval
        while key<l[j] and j>=0:
            l[j+interval]=l[j]
            j -= interval
        l[j+interval]=key

def shell_sort(l):
    interval = len(l)/2
    while interval:
        shell_insert_sort(l,interval)
        interval = interval/2
        print l

def select_min_key(l):
    key = l[0]
    pos = 0
    for i in xrange(1,len(l),1):
        if l[i]<key:
            key = l[i]
            pos = i
    return pos

def select_sort(l):
    for i in xrange(0,len(l),1):
        m=l[i:len(l)]
        pos = select_min_key(m)
        if i is not pos+i:
            l[i],l[pos+i] = l[pos+i],l[i]


def heap_adjust(l,s,length):
    tmp = l[s]
    child = 2*s+1
    while child<length:
        if child+1<length and l[child+1]<l[child]:
            child += 1
        if l[s]>l[child]:
            l[s] = l[child]
            s = child
            child = s*2+1
        else:
            break
        l[s] = tmp
    
    

def build_heap(l):
    list_size = len(l)
    for i in xrange((list_size-1)/2,-1,-1):
        heap_adjust(l,i,list_size)

def heap_sort(l):
    build_heap(l)
    list_size = len(l)
    m = [l[0]]
    l[0] = l[list_size-1]   
    for i in xrange(1,list_size,1):
        l = l[0:list_size-i]       
        print l
        heap_adjust(l,0,len(l))
        m.append(l[0])
        l[0] = l[len(l)-1]
    return m

def merge(a,b):
    m = []
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            m.append(a[i])
            i+=1
        else:
            m.append(b[j])
            j+=1

    while i<len(a):
        m.append(a[i])
        i+=1
    while j<len(b):
        m.append(b[j])
        j+=1
        
    return m

def merge_sort(l):
    if len(l)<=1:
        return l
    mid = len(l)/2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left,right)
            
    
if __name__=='__main__':
    l=[3,1,5,7,2,4,9,6,10,8]  
    m = merge_sort(l)
    print m
