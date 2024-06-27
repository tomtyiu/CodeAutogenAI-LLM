//created by GPT 4o and Thomas Yiu

import autogen
from autogen import UserProxyAgent
# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample
import os

llm_config = {
    "config_list": [{"model": "gpt-3.5-turbo-0125", "api_key": os.environ["OPENAI_API_KEY"]}],
}

# You can also set config_list directly as a list, for example, config_list = [{'model': 'gpt-4', 'api_key': '<your OpenAI API key here>'},]
assistant = autogen.AssistantAgent(name="assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", human_input_mode="TERMINATE", code_execution_config={"work_dir": "coding", "use_docker": False}) # IMPORTANT: set to True to run code in docker, recommended

autogen_input=input(f"Write your prompt for autogen: (default: {"Plot a chart of NVDA and TESLA stock price change YTD."}):")
if autogen_input == "":
    autogen_input = "Plot a chart of NVDA and TESLA stock price change YTD."
    
user_proxy.initiate_chat(assistant, message=autogen_input)
# This initiates an automated chat between the two agents to solve the task
