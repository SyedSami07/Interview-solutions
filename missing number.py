#find missing number from array
n = 7
arr = [7,3,2,4,1,6];
total_sum = n * (n+1)/2;

sum = 0
for i in range(len(arr)):
     sum += arr[i]
     
result = total_sum - sum;
print("missing element: ", result);