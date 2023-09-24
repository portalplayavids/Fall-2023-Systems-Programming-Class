# Elijah Guzman - nze594 - 09/15/23
#implement the fibonnaci function using naive and memo methods
#and compare the time it takes to run each method

import time

#user input for fibonnaci number
n = int(input("Enter a number: "))
print("")
memo = [0] * (n+1)

#fibonnaci function using naive method
def fibonnaciNaive(n):
    if n <= 1:
        return n
    else:
        return fibonnaciNaive(n-1) + fibonnaciNaive(n-2)
    
#fibonnaci function using memo method
def fibonnaciMemo(n, memo):
    if memo[n] != 0:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonnaciMemo(n-1, memo) + fibonnaciMemo(n-2, memo)
    return memo[n]

    

#print the fibonnaci number using user's input
print("Compute time for F(input)")
start_time = time.time()
fibonnaciNaive(n)
end_time = time.time()
elapsed_time = end_time - start_time
print("Naive method: ", elapsed_time)
start_time = time.time()
fibonnaciMemo(n, memo)
end_time = time.time()
elapsed_time = end_time - start_time
print("Memo method: ", elapsed_time)
print("")

#measure the time it takes to compute F(40) for naive method
start_time = time.time()
fibonnaciNaive(40)
end_time = time.time()
elapsed_time = end_time - start_time
print("Compute time for F(40)")
print("Naive time: ", elapsed_time)

#measure the time it takes to compute F(40) for memo method
start_time = time.time()
memo = [0] * 41
fibonnaciMemo(40, memo)
end_time = time.time()
elapsed_time = end_time - start_time
print("Memo time: ", elapsed_time)