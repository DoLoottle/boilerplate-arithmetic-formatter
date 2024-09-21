def arithmetic_arranger(problems, show_answers=False):
    # Error handling
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top_lines = []
    bottom_lines = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        num1, operator, num2 = parts
        
        # Validate operator
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        # Validate numbers
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate the answer
        if operator == '+':
            answer = str(int(num1) + int(num2))
        else:
            answer = str(int(num1) - int(num2))

        # Find the width for formatting
        width = max(len(num1), len(num2)) + 2  # +2 for operator and space
        
        # Append to lists
        top_lines.append(num1.rjust(width))
        bottom_lines.append(operator + ' ' + num2.rjust(width - 2))
        dashes.append('-' * width)
        answers.append(answer.rjust(width))

    # Join the lines with spaces
    arranged_problems = "    ".join(top_lines) + "\n" + "    ".join(bottom_lines) + "\n" + "    ".join(dashes)

    if show_answers:
        arranged_problems += "\n" + "    ".join(answers)

    return arranged_problems

# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
