import os

from typing_extensions import Annotated

import autogen
from autogen import UserProxyAgent
from autogen import AssistantAgent

config_list_claude = [
    {
        # Choose your model name.
        "model": "claude-3-5-sonnet-20240620",
        # You need to provide your API key here.
        "api_key": os.getenv("ANTHROPIC_API_KEY"),
        "api_type": "anthropic",
    }
]

assistant = autogen.AssistantAgent(
    "assistant",
    llm_config={
        "config_list": config_list_claude,
    },
)

user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    human_input_mode="NEVER",
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,
    },
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    max_consecutive_auto_reply=1,
)

autogen_input=input(f"Write your prompt for autogen: (default: {"Write a python program to print the first 10 numbers of the Fibonacci sequence"}):")
if autogen_input == "":
    autogen_input = "Write a python program to print the first 10 numbers of the Fibonacci sequence"


user_proxy.initiate_chat(
    assistant, message=autogen_input
)
