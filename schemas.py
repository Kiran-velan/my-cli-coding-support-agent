TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read the contents of a file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the file"
                    }
                },
                "required": ["path"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_file",
            "description": "Create a new empty file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path of the new file"
                    }
                },
                "required": ["path"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write content to a file. Overwrites existing content.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the file."
                    },
                    "content": {
                        "type": "string",
                        "description": "Complete content to write into the file."
                    }
                },
                "required": ["path", "content"],
                "additionalProperties": False
            }
        }
    },
    {
    "type": "function",
        "function": {
            "name": "list_files",
            "description": (
                "List all files and directories in a directory. "
                "Use this tool to discover the project structure before "
                "reading or editing files if the location is unknown."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": (
                            "Directory path. Use '.' for the current directory."
                        )
                    }
                },
                "required": ["path"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_directory",
            "description": (
                "Return the current working directory. "
                "Use this tool when you need to determine the base path "
                "before locating or accessing files."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_shell",
            "description": (
                "Execute a shell command and return its stdout and stderr. "
                "Use this tool only when necessary to inspect the project or "
                "verify changes."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "Shell command to execute"
                    }
                },
                "required": ["command"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "edit_file",
            "description": (
                "Modify an existing file by replacing text or inserting text "
                "before or after a unique target text. The target text must "
                "match exactly one location in the file."
                "If you do not know the exact target_text, "
                "first call read_file() to inspect the file. "
                "The target_text should uniquely identify a single location."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the file."
                    },
                    "action": {
                        "type": "string",
                        "enum": [
                            "replace",
                            "insert_before",
                            "insert_after"
                        ],
                        "description": "The type of edit to perform."
                    },
                    "target_text": {
                        "type": "string",
                        "description": (
                            "A unique block of text in the file that identifies "
                            "where the edit should occur."
                        )
                    },
                    "new_text": {
                        "type": "string",
                        "description": (
                            "Replacement text or text to insert."
                        )
                    }
                },
                "required": [
                    "path",
                    "action",
                    "target_text",
                    "new_text"
                ],
                "additionalProperties": False
            }
        }
    }
]