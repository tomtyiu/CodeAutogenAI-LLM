## AutoGen Claude 3.5 Sonnet / OpenAI GPT 4o
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

## Installation
To use AutoGen Claude 3.5 Sonnet, you need to have Python installed on your system. Follow the steps below to set up the project:

Clone the repository:
<code>
git clone https://github.com/yourusername/AutoGen_Claude_3.5_Sonnet.git
cd AutoGen_Claude_3.5_Sonnet
</code>

Install dependencies:
<code>
Anthropic:
pip install pyautogen["anthropic"]
or
!pip install pyautogen["anthropic"]

OpenAI
pip install --upgrade openai
</code>

Setup key
Windows
<code>
setx ANTHROPIC_API_KEY "your-api-key-here"
setx OPENAI_API_KEY "your-api-key-here"
</code>

Mac/Linux
<code>
export ANTHROPIC_API_KEY-"your-api-key-here"
export OPENAI_API_KEY='your-api-key-here'
</code>

Usage
The main script for AutoGen Claude 3.5 Sonnet is AutoGen_Claude_3.5_Sonnet.py. You can run this script to access the different functionalities of the tool.

Run the script:
<code>
python AutoGen_Claude_3.5_Sonnet.py
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
