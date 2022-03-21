from math import *


def binary_search(lst, item):
    """
    二分查找算法自实现

    Parameters
    ----------
    lst : list or array like
        有序的序列.
    item : number
        需要查找的数据.

    Returns
    -------
    如果元素在列表中返回元素所在位置
    如果元素不在列表中返回None.

    """
    low = 0
    high = len(lst) - 1
    
    while low<=high:
        mid_num = floor((high + low) / 2)
        guess = lst[mid_num]
        
        if guess == item:
            return mid_num
        
        if guess > item:
            high = mid_num -1 
            
        if guess < item:
            low = mid_num + 1
            
    return None
    

if __name__ == "__main__":
    lst = [1,3,5,7,9,11]
    idx_num = binary_search(lst, 1)
    if idx_num is not None:
        print("列表中包含元素,索引为:{}".format(idx_num))
    else:
        print("列表中没有找到元素")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    