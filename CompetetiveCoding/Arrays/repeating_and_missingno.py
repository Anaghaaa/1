def repeat_and_missing_number(A):
    r = []
    sum_l = 0
    n = len(A)
    A = list(A)
    # calculate repeating number by O(N)
    for i in range(n):
        sum_l += abs(A[i])
        if A[abs(A[i])-1] > 0:
            A[abs(A[i])-1] = -A[abs(A[i])-1]
        else:
            r.append(abs(A[i]))

    # calculate sum of the list, n*(n+1)//2
    # actual sum of 1 to N - (above sum -repeating no) = missing number
    sum_n = n*(n+1)//2
    r.append(sum_n-(sum_l-r[0]))
    return r
