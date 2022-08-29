## ASSOCIATED TEXT FILES
1. ```primes1000.txt``` --> Contains all primes number below 1000 (same file provided for in-class assignment #9)
2. ```RSA_miscellaneous.txt``` --> Contains all parameters used to generate the keys, signature, etc.
3. ```RSA_public_key.txt``` --> Contains the public key pair.
4. ```RSA_private_key.txt``` --> Contains the private key pair.
5. ```RSA_signature.txt``` --> Contains the signed message (signature) computed using the private key in the above text file.

## BUILD INSTRUCTIONS (COMMAND PROMPT)
1. Open a command-line.
2. Navigate to the folder containing the python file with the name: ```rsa.py```.
3. In the command-line, type ```python rsa.py``` or ```python3 rsa.py``` and hit Enter.

## BUILD INSTRUCTIONS (VS Code)
1. Open the folder containing the python file with the name: ```rsa.py``` in VS Code.
2. Open a new terminal. By clicking ```Terminal``` on the top bar and then ```New Terminal```.
3. Click the ```run``` button on the top right or click ```Run``` on the top bar and then ```Run Without Debugging```.

## DESCRIPTIONS OF ALGORITHMS
1. ```MODULAR_INVERSE(a, m)```
    * If the GCD of ```a``` and ```m``` is 1, the algorithm uses the extended euclidean algorithm described below to compute certain integers that satisfy certain equations as specified in section 31.2 (pages 937 - 938) of the textbook.

2. ```EXTENDED_EUCLIDEAN(a, b)```
    * Calculate the GCD of ```a``` and ```b``` using recursion and computes the integer coefficients ```x``` and ```y``` to saisfy requirements as specified in section 31.2 (page 937) of the textbook.

3. ```WITNESS(a, n)```
    * Returns true if ```a``` can be used to prove if ```n``` is not a prime by performing modular arithmetic operations and comparing them to certain numbers as specified in section 31.8 (page 969) of the textbook.

4. ```MILLER_RABIN(n, s)```
    * In ```s``` trials, the algorithm selects a random integer ```a``` from 1 to ```n``` and performs the witness test on the random integer. If the integer passed the trials and is a prime, it return true, otherwise if the integer is composite, it returns false. 

5. ```CHECK_IF_PRIME(n)```
    * Checks if ```n``` is a prime by returning true if it exists in the integerPrimes1000 array or if Miller-Rabin returns true. Returns false if ```n``` is less than 2 or is divisible by a number in the integerPrimes1000 array.

6. ```GENERATE_PRIME(modulusSize)```
    * Generates random prime number from 1 to (2^modulesSize)-1 and uses the Miller-Rabin test to check if the random number is prime, if so it returns it, otherwise, it trys a new random number.

7. ```GENERATE_KEYS(modulusSize)```
    * Follows the RSA cryptosystem procedure step-by-step as described in section 31.7 (page 962) of the textbook. Prints out everything it calculated into the relevant text files.

8. ```POPULATE_PRIMES1000()```
    * Uses the ```primes1000.txt``` file provided during in-class assignment #9 to fill in the global array called ```integerPrimes1000``` with all prime numbers below 1000 by converting them from strings, formatting them, then converting them to integers to be easily used/accessed in for loops.
    
9. ```ENCODE(m)```
    * Encodes the passed message using the encoding technique provided in the project description.

## POSSIBLE ERROR ENCOUNTERS:
1. Maximum recursion depth exceeded
    * **Solution:** Change the recursion limit on line 5 of ```rsa.py``` to a higher value than the initial input. That is, change the line ```sys.setrecursionlimit(5000)``` to something like ```sys.setrecursionlimit(6500)``` until the error doesn't exist.

## NOTES 
1. The python files were all programmed and tested in Microsoft Visual Studio Code (VS Code).
2. It is advisable to save all associated text files somewhere else before you run this program, as the program requires you to delete pre-existing files so that there is no confusion.
3. Modulus sizes of 2048 or higher may take a few minutes. A modulus size of 4096 was tested to take somewhere between 9 - 16 minutes.
4. The library used in this program does not use different algorithms depending on parameters sizes. Hence vague descriptions are provided.

## AUTHOR
Atta-ur-Rheman Navaid-Munir
