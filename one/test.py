def bubble_sort(arry):
    n = len(arry)                   #获得数组的长度
    for i in range(n):
        min=i
        for j in range(min+1,n):
            if  arry[j] < arry[min] :            
                min=j 
                #print (min)
        arry[min],arry[i] = arry[i],arry[min]  
        #print ("!",min)
        #print (arry)
    return arry

arry=[5,4,5,7,9,3,2,3,4]
print (arry)
bubble_sort(arry)
print (arry)
