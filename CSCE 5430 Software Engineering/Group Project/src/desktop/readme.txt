This directory of the repo is for the desktop side of the project.

This is a Qt application written with qt for python - to run it you will need to install pyside6 and qt creator.
getting qt creator will require an account (its free).

Running
* you should use the build.bat file. Assuming you have all the dependencies built, you should need only
  run `build` in your command line
* you can also just run the program with python: `python mainwindow.py` (assumes that the uis have been built)

directories / files
* ui - contains qt ui files (edit this with qt creator) and generated ui files
* ui_*.py - these are the generated files that `pyside6-uic` creates. they get generated when you run the 
  build.bat file. these are stored in the ui folder along with the ui designer folders
* *.pyproject - these are files that tell qtcreator how to do things
* build.bat - this is the file that compiles all the .ui files into usable ui classes that you can have 
  widgets inherit from. Think of this essentially as a makefile.

Tests
to run the tests either user the batch script by typing `test` in your commandline or run the command
python test.py.
the tests don't use any sort of framework for unittesting, we keep up with all of that ourselves because it is
simpler, faster, and better. there is a class calle `AllTests` that has class definitions and function 
defintions. Each function definition is a test case and each class definition is a collection of test cases
(they implement functions for each case).
It is helpful to think of this as a bulleted list:
* all tests
    * test_this_feature
        * case 1
        * case 2
        * ...
    * test_another_feature
        * case 1
        * case 2
        * ...
    * just_a_lone_test

Modifying the UI
* open up qtcreator and select "open" to open an existing project.
* navigate to this repository and select the mainwindow.pyproject.
* Now you can click on the ui file and edit it with the qt creator
* These ui files will need to get "compiled" by using the command:
  `pyside6-uic mainwindow.ui > ui_mainwindow.py` (the batch file 
  included here should help)