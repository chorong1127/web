arr=list(input())
i=0
while i in range(0,len(arr)):
    if arr[i]!=' ':
        print(arr[i])
    if arr[i]=='q':
       break
    i+=1
