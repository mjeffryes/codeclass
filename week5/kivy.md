Installation
------------

On Mac:
#######

We'll install kivy in a virtualenv:

  $ virtualenv kivy-env  # create the virtual env
  $ source kivy-env/bin/activate # activate the virtual env
  $ pip3 install kivy kivy-examples # install kivy
  $ python3 kivy-env/share/kivy-examples/demo/showcase/main.py # run the demo

On Windows:
###########

I think we'll need to run kivy from powershell to be able to create graphics.
If you can run python from powershell, we'll install in a virtual env:

  $ python -m virtualenv kivy_venv
  $ kivy_venv\Scripts\activate
  $ python -m pip install kivy kivy-examples
  $ python kivy_venv\share\kivy-examples\demo\showcase\main.py

If you can't run python from powershell, we'll install using Anaconda. (A distribution of python
which includes some optimized libraries for numeric operations;
which is valuable for drawing pretty pictures on the screen quickly)

  1. Download the installer: https://www.anaconda.com/download/
  2. Open and run the installer.
  3. On the "Advanced installation options", click "Add Anaconda to my PATH environment variable".
     Otherwise accept the defaults.
  4. In powershell run "conda install kivy -c conda-forge"

Using Kivy
----------

We're going to follow the kivy documentation to create a few kivy applications:

  1. Create a Hello World app: https://kivy.org/doc/stable/guide/basic.html#quickstart

  2. Create a pong game: https://kivy.org/doc/stable/tutorials/pong.html --OR--
     Create a paint app: https://kivy.org/doc/stable/tutorials/firstwidget.html

  3. Try packaging one of your apps for distribution: https://kivy.org/doc/stable/guide/packaging.html
     (This is going to be different on every platform; ask for help if the guide is unclear.)

  4. If you're feeling ambitious, try to package your app for android or iOS.

