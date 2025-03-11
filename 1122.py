def relativeSortArray(self, arr1, arr2):
        seen = set(arr1)
        present =[]
        not_present=[]
        for i in arr2:
            if i in seen:
                t=arr1.count(i)
                for _ in range(t):
                    present.append(i)
        for j in arr1:
            if j not in arr2:
                not_present.append(j)
        not_present.sort()
        for num in not_present:
            present.append(num)
        return present