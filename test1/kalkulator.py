import math
import cmath
import numpy as np
from statistics import mean, median, mode
import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
import matplotlib.pyplot as plt
import sympy as sp

class Calculator:
    def __init__(self):
        self.history = []
        self.default_units = 'metric'  # User preference for units

    def add(self, x, y):
        result = x + y
        self.history.append(f"{datetime.now()}: {x} + {y} = {result}")
        return result

    def subtract(self, x, y):
        result = x - y
        self.history.append(f"{datetime.now()}: {x} - {y} = {result}")
        return result

    def multiply(self, x, y):
        result = x * y
        self.history.append(f"{datetime.now()}: {x} * {y} = {result}")
        return result

    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero."
        result = x / y
        self.history.append(f"{datetime.now()}: {x} / {y} = {result}")
        return result

    def square_root(self, x):
        result = math.sqrt(x)
        self.history.append(f"{datetime.now()}: √{x} = {result}")
        return result

    def power(self, x, y):
        result = x ** y
        self.history.append(f"{datetime.now()}: {x} ^ {y} = {result}")
        return result

    def percentage(self, x, y):
        result = (x * y) / 100
        self.history.append(f"{datetime.now()}: {y}% of {x} = {result}")
        return result

    def sin(self, x):
        result = math.sin(math.radians(x))
        self.history.append(f"{datetime.now()}: sin({x}) = {result}")
        return result

    def cos(self, x):
        result = math.cos(math.radians(x))
        self.history.append(f"{datetime.now()}: cos({x}) = {result}")
        return result

    def tan(self, x):
        result = math.tan(math.radians(x))
        self.history.append(f"{datetime.now()}: tan({x}) = {result}")
        return result

    def log(self, x, base=math.e):
        if x <= 0:
            return "Error! Logarithm of non-positive number."
        result = math.log(x, base)
        self.history.append(f"{datetime.now()}: log({x}, {base}) = {result}")
        return result

    def matrix_add(self, A, B):
        return np.add(A, B)

    def matrix_subtract(self, A, B):
        return np.subtract(A, B)

    def matrix_multiply(self, A, B):
        return np.matmul(A, B)

    def calculate_expression(self, expression):
        try:
            result = eval(expression)
            self.history.append(f"{datetime.now()}: {expression} = {result}")
            return result
        except Exception as e:
            return f"Error: {str(e)}"

    def clear_history(self):
        self.history.clear()
        return "History cleared."

    def get_history(self):
        return self.history

    def calculate_statistics(self, data):
        return {
            'mean': mean(data),
            'median': median(data),
            'mode': mode(data)
        }

    def convert_units(self, value, from_unit, to_unit):
        conversions = {
            'meters_to_feet': value * 3.28084,
            'feet_to_meters': value / 3.28084,
            'celsius_to_fahrenheit': (value * 9/5) + 32,
            'fahrenheit_to_celsius': (value - 32) * 5/9,
            'kilograms_to_pounds': value * 2.20462,
            'pounds_to_kilograms': value / 2.20462,
        }
        return conversions.get(f"{from_unit}_to_{to_unit}", "Invalid conversion")

    def save_history(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.history, f)

    def load_history(self, filename):
        with open(filename, 'r') as f:
            self.history = json.load(f)

    def plot_function(self, func, x_range):
        x = np.linspace(x_range[0], x_range[1], 100)
        y = eval(func)
        plt.plot(x, y)
        plt.title(f"Plot of {func}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid()
        plt.show()

    def symbolic_calculation(self, expression):
        x = sp.symbols('x')
        expr = sp.sympify(expression)
        return expr

def main():
    calc = Calculator()
    print("Advanced Calculator")
    print("Type 'exit' to quit")
    print("Type 'history' to view calculation history")
    print("Type 'clear' to clear history")
    print("Type 'save' to save history to a file")
    print("Type 'load' to load history from a file")
    print("Type 'plot' to plot a function")
    print("Type 'symbolic' to perform symbolic calculations")

    while True:
        expression = input("Enter expression: ")

        if expression.lower() == 'exit':
            break
        elif expression.lower() == 'history':
            print("Calculation History:")
            for entry in calc.get_history():
                print(entry)
            continue
        elif expression.lower() == 'clear':
            print(calc.clear_history())
            continue
        elif expression.lower() == 'save':
            filename = input("Enter filename to save history: ")
            calc.save_history(filename)
            print(f"History saved to {filename}.")
            continue
        elif expression.lower() == 'load':
            filename = input("Enter filename to load history: ")
            calc.load_history(filename)
            print(f"History loaded from {filename}.")
            continue
        elif expression.lower() == 'plot':
            func = input("Enter function to plot (e.g., np.sin(x)): ")
            x_range_input = input("Enter x range (e.g., -10, 10): ")
            try:
                x_range = [float(x) for x in x_range_input.split(",")]
                if len(x_range) != 2:
                    raise ValueError("Please provide exactly two values.")
            except ValueError as e:
                print(f"Invalid input for x range: {e}")
                continue
            calc.plot_function(func, x_range)
            continue
        elif expression.lower() == 'symbolic':
            sym_expr = input("Enter symbolic expression (e.g., x**2 + 2*x + 1): ")
            result = calc.symbolic_calculation(sym_expr)
            print(f"Symbolic result: {result}")
            continue

        result = calc.calculate_expression(expression)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
