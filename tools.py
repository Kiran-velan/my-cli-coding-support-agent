import os
import subprocess


def get_current_directory():
    """Return the current working directory."""
    try:
        return os.getcwd()
    except Exception as e:
        return f"Error: {str(e)}"


def list_files(path="."):
    """List files and folders in a directory."""
    try:
        items = os.listdir(path)

        if not items:
            return "Directory is empty."

        return "\n".join(items)

    except Exception as e:
        return f"Error: {str(e)}"


def read_file(path):
    """Read a file and return its contents."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    except Exception as e:
        return f"Error: {str(e)}"


def create_file(path):
    """Create a new file."""
    try:
        if os.path.exists(path):
            return f"Error: '{path}' already exists."

        return f"File '{path}' created successfully."

    except Exception as e:
        return f"Error: {str(e)}"


def write_file(path, content):
    """Overwrite an existing file."""
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"File '{path}' written successfully."

    except Exception as e:
        return f"Error: {str(e)}"


def edit_file(path, action, target_text, new_text):
    """
    Edit a file.

    action:
        replace
        insert_before
        insert_after
    """

    try:

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        occurrences = content.count(target_text)

        if occurrences == 0:
            return "Error: target_text not found."

        if occurrences > 1:
            return (
                f"Error: target_text is ambiguous. "
                f"Found {occurrences} occurrences."
            )

        if action == "replace":
            updated = content.replace(target_text, new_text, 1)

        elif action == "insert_before":
            updated = content.replace(
                target_text,
                new_text + target_text,
                1
            )

        elif action == "insert_after":
            updated = content.replace(
                target_text,
                target_text + new_text,
                1
            )

        else:
            return "Error: Invalid action."

        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)

        return "File edited successfully."

    except Exception as e:
        return f"Error: {str(e)}"


def run_shell(command):
    print(f"\nThe assistant wants to run:\n\n{command}\n")

    # Ask for user permission before executing the command
    permission = input("Allow? (y/n): ").strip().lower()
    if permission != "y":
        return "User denied permission."

    """Run a shell command and return stdout/stderr."""

    try:

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        output = ""

        if result.stdout:
            output += result.stdout

        if result.stderr:
            output += "\nSTDERR:\n"
            output += result.stderr

        if output.strip() == "":
            output = "Command executed successfully."

        return output

    except Exception as e:
        return f"Error: {str(e)}"