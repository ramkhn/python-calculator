import time
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b
def main():
    print("=" * 40)
    print("       PYTHON CLI CALCULATOR")
    print("=" * 40)
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("\nEnter choice (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("\n[!] Invalid input. Please enter valid numerical values.")
            return
        # Start timer to measure execution time
        start_time = time.perf_counter()
        
        if choice == '1':
            result = add(num1, num2)
            operation = f"{num1} + {num2}"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = f"{num1} - {num2}"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = f"{num1} * {num2}"
        elif choice == '4':
            result = divide(num1, num2)
            operation = f"{num1} / {num2}"
            
        # End timer
        end_time = time.perf_counter()
        execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds

        print("-" * 40)
        print(f"Result: {operation} = {result}")
        print(f"Execution Time: {execution_time_ms:.6f} ms")
        print("-" * 40)
    else:
        print("\n[!] Invalid operation choice selected.")

if __name__ == "__main__":
    main()
    