def frequencyCount(arr):
    freq_map = {}
    for i in range(1,len(arr)+1):
        freq_map[i]=0
    for i in arr:
        if i in freq_map:
            freq_map[i]+=1
    print(freq_map)
    arr = []
    for i in freq_map:
        print(arr.append(freq_map[i]))
    # for j in arr:
frequencyCount([2,3,2,3,5])