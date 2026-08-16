PyCalc v1.5.0

Advanced Math Toolkit

PyCalc is a modular Python command-line math toolkit that provides mathematical operations and utilities through a simple menu-based interface.

Version

v1.5.0

Features

1. Calculator

Addition

Subtraction

Multiplication

Division

Power

Modulus

2. Quadratic Equations

One Quadratic Equation

System of Two Equations

System of Three Equations

Discriminant & Root Analysis

3. Geometry

Circle

Rectangle

Square

Triangle

Cube

Sphere

Cylinder

4. Scientific Calculator

Square Root

Cube Root

Logarithm

Factorial

Sin

Cos

Tan

Arcsin

Arccos

Arctan

<<<<<<< HEAD
5. History
=======
5. Unit Converter

Length: Meter, Kilometer, Centimeter, Millimeter, Mile, Yard, Foot, Inch

Weight: Kilogram, Gram, Milligram, Pound, Ounce

Temperature: Celsius, Fahrenheit, Kelvin

Time: Second, Minute, Hour, Day

6. Calculation History
>>>>>>> 06f431c (feat: add unit converter v1.5.0)

View calculation history

Clear calculation history

<<<<<<< HEAD
History is stored in history.json

6. Exit

Close PyCalc safely from the main menu.
=======
Store results in history.json

Technologies

Python

Colorama

Pint

JSON

Python math module

Installation

Clone the repository:

git clone <YOUR-REPOSITORY-URL>
cd PyCalc

Install the required packages:

python -m pip install colorama pint

Run

python main.py
>>>>>>> 06f431c (feat: add unit converter v1.5.0)

Project Structure

PyCalc/
├── main.py
├── Calculator.py
├── QuadraticEquations.py
├── Geometry.py
├── ScientificCalculator.py
<<<<<<< HEAD
├── History.py
├── history.json
└── README.md

Technologies

Python

JSON

Colorama

Python math module

Installation

Clone the repository:

git clone <YOUR-REPOSITORY-URL>
cd PyCalc

Install the required dependency:

pip install colorama

Run

Start PyCalc with:

python3 main.py

Version 1.4.0

This release includes the Scientific Calculator module and integrates it
into the main PyCalc menu.

The project is structured into separate Python modules so that each
feature can be developed and maintained independently.

Author

Ali Hamze

GitHub: AliHamze

License

=======
├── UnitConverter.py
├── History.py
├── history.json
├── README.md
└── .gitignore

Version 1.5.0

This release adds the Unit Converter to PyCalc.

The Unit Converter supports length, weight, temperature, and time conversions using the Pint library. Conversion results are also integrated with the existing calculation history system.

Author

Ali Hamze

GitHub: AliHamzeCS

License

>>>>>>> 06f431c (feat: add unit converter v1.5.0)
This project is for learning and development purposes.
