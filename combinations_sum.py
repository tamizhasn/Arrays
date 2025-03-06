can=[2,8,9]
tar=10
result = []
for i in range(len(can)-1):
    if(can[i]+can[i+1]==tar):
        result.append(can[i])
        result.append(can[i+1])

    
print(result)