# PyCalc v1.7.0

## Advanced Math Toolkit

PyCalc is a modular Python command-line math toolkit that provides
mathematical operations and utilities through a simple menu-based interface.

## Version

v1.7.0

## Features

### 1. Basic Calculator

- Addition
- Subtraction
- Multiplication
- Division
- Power
- Modulus

### 2. Scientific Calculator

- Square Root
- Cube Root
- Sine
- Cosine
- Tangent
- Logarithm
- Factorial
- Arcsine
- Arccosine
- Arctangent

### 3. Quadratic Equations

- Solve one quadratic equation
- Solve systems of two equations
- Solve systems of three equations
- Discriminant and root analysis
- Real and complex roots

### 4. Geometry

- Circle
- Rectangle
- Square
- Triangle
- Cube
- Sphere
- Cylinder

### 5. Statistics

- Mean
- Median
- Mode
- Range
- Variance
- Standard Deviation

### 6. Unit Converter

#### Length
- Meter
- Kilometer
- Centimeter
- Millimeter
- Mile
- Yard
- Foot
- Inch

#### Weight
- Kilogram
- Gram
- Milligram
- Pound
- Ounce

#### Temperature
- Celsius
- Fahrenheit
- Kelvin

#### Time
- Second
- Minute
- Hour
- Day

### 7. Calculation History

- Save calculations
- View calculation history
- Clear calculation history
- JSON-based history storage

### 8. Settings

- Set decimal precision
- Set calculation delay
- Reset settings to default
- JSON-based settings storage

## v1.7.0 Changes

### Settings System

Added a settings system that allows users to customize PyCalc.

### Decimal Precision

Users can choose the number of decimal places displayed in calculation results.

Supported precision:

- 0 to 10 decimal places

### Calculation Delay

Users can customize the delay used by PyCalc.

### Reset Settings

Users can restore the default settings:

- Decimal precision: 2
- Calculation delay: 1 second

### Settings Storage

Settings are stored in:

`settings.json`

## Technologies

- Python
- JSON
- Colorama
- Pint

## Project Structure

```text
PyCalc/
│
├── Calculator.py
├── ScientificCalculator.py
├── QuadraticEquations.py
├── Geometry.py
├── Statistics.py
├── UnitConverter.py
├── History.py
├── Settings.py
├── main.py
│
├── history.json
├── settings.json
├── .gitignore
└── README.md