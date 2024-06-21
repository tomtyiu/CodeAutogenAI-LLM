## AutoGen Claude 3.5 Sonnet
Welcome to AutoGen Claude 3.5 Sonnet, a comprehensive tool for automating various code-related tasks using the Claude 3.5 Sonnet model from Anthropic. This README provides instructions on how to set up, use, and contribute to this project.

## Table of Contents

Introduction
Features
Installation
Usage
Examples
Contributing
License

## Introduction

AutoGen Claude 3.5 Sonnet is designed to help developers streamline their workflow by providing capabilities for code generation, documentation, code completion, code review, test generation, and debugging. Utilizing the advanced natural language processing capabilities of the Claude 3.5 Sonnet model, this tool aims to enhance productivity and code quality.

## Features
Single Input Processing: Automatically generates documentation, completes code, reviews code, and generates tests for a given input.
Code Generation: Generate new code based on a given prompt.
Documentation Generation: Create clear and comprehensive documentation for any piece of code.
Code Completion: Complete partially written code snippets.
Code Review: Provide constructive feedback and suggestions for improvement on existing code.
Test Generation: Generate thorough unit tests for a given codebase.
Code Debugging: Analyze and debug code based on provided error messages.
Installation
To use AutoGen Claude 3.5 Sonnet, you need to have Python installed on your system. Follow the steps below to set up the project:

Clone the repository:
<code>
git clone https://github.com/yourusername/AutoGen_Claude_3.5_Sonnet.git
cd AutoGen_Claude_3.5_Sonnet
</code>

Install dependencies:
<code>
pip install anthropic
</code>

Setup key
Windows
<code>
setx ANTHROPIC_API_KEY "your-api-key-here"
</code>

Mac/Linux
<code>
setx ANTHROPIC_API_KEY "your-api-key-here"
</code>

Usage
The main script for AutoGen Claude 3.5 Sonnet is AutoGen_Claude_3.5_Sonnet.py. You can run this script to access the different functionalities of the tool.

Run the script:

Copy code
python AutoGen_Claude_3.5_Sonnet.py
Menu Options:

Upon running the script, you will be presented with a menu offering various options:

1. Single Input AutoGen
2. Generate Code
3. Generate Documentation
4. Complete Code
5. Review Code
6. Generate Tests
7. Debug Code
8. Exit

Select the desired option by entering the corresponding number.

Example Menu Interaction:

AutoGen Menu:
1. Single Input AutoGen
2. Generate Code
3. Generate Documentation
4. Complete Code
5. Review Code
6. Generate Tests
7. Debug Code
8. Exit

Enter your choice (1-8): 1
Examples

Single Input AutoGen
For processing a single input, enter the code you want to process, and AutoGen will generate documentation, complete the code, review it, and generate tests:

<code>
Enter your code for AutoGen processing:
def add(a, b):
    return a + b
</code>

Code Generation
<code>
Generate code based on a prompt:

Enter a prompt to generate code: Create a function that calculates the factorial of a number.
</code>


Documentation Generation
Generate documentation for existing code:

<code>
Enter the code to document:
def multiply(a, b):
    return a * b
</code>

Code Completion
Complete a partially written code snippet:

<code>
Enter the partial code to complete:
def divide(a, b):
    if b != 0:
</code>

Code Review
Review existing code and provide feedback:

<code>
Enter the code to review:
def subtract(a, b):
    return a - b
</code>
    
Test Generation
Generate unit tests for existing code:

<code>
Enter the code to generate tests for:
def is_even(n)
    return n % 2 == 0
</code>


Code Debugging
Debug code with a given error message:
<code>
Enter the code to debug:
def mod(a, b):
    return a % b

Enter the error message:
ZeroDivisionError: division by zero
</code>

Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch (<code>git checkout -b feature-branch</code>).
Commit your changes (<code>git commit -am 'Add new feature' </code>).
Push to the branch (<code>git push origin feature-branch</code>).
Create a new Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.FR
