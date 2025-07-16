import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Kalkulator {
    private List<String> history;

    public Kalkulator() {
        history = new ArrayList<>();
    }

    public double add(double x, double y) {
        double result = x + y;
        history.add(x + " + " + y + " = " + result);
        return result;
    }

    public double subtract(double x, double y) {
        double result = x - y;
        history.add(x + " - " + y + " = " + result);
        return result;
    }

    public double multiply(double x, double y) {
        double result = x * y;
        history.add(x + " * " + y + " = " + result);
        return result;
    }

    public double divide(double x, double y) {
        if (y == 0) {
            System.out.println("Error! Division by zero.");
            return Double.NaN;
        }
        double result = x / y;
        history.add(x + " / " + y + " = " + result);
        return result;
    }

    public double squareRoot(double x) {
        double result = Math.sqrt(x);
        history.add("√" + x + " = " + result);
        return result;
    }

    public double power(double x, double y) {
        double result = Math.pow(x, y);
        history.add(x + " ^ " + y + " = " + result);
        return result;
    }

    public double sin(double x) {
        double result = Math.sin(Math.toRadians(x));
        history.add("sin(" + x + ") = " + result);
        return result;
    }

    public double cos(double x) {
        double result = Math.cos(Math.toRadians(x));
        history.add("cos(" + x + ") = " + result);
        return result;
    }

    public double tan(double x) {
        double result = Math.tan(Math.toRadians(x));
        history.add("tan(" + x + ") = " + result);
        return result;
    }

    public double log(double x) {
        if (x <= 0) {
            System.out.println("Error! Logarithm of non-positive number.");
            return Double.NaN;
        }
        double result = Math.log(x);
        history.add("log(" + x + ") = " + result);
        return result;
    }

    public void printHistory() {
        System.out.println("Calculation History:");
        for (String entry : history) {
            System.out.println(entry);
        }
    }

    public static void main(String[] args) {
        Kalkulator calc = new Kalkulator();
        Scanner scanner = new Scanner(System.in);
        String command;

        System.out.println("Advanced Calculator");
        System.out.println("Type 'exit' to quit");
        System.out.println("Type 'history' to view calculation history");
        System.out.println("Available operations: +, -, *, /, sqrt, ^, sin, cos, tan, log");

        while (true) {
            System.out.print("Enter command: ");
            command = scanner.nextLine();

            if (command.equalsIgnoreCase("exit")) {
                break;
            } else if (command.equalsIgnoreCase("history")) {
                calc.printHistory();
                continue;
            }

            String[] parts = command.split(" ");
            if (parts.length < 3) {
                System.out.println("Invalid command. Please enter a valid operation.");
                continue;
            }

            double x = Double.parseDouble(parts[0]);
            String operator = parts[1];
            double y = Double.parseDouble(parts[2]);
            double result = 0;

            switch (operator) {
                case "+":
                    result = calc.add(x, y);
                    break;
                case "-":
                    result = calc.subtract(x, y);
                    break;
                case "*":
                    result = calc.multiply(x, y);
                    break;
                case "/":
                    result = calc.divide(x, y);
                    break;
                case "sqrt":
                    result = calc.squareRoot(x);
                    break;
                case "^":
                    result = calc.power(x, y);
                    break;
                case "sin":
                    result = calc.sin(x);
                    break;
                case "cos":
                    result = calc.cos(x);
                    break;
                case "tan":
                    result = calc.tan(x);
                    break;
                case "log":
                    result = calc.log(x);
                    break;
                default:
                    System.out.println("Invalid operator.");
                    continue;
            }
            System.out.println("Result: " + result);
        }
        scanner.close();
    }
}
