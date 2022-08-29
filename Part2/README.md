## ASSOCIATED FILES
1. ```all-moduli.csv``` **-->** Contains all moduli posted by the professor and students up to 5/19/2022 - 2:09 PM.
3. ```factored-moduli.txt``` **-->** Contains all of the moduli that were factored successfully by the authors and the relevant information.
4. ```factoring.py``` **-->** Python file containing all major factoring algorithms used to factor some moduli in the above file.
5. ```factoring.ipynb``` **-->** Jupyter notebook file containing all major factoring algorithms used to factor some moduli in the above file.
6. ```main.c``` **-->** Contains the Pollard's Rho algorithm written in C with the GMP multiprecision library.
7. ```Makefile``` **-->** Used to build and compile the C file ```main.c``` above.

## BUILD INSTRUCTIONS (PYTHON FILE - COMMAND PROMPT)
1. Open a command-line.
2. Navigate to the folder containing the python file with the name: ```factoring.py```.
3. In the command-line, type ```python factoring.py``` or ```python3 factoring.py``` depending on your version, and hit Enter.

## BUILD INSTRUCTIONS (PYTHON FILE - VS Code)
1. Open the folder containing the python file with the name: ```factoring.py``` in VS Code.
2. Open a new terminal. By clicking ```Terminal``` on the top bar and then ```New Terminal```.
3. Click the ```Run``` button logo on the top right or click ```Run``` on the top bar and then ```Run Without Debugging```.

## BUILD INSTRUCTIONS (JUPYTER NOTEBOOK FILE)
1. Douwnload Jupyter Notebook, instructions here: https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/install.html. _Note_ there are many other ways to download Jupyter Notebook.
2. Run Jupyter Notebook on your machine.
3. Open the ```factoring.ipynb``` file on Jupyter Notebook and run all the blocks.

## BUILD INSTRUCTIONS (C FILE - PUTTY)
1. Douwnload the SSH Telnet client software, PuTTy, from here: https://www.putty.org/. 
2. Download WinSCP to upload the files ```Makefile``` and ```main.c``` to the UMBC GL server, instructions here: https://wiki.umbc.edu/display/faq/Setting+up+a+SFTP+Client.
3. To run C file, you will also want to install GMP, using the instructions here: http://rstudio-pubs-static.s3.amazonaws.com/493124_a46782f9253a4b8193595b6b2a037d58.html.
4. Once GMP is successfully installed, open up PuTTy, and log in using your UMBC credentials, instructions here: https://userpages.umbc.edu/~cmarron/cs341.s20/resources/accessing_gl.pdf.
5. On PuTTy, use the change directory command ```cd``` to get to the folder containing the files ```Makefile``` and ```main.c```.
6. When you're in the folder, run the command: ```make```.
7. Once ```make``` outputs successfully, run the command: ```./main```.

## POSSIBLE ERROR ENCOUNTERS
1. Maximum recursion depth exceeded
      * **Solution:** Change the recursion limit on line 5 of ```rsa.py``` to a higher value than the initial input.
      * That is, change the line ```sys.setrecursionlimit(5000)``` to something like ```sys.setrecursionlimit(6500)``` until the error doesn't exist.

## NOTES
1. The python files were all _initially_ programmed and tested in Microsoft Visual Studio Code (VS Code).
2. Installation of _big_ modules/softwares may be required to run some of the programs/files. We recommend running only the python file ```factoring.py``` if you do not want to install anything else. As all other programming files contain the same information.

## AUTHORS
_Atta-ur-Rheman Navaid-Munir_ and _Liam Dobbins_
