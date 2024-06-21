from openai import OpenAI

class AutoGen:
    def __init__(self):
        self.client = OpenAI()

    def process_single_input(self, input_code):
        results = {}
        results['documentation'] = self.generate_documentation(input_code)
        results['code_completion'] = self.complete_code(input_code)
        results['code_review'] = self.review_code(input_code)
        results['tests'] = self.generate_tests(input_code)
        return results

    def verify_output(self, task, input_data, output_data):
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert programmer. Verify the following output."},
                {"role": "user", "content": f"Task: {task}\nInput: {input_data}\nOutput: {output_data}\nVerify the output and provide feedback or corrections if necessary."}
            ]
        )
        return response.choices[0].message.content

    def generate_code(self, prompt=None):
        if prompt is None:
            prompt = input("Enter a prompt to generate code: ")
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert programmer. Provide concise, efficient code solutions."},
                {"role": "user", "content": f"Generate code for: {prompt}"}
            ]
        )
        generated_code = response.choices[0].message.content
        verification = self.verify_output("Generate Code", prompt, generated_code)
        print (generated_code)
        print (verification)
        return verification

    def generate_documentation(self, code=None):
        if code is None:
            code = input("Enter the code to document:\n")
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert in writing clear and comprehensive code documentation."},
                {"role": "user", "content": f"Generate documentation for this code:\n\n{code}"}
            ]
        )
        documentation = response.choices[0].message.content
        verification = self.verify_output("Generate Documentation", code, documentation)
        print (documentation)
        print (verification)
        return verification

    def complete_code(self, partial_code=None):
        if partial_code is None:
            partial_code = input("Enter the partial code to complete:\n")
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert programmer. Complete the given code snippet in a logical and efficient manner."},
                {"role": "user", "content": f"Complete this code:\n\n{partial_code}"}
            ]
        )
        completed_code = response.choices[0].message.content
        verification = self.verify_output("Complete Code", partial_code, completed_code)
        print (completed_code)
        print (verification)
        return verification

    def review_code(self, code=None):
        if code is None:
            code = input("Enter the code to review:\n")
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an experienced code reviewer. Provide constructive feedback and suggestions for improvement."},
                {"role": "user", "content": f"Review this code and provide feedback:\n\n{code}"}
            ]
        )
        review = response.choices[0].message.content
        verification = self.verify_output("Review Code", code, review)
        print (review)
        print (verification)
        return verification

    def generate_tests(self, code=None):
        if code is None:
            code = input("Enter the code to generate tests for:\n")
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert in writing comprehensive unit tests. Generate thorough test cases for the given code."},
                {"role": "user", "content": f"Generate unit tests for this code:\n\n{code}"}
            ]
        )
        tests = response.choices[0].message.content
        verification = self.verify_output("Generate Tests", code, tests)
        print (tests)
        print (verification)
        return verification

    def debug_code(self, code=None, error_message=None):
        if code is None:
            code = input("Enter the code to debug:\n")
        if error_message is None:
            error_message = input("Enter the error message:\n")
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert debugger. Analyze the code and error message to provide solutions."},
                {"role": "user", "content": f"Debug this code with the following error:\n\nCode:\n{code}\n\nError:\n{error_message}"}
            ]
        )
        debug_solution = response.choices[0].message.content
        verification = self.verify_output("Debug Code", f"Code:\n{code}\nError:\n{error_message}", debug_solution)
        print (debug_solution)
        print (verification)
        return verification

def main():
    autogen = AutoGen()
    
    while True:
        print("\nAutoGen Menu:")
        print("1. Single Input AutoGen")
        print("2. Generate Code")
        print("3. Generate Documentation")
        print("4. Complete Code")
        print("5. Review Code")
        print("6. Generate Tests")
        print("7. Debug Code")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            input_code = input("Enter your code for AutoGen processing:\n")
            results = autogen.process_single_input(input_code)
            for key, value in results.items():
                print(f"\n{key.replace('_', ' ').title()}:")
                print(value)
        elif choice == '2':
            result = autogen.generate_code()
        elif choice == '3':
            result = autogen.generate_documentation()
        elif choice == '4':
            result = autogen.complete_code()
        elif choice == '5':
            result = autogen.review_code()
        elif choice == '6':
            result = autogen.generate_tests()
        elif choice == '7':
            result = autogen.debug_code()
        elif choice == '8':
            print("Exiting AutoGen. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue
        
        if choice != '1':
            print("\nResult:")
            print(result)

if __name__ == "__main__":
    main()
