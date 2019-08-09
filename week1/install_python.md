# Python orientation (Part 1)

Note: If I were to do this again, I might just have people install python using anaconda:
https://www.anaconda.com/distribution/#download-section

## OS X

1. Install python:
    1. Visit [https://www.python.org/downloads/](https://www.python.org/downloads/) and click on the link to download the installer for python 3.7.3. Run the installer and accept all the defaults.
2. Find your terminal
    2. Use Finder or spotlight to navigate to your “Applications” folder.
    3. Open the “Utilities” folder and find “Terminal.app”.
    4. Drag “Terminal.app” to your dock so it’s easy for you to find again.
    5. Click to open the “Terminal” you should see a short line or two of text with a prompt something like this:

            ```
            Last login: Sat Apr 20 15:04:38 on console
            Matthews-Air:~ mjeffryes$
            ```


3. Run python in interactive mode
    6. Type `python3` into the terminal and hit return. You should see a few more lines of text something like this:

            ```
            Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21)
            [Clang 6.0 (clang-600.0.57)] on darwin
            Type "help", "copyright", "credits" or "license" for more information.
            >>>
            ```


    7. Hit CTRL- Z (^Z), to get out of python. You should be back at a prompt similar to what you had before you typed python.


## Windows 10

1. Install python:
    1. Visit [https://www.python.org/downloads/](https://www.python.org/downloads/) and click on the link to download the installer for python 3.7.3. Run the installer and accept all the defaults.
2. Find your terminal
    2. Search for PowerShell form your start menu and you can just hit Enter to run it.
    3. Make a shortcut to it on your desktop and/or Quick Launch for your convenience.
    4. Run your terminal program (PowerShell). You should see a line or two of text with a prompt that looks something like this:

            ```
            Windows PowerShell
            Copyright (C) Microsoft Corporation. All rights reserved.
            >>
            ```


3. Run python in interactive mode
    5. In your terminal, type `python3` and hit enter. You should see a few more lines of text with a new prompt something like this:

        ```
        Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)]
        Type "copyright", "credits" or "license" for more information.
        >>>
        ```


        1. If you run python and it’s not there (python3 is not recognized.), then in PowerShell enter this:

             `[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python3", "User") `

        2. Close PowerShell and then start it again to make sure Python now runs. If it doesn’t, restart may be required.
    6. Type quit() and hit Enter to exit python. You should be back at a prompt similar to what you had before you typed python.
i
