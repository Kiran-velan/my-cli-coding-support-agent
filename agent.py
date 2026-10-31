import json

from llm_client import chat_completion
from schemas import TOOLS
from prompts import SYSTEM_PROMPT

from tools import (
    get_current_directory,
    list_files,
    read_file,
    create_file,
    write_file,
    edit_file,
    run_shell,
)


class Agent:

    MAX_HISTORY = 25
    MAX_ITERATIONS = 10

    def __init__(self):

        self.system_message = {
            "role": "system",
            "content": SYSTEM_PROMPT
        }

        # Everything except the system prompt
        self.conversation = []

        self.tool_map = {
            "get_current_directory": get_current_directory,
            "list_files": list_files,
            "read_file": read_file,
            "create_file": create_file,
            "write_file": write_file,
            "edit_file": edit_file,
            "run_shell": run_shell,
        }

    def trim_history(self):
        """
        Keep the system prompt and only the latest conversation.
        """

        if len(self.conversation) > self.MAX_HISTORY:
            self.conversation = self.conversation[-self.MAX_HISTORY:]

    def chat(self, user_input):

        # Add user message
        self.conversation.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        for _ in range(self.MAX_ITERATIONS):

            # Trim history before sending to the model
            self.trim_history()

            messages = [
                self.system_message,
                *self.conversation
            ]

            response = chat_completion(
                messages=messages,
                tools=TOOLS,
            )

            message = response.choices[0].message

            # Save assistant response
            assistant_message = {
                "role": "assistant"
            }

            if message.content:
                assistant_message["content"] = message.content

            if message.tool_calls:
                assistant_message["tool_calls"] = message.tool_calls

            self.conversation.append(assistant_message)

            # No tool calls -> final answer
            if not message.tool_calls:
                return message.content
            


            # Execute tool calls
            for tool_call in message.tool_calls:

                tool_name = tool_call.function.name

                arguments = json.loads(tool_call.function.arguments)

                print(f"\nUsing tool: {tool_name}")
                print(arguments)

                tool_function = self.tool_map[tool_name]

                result = tool_function(**arguments)

                print(f"\nObservation:\n{result}\n")

                self.conversation.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(result)
                    }
                )

        return "Stopped after reaching the maximum number of tool iterations."