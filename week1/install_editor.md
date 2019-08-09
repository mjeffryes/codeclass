# Python orientation (Part 2)

Note: I might chose VS Code instead of sublime now.

## OS X

1. Install the editor:
    1. Visit [https://www.sublimetext.com/3](https://www.sublimetext.com/3) and click on the link to download the installer for Sublime Text 3. Install it by opening the package you downloaded and dragging the “Sublime Text” app into your Applications folder.
    2. Drag a shortcut SublimeText onto your Dock so you can find it easily.
2. Create a project directory for this class
    3. Open up your terminal and create a project directory for this class by typing:

        ```
        mkdir -p workspace/codeclass
        ```



        and then hitting return.

    4. Look at your current directory by typing:

        ```
        ls
        ```



        And then hitting return. You should see a directory called `workspace/` in the output.

    5. Look at the workspace/ directory by typing:

        ```
        ls workspace
        ```



        And then hitting return. You should see a directory called `codeclass/` in the output.

    6. Change into your new directory by typing:

        ```
        cd workspace/codeclass
        ```



        And then hitting return

    7. Look at your current directory (ie. the codeclass directory) by typing:

        ```
        ls
        ```



        And then hitting return. The output should be empty

3. Create a Python file
    8. Open your editor (ie. Sublime Text)
    9. Type/copy in the following text:

            ```
            # The four fours challenge!

            from math import *

            print("Zero is", 4+4-4-4)
            ```


    10. Save your file (Cmd-S) in your newly created codeclass directory with the file name of `four_fours.py`
    11. The text in your editor should now have lots of pretty colors. When you save a file with the `.py` extension, your editor can now tell that this is a python file and colorizes the text help you see the structure of the program more easily. (This is called “syntax highlighting”)
4. Run your new python program
    12. Go back to your terminal and type

        ```
        ls
        ```



        And hit return. You should see your new `four_fours.py` file in the output.

    13. Now type

        `python3 four_fours.py`


        into the terminal and hit return. You should see it print:


        ```
        Zero is 0

        ```



## Windows 10



1. Install the editor:
    1. Visit [https://www.sublimetext.com/3](https://www.sublimetext.com/3) and click on the link to download the installer for Sublime Text 3. Run the installer and accept the defaults.
    2. Drag a shortcut SublimeText onto your Desktop so you can find it easily.
2. Create a project directory for this class
    3. Open up your terminal and create a project directory for this class by typing:

        ```
        mkdir -p workspace/codeclass
        ```



        and then hitting return.

    4. Look at your current directory by typing:

        ```
        ls
        ```



        And then hitting return. You should see a directory called `workspace/` in the output.

    5. Look at the workspace/ directory by typing:

        ```
        ls workspace
        ```



        And then hitting return. You should see a directory called `codeclass/` in the output.

    6. Change into your new directory by typing:

        ```
        cd workspace/codeclass
        ```



        And then hitting return

    7. Look at your current directory (ie. the codeclass directory) by typing:

        ```
        ls
        ```



        And then hitting return. The output should be empty

3. Create a Python file
    8. Open your editor (ie. Sublime Text)
    9. Type/copy in the following text:

            ```
            # The four fours challenge!

            from math import *

            print("Zero is", 4+4-4-4)
            ```


    10. Save your file (Ctrl-S) in your newly created codeclass directory with the file name of `four_fours.py`
    11. The text in your editor should now have lots of pretty colors. When you save a file with the `.py` extension, your editor can now tell that this is a python file and colorizes the text help you see the structure of the program more easily. (This is called “syntax highlighting”)
4. Run your new python program
    12. Go back to your terminal and type

        ```
        ls
        ```



        And hit return. You should see your new `four_fours.py` file in the output.

    13. Now type

        `python3 four_fours.py`


        into the terminal and hit return. You should see it print:


        ```
        Zero is 0
        ```
