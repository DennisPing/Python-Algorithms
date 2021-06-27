def print_fibonacci():
    """
    A static function that returns the first 10 fibonacci numbers for reference.
    Starts with 0 index.
    """
    print("0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89")

def naive_fibonacci(n):
    """
    Return the n-th number in the fibonacci sequence. Uses recursion.
    The basic math expression is Xn = (Xn-1) + (Xn-2)
    The complexity is O(2^n). There are too many overlapping subproblems.
    """
    n = int(n)
    if n == 0 or n == 1: # base case
        return n
    return naive_fibonacci(n-1) + naive_fibonacci(n-2)

def memo_fibonacci(n, memo=[]):
    """
    A fibonacci function that uses memoization.
    Subproblems that we've done are stored in a memo.
    Top down approach. The complexity is O(n).
    """
    # Set up a memo list of n + 1 size
    n = int(n)
    memo = [None] * (n + 1)
    def recursion(n, memo):
        if n == 0 or n == 1:
            return n
        if memo[n] == None:
            memo[n] = recursion(n-1, memo) + recursion(n-2, memo)
        return memo[n]
    return recursion(n, memo)

def tab_fibonacci(n):
    """
    A fibonacci function that uses tabulation.
    Start with the smallest problems and use returned values to calculate larger values.
    Bottom up approach. The complexity is O(n).
    """
    n = int(n)
    if n == 0 or n == 1:
        return n
    x = 0
    y = 1
    for each in range(n)[2:]:
        subSum = x + y
        x = y
        y = subSum
    return x + y

def main():
    print("Return the n-th number in the Fibonacci sequence")
    n = input("Enter a number: ")
    #print(naive_fibonacci(n))
    #print(memo_fibonacci(n))
    print(tab_fibonacci(n))

if __name__ == "__main__":
    main()