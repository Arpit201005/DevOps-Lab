
import subprocess

def test_command(command):
    print(f"\nTesting command: {command}")
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print("Command succeeded.")
            print(result.stdout[:300])
        else:
            print("Command failed or was denied.")
            print(result.stderr[:300])
    except Exception as e:
        print(f"Error: {e}")

test_command(["cat", "/etc/passwd"])
test_command(["/bin/bash", "-c", "echo Bash executed"])
