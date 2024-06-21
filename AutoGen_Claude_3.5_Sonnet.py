import anthropic

class AutoGen:
    def __init__(self):
        self.client = anthropic.Anthropic()

    def process_single_input(self, input_code):
        results = {}
        results['documentation'] = self.generate_documentation(input_code)
        results['code_completion'] = self.complete_code(input_code)
        results['code_review'] = self.review_code(input_code)
        results['tests'] = self.generate_tests(input_code)
        return results

    def generate_code(self, prompt=None):
        if prompt is None:
            prompt = input("Enter a prompt to generate code: ")
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0,
            system="You are an expert programmer. Provide concise, efficient code solutions.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Generate code for: {prompt}"
                        }
                    ]
                }
            ]
        )
        return message.content

    def generate_documentation(self, code=None):
        if code is None:
            code = input("Enter the code to document:\n")
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0,
            system="You are an expert in writing clear and comprehensive code documentation.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Generate documentation for this code:\n\n{code}"
                        }
                    ]
                }
            ]
        )
        return message.content

    def complete_code(self, partial_code=None):
        if partial_code is None:
            partial_code = input("Enter the partial code to complete:\n")
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0,
            system="You are an expert programmer. Complete the given code snippet in a logical and efficient manner.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Complete this code:\n\n{partial_code}"
                        }
                    ]
                }
            ]
        )
        return message.content

    def review_code(self, code=None):
        if code is None:
            code = input("Enter the code to review:\n")
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0,
            system="You are an experienced code reviewer. Provide constructive feedback and suggestions for improvement.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Review this code and provide feedback:\n\n{code}"
                        }
                    ]
                }
            ]
        )
        return message.content

    def generate_tests(self, code=None):
        if code is None:
            code = input("Enter the code to generate tests for:\n")
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0,
            system="You are an expert in writing comprehensive unit tests. Generate thorough test cases for the given code.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Generate unit tests for this code:\n\n{code}"
                        }
                    ]
                }
            ]
        )
        return message.content

    def debug_code(self, code=None, error_message=None):
        if code is None:
            code = input("Enter the code to debug:\n")
        if error_message is None:
            error_message = input("Enter the error message:\n")
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0,
            system="You are an expert debugger. Analyze the code and error message to provide solutions.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Debug this code with the following error:\n\nCode:\n{code}\n\nError:\n{error_message}"
                        }
                    ]
                }
            ]
        )
        return message.content

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
