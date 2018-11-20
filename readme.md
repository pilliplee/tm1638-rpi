# CP320 - Final Project

Fall 2018
For Terry
Alex Kirsopp and Pillip Lee

## Overview

Our group have combined both exploration and integration project into one.
The user will able to find out the distance of the object via infrared sensor and then it is displayed on the 7-segment display.
Also, the user will be able to adjust the angle of the stepper motor by using the buttons on the TM1638.

### Hardware and Software Used

For this project, the following components have been used.

```
- raspberry pi 2
- TM1638 - 7-sgement display with buttons and LEDs
- stepper motor
- infrared sensor
- python
```

### Packages & Libraries Needed

Following python package is needed to run the codes for this project.

This package allows us to communicate with TM1638 board and has helper functions that enable using TM1638 easier.
```
1. pytm1638.py
```

## Challenges & Issues

The biggest challenge we have faced with the exploration project was figuring out how we interact with TM1638.
Finding out which GPIO pins was not so hard as there are only five pins total. However, we were not able to find any
relevant packages/libraries that help us use TM1638 using Raspberry Pi via Python.

### Useful Links

Explain what these tests test and why

* [Martin’s Atelier](https://mjoldfield.com/atelier/2012/08/pi-tm1638.html) - Overview of using TM1638 with Raspberry Pi
* [MicroPython TM1638 LED Driver](https://github.com/mcauser/micropython-tm1638) - Sample GitHub repo with TM1638 examples
* [py-tm1638](https://github.com/johnblackmore/py-tm1638) - Another sample GitHub repo with TM1638 examples

## Authors

* **Pillip Lee**
* **Alex Kirsopp**

## License

This project is created for Wilfrid Laurier University CP320 - Physical Computing. Reproduction and redistribution is allowed for academic purposes only.
