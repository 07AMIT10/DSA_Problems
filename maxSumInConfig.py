a = [1,2,3,4]
n = len(a)


a_sum=sum(a)
curr_val=sum(i*a[i] for i in range(n))
print(curr_val)
max_value=curr_val
for i in range(1,n):        
    curr_val=curr_val+a_sum-n*a[n-i]
    if curr_val>max_value:
        max_value=curr_val
    print(max_value)