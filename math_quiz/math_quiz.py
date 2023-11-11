import random

def generate_random_integer(min_value, max_value):
    """
    Generates a random integer between min_value and max_value (inclusive).

    param min_value: Minimum value for the random integer
    param max_value: Maximum value for the random integer
    return: Random integer
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generates a random mathematical operator (+, -, *).

    return: Random operator
    """
    return random.choice(['+', '-', '*'])


def calculate_result(num1, num2, operator):
    """
    Calculates the result of a mathematical operation.

    param num1: First operand
    param num2: Second operand
    param operator: Mathematical operator (+, -, *)
    return: Tuple containing the problem expression and the correct answer
    """
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    problem_expression = f"{num1} {operator} {num2}"
    return problem_expression, result


def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = calculate_result(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_answer = 0

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
