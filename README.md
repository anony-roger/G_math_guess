
# 🧮 Math Quiz Game

A simple Python command-line game that quizzes you with randomly generated arithmetic problems. Tracks your performance and time taken to complete the quiz.

## 🚀 Features

- Random generation of math problems using `+`, `-`, and `*`
- Adjustable difficulty and number of questions
- Tracks number of incorrect answers
- Displays total time taken

## 📝 How It Works

1. User starts the game by pressing Enter.
2. The program generates 5 math problems using random numbers from 2 to 17.
3. User answers each question one by one.
4. At the end, it displays how many were wrong and how long it took.

## 🔧 Configuration

Customize quiz settings by changing the following variables in the script:

```python
operand = ["+", "-", "*"]        # Types of operations
min_operand = 2                  # Minimum number value
max_operand = 17                 # Maximum number value
total_questions = 5             # Number of questions in the quiz
