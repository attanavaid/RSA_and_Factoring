import sys
import random
import time
import math
import csv
import multiprocessing

sys.setrecursionlimit(5000)
start_time = time.time()

def POLLARD_RHO(n, run):
    while run.is_set():
        # If n is even, return 2 as a factor
        if ((n % 2) == 0):
            print(f"Pollard's Rho determined that one of the divisors for {n} is 2 in {time.time() - start_time} seconds.\n")
            run.clear()
            return 2

        # Initialize parameters, set curr to equal any integer less than n
        i = 0
        curr = random.randint(0, n - 1)
        y = curr
        k = 2

        # Loop forever using the reccurence relation on line 29
        # and search for a factor
        while (1):
            i = i + 1 # Record how many times the loop runs
            next = (pow(curr, 2) - 1) % n  # Compute the next value of the sequence using the most recent value
            d = math.gcd((y - next), n) # Compute GCD using y and the next value of the sequence

            # If d is neither 1 nor n, return d, the non-trivial divisor
            if (d > 1) and (d < n):
                print(f"Pollard's Rho determined that one of the divisors for {n} is {d} in {time.time() - start_time} seconds.\n")
                run.clear()
                return d
            
            # Set y to equal the most recent value of the sequence (value with subscript k) and 
            # double k when the number of times the loop has ran equals k.
            if (i == k):
                y = next
                k = 2 * k
            
            curr = next  # Save the most recent value of the sequence
        
        # The algorithm failed to find a factor, return 1
        print(f"Pollard's Rho determined that one of the divisors for {n} is 1 in {time.time() - start_time} seconds.\n")
        run.clear()
        return 1

def POLLARD_P_MINUS_1(n, B, run):
    while run.is_set():
        # If n is even, return 2 as a factor
        if ((n % 2) == 0):
            print(f"Pollard's P-1 method determined that one of the divisors for {n} is 2 in {time.time() - start_time} seconds.\n")
            run.clear()
            return 2
        
        # Initialize the base and the product of all (or most) integers less than or equal to B
        a = 2
        m = 2
        
        # Make computations based on Fermat's little theorem incrementally and make checks
        while (m <= B):
            a = pow(a, m) % n
            d = math.gcd((a - 1), n) # Compute GCD using ((a ^ m) - 1) and modulus

            # If d is neither 1 nor n, return d, the non-trivial divisor
            if (d > 1) and (d < n):
                print(f"Pollard's P-1 method determined that one of the divisors for {n} is {d} in {time.time() - start_time} seconds.\n")
                run.clear()
                return d

            m = m + 1
        
        # The algorithm failed to find a factor, return 1
        print(f"Pollard's P-1 method determined that one of the divisors for {n} is 1 in {time.time() - start_time} seconds.\n")
        run.clear()
        return 1

def SQUARE_ROOT_TRIVIAL_DIVISION(n, run):
    while run.is_set():
        # Floor of square root of n
        p = math.isqrt(n)
        
        # Check for perfect square
        if (pow(p, 2) == n):
            print(f"Square Root Trivial Division determined that one of the divisors for {n} is {p} in {time.time() - start_time} seconds.\n")
            run.clear()
            return p
        
        # If p is even, add 1 and make it odd
        if ((p % 2) == 0):
            p = p + 1
        
        # While no odd factor of n is found, increment the possible factor
        while ((n % p) != 0):
            p = p + 2
        
        # Check for no factor of n found other than itself
        if (p == n):
            print(f"Square Root Trivial Division determined that one of the divisors for {n} is 1 in {time.time() - start_time} seconds.\n")
            run.clear()
            return 1
        
        # Print and return the found factor
        print(f"Square Root Trivial Division determined that one of the divisors for {n} is {p} in {time.time() - start_time} seconds.\n")
        run.clear()
        return p

if __name__ == "__main__":
    # Open the all-moduli.csv file and read it properly line-by-line
    with open("all-moduli.csv") as moduliFile:
        moduli = csv.reader(moduliFile, delimiter = ",")
        lineNum = 0
        for modulus in moduli:
            # Ignore the headings: ModulusName,Modulus. Print the line below instead
            if (lineNum == 0):
                print("Final Project: Part 2\n") 
            
            # Set lineNum to whatever modulus you want to factor from the all-moduli.csv file. (lineNum == 1) means test80, (lineNum == 2) means test 100, and so on...
            elif (lineNum == 1):
                # Start the timer and set parameters required for efficient multiprocessing
                print(f"Finding a factor for {modulus[0]}...")
                start_time = time.time()
                run = multiprocessing.Event() # Will aid in stopping all other parallel processes once a process is complete
                run.set()
 
                # Set range to mirror the number of logical processors in your CPU, in my case that would be 8.
                for i in range(0, 8):
                    # Divide the processes. In this case, I made 7/8 processes run Pollard's Rho and 1/8 processes run Pollard's P - 1 method.
                    if (i <= 6):
                        process = multiprocessing.Process(target = POLLARD_RHO, args = (int(modulus[1]), run))
                    else:
                        process = multiprocessing.Process(target = POLLARD_P_MINUS_1, args = (int(modulus[1]), pow(2, 16), run))
                    
                    process.start()
                    process.join()
            
            lineNum = lineNum + 1
    
    print("========= END =========")