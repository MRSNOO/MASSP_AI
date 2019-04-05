def daycontongmax(a,len): 
       
    currentmax = -10**9-1
    endmax = 0
       
    for i in range(0, len): 
        endmax = endmax + a[i] #moi lan cong them 1 phan tu
        if (currentmax < endmax): 
            currentmax = endmax #neu ma tong hien tai nho hon tongmax thi thay tong hien tai = tong max
        if endmax < 0: 
            endmax = 0 #neu ma tong max nho hon 0 thi dat lai tongmax = 0  
    return currentmax

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
print ("Maximum contiguous sum is", daycontongmax(a,len(a)))