# Interactive Terminal Calculator

print("Welcome to Interactive Calculator!")
print("Type any mathematical expression to evaluate it (e.g., 5+5*2-3/1)")
print("Type 'exit' to quit.\n")

while True:
    user_input = input(">>> ").strip()
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    try:
        # Evaluate the mathematical expression
        result = eval(user_input)
        print("Result:", result)
    except Exception as e:
        print("Invalid expression! Please try again.")

