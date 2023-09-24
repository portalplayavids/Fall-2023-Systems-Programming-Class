// Elijah Guzman - nze594 - 09/15/2023
// implement the fibbonaci function using naive and memo methods
// and compare the time it takes to run each method

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// timer macros
#define start_timer() clock_gettime(CLOCK_MONOTONIC, &start_time);
#define end_timer() clock_gettime(CLOCK_MONOTONIC, &end_time);
#define elapsed_time() printf("Elapsed time: %f seconds\n", end_time.tv_sec - start_time.tv_sec + (end_time.tv_nsec - start_time.tv_nsec)/1000000000.0);

// User Input Function
int get_user_input() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    return n;
}

// naive fibbonaci function
int fib_naive(int n) {
    if (n <= 1) {
        return n;
    }
    return fib_naive(n - 1) + fib_naive(n - 2);
}

// memo fibbonaci function
int fib_memo(int n, int *memo) {
    if (n <= 1) {
        return n;
    }
    if (memo[n] != -1) {
        return memo[n];
    }
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo);
    return memo[n];
}

// Main Function
int main() {
    // initialize timer variables
    struct timespec start_time;
    struct timespec end_time;

    // get user input
    int n = get_user_input();

    // initialize memo array
    int memo[n + 1];
    for (int i = 0; i < n + 1; i++) {
        memo[i] = -1;
    }

    // run naive fibbonaci function
    printf("Computing F(%d),\n", n);
    start_timer();
    int fibNaive = fib_naive(n);
    end_timer();
    float time = end_time.tv_sec - start_time.tv_sec + (end_time.tv_nsec - start_time.tv_nsec)/1000000000.0;
    printf("Naive time: %f\n", time);

    // run memo fibbonaci function
    start_timer();
    float fibMemo = fib_memo(n, memo);
    end_timer();
    time = end_time.tv_sec - start_time.tv_sec + (end_time.tv_nsec - start_time.tv_nsec)/1000000000.0;
    printf("Memo time: %f\n", time);
    printf("\n");
    
    
    // run naive fibbonaci F(40)
    printf("Computing F(40),\n");
    n = 40;
    start_timer();
    fibNaive = fib_naive(n);
    end_timer();
    time = end_time.tv_sec - start_time.tv_sec + (end_time.tv_nsec - start_time.tv_nsec)/1000000000.0;
    printf("Naive time: %f\n", time);

    // run memo fibbonaci function F(40)
    n = 40;
    start_timer();
    fibMemo = fib_memo(n, memo);
    end_timer();
    time = end_time.tv_sec - start_time.tv_sec + (end_time.tv_nsec - start_time.tv_nsec)/1000000000.0;
    printf("Memo time: %f\n", time);
    
    return 0;
}