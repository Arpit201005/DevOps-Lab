# Exercise 5: Docker Security with AppArmor

## Aim
To secure a Flask application running inside a Docker container using AppArmor security profiles and the Docker Python SDK, and to test restrictions on potentially sensitive operations.

## Technologies Used
- Python
- Flask
- Docker
- Docker Python SDK
- AppArmor
- Ubuntu on WSL2
- Visual Studio Code

## Project Structure

```text
Exercise5/
├── app.py
├── Dockerfile
├── requirements.txt
├── apply_apparmor.py
├── test_restricted_actions.py
└── exercise5.md
```

## Task 1: Create the Flask Application

The Flask application displays a welcome message when accessed through the browser.

**File: `app.py`**

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a secure Flask application running inside a Docker container!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## Task 2: Create the Docker Image

The Dockerfile specifies the base image, working directory, dependencies, exposed port, and startup command.

**File: `Dockerfile`**

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

Build the Docker image:

```bash
docker build -t flask-apparmor .
```

Verify the image:

```bash
docker images flask-apparmor
```

## Task 3: Configure AppArmor

AppArmor is a Linux security module that restricts what programs can access or execute according to a defined security profile. A profile can limit file access, capabilities, and other operations.

The intended profile name for this exercise is:

```text
my-apparmor-profile
```

In a Linux environment with AppArmor enabled, a profile can be installed under `/etc/apparmor.d/`, loaded, and associated with a container using Docker's `--security-opt` option.

Example Docker command:

```bash
docker run --security-opt apparmor=my-apparmor-profile flask-apparmor
```

**Environment limitation:** The exercise was performed using Ubuntu on WSL2. The command below returned `N`:

```bash
cat /sys/module/apparmor/parameters/enabled
```

Therefore, AppArmor enforcement was unavailable in this environment. Actual profile loading and enforcement could not be verified.

## Task 4: Apply the AppArmor Option Using the Docker Python SDK

The `apply_apparmor.py` script uses the Docker Python SDK to build the image, create a container with the requested AppArmor security option, inspect its configuration, and stop and remove it.

Run the script using:

```bash
python3 apply_apparmor.py
```

The script reported the following security option:

```text
apparmor=my-apparmor-profile
```

This confirms that the option was included in the container configuration. It does not confirm that the kernel enforced the profile.

## Task 5: Test Restricted Actions

Run the existing test script:

```bash
python3 test_restricted_actions.py
```

The script tested these commands:

```text
cat /etc/passwd
/bin/bash -c "echo Bash executed"
```

### Observed Results

| Test | Result |
|---|---|
| Read `/etc/passwd` | Command succeeded |
| Execute Bash | Command succeeded |
| AppArmor restriction | Not verified |

The commands were executed directly in the Ubuntu environment rather than inside a container with an enforced AppArmor profile. Therefore, these results do not demonstrate successful AppArmor restriction.

## Verification

The Flask application was started in Docker using:

```bash
docker run -d --name flask-apparmor-test -p 5000:5000 flask-apparmor
```

The container status was checked with:

```bash
docker ps --filter name=flask-apparmor-test
```

The application was accessible at:

http://localhost:5000

The browser displayed:

```text
Hello, this is a secure Flask application running inside a Docker container!
```

**Screenshot evidence:** Attach a screenshot of the Flask application running in the browser and, if required, terminal screenshots showing the Docker container and script output.

## Conclusion

The Flask application was successfully containerized and accessed through Docker. The Docker Python SDK script configured the requested AppArmor security option, and the test script executed its commands. However, AppArmor enforcement could not be verified because it was unavailable in the WSL2 environment. The security portion must be validated on a compatible Linux system with AppArmor enabled before claiming that restricted operations were blocked.
