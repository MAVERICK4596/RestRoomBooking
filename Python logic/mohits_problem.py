def Find_the_next(source_list):
    occupied_list = []
    difference_list = []
    max_difference = 0

    for i in range(0, len(source_list)):
        if(source_list[i] == 1):
            occupied_list.append(i)

    if(len(occupied_list)==0):       
       source_list[0]=1
    elif(len(occupied_list)==1):
        source_list[len(source_list)-1]=1
    else:
        for j in range(0, len(occupied_list)-1):Find_the_empty
            difference = abs(occupied_list[j]-occupied_list[j+1])
            difference_list.append(difference)
        
        max_difference = max(difference_list)
        for k in range(0, len(occupied_list)-1):
            difference = abs(occupied_list[k]-occupied_list[k+1])
            if(difference == max_difference):
                source_list[(occupied_list[k]+(difference//2))]=1
                
    print(source_list)
    
Find_the_next([1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1])













