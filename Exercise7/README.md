# Exercise 7: Introduction to CI and Jenkins

## 1. Objective

To understand the basics of Continuous Integration (CI) and learn how to run Jenkins using Docker, access the Jenkins web interface, and verify that Jenkins is running successfully.

## 2. Technologies Used

- **Jenkins** – Automation server used for CI/CD.
- **Docker** – Used to run Jenkins inside a container.
- **Web Browser** – Used to access the Jenkins dashboard.

## 3. Run Jenkins Using Docker

The following command can be used to run Jenkins in a Docker container on a fresh installation:

```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
```

Check the container status using:

```bash
docker ps -a
```

**Note:** Jenkins was already running from Exercise 6, so the existing container was reused instead of creating a second container.

## 4. Retrieve the Initial Administrator Password

For a new Jenkins installation, the initial administrator password can be retrieved using:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

This command is required only when completing the initial setup of a new Jenkins instance.

## 5. Access Jenkins

Open the following URL in a web browser:

http://localhost:8080/

The initial setup of Jenkins involves:

1. Entering the initial administrator password.
2. Installing the suggested plugins.
3. Creating the first administrator user.
4. Configuring the Jenkins URL.
5. Completing the setup and opening the dashboard.

For this exercise, the existing Jenkins instance was already configured and accessible.

## 6. Verification

The following checks were completed:

- Jenkins was accessible at `http://localhost:8080/`.
- The Jenkins sign-in page was displayed.
- The Jenkins dashboard loaded successfully after signing in.
- The existing `Delivery-Metrics-Pipeline` job was visible.
- Successful build #12 was displayed on the dashboard.

## 7. Screenshots
### Jenkins Sign-in Page

![Jenkins Sign-in Page](Screenshots/IMAGE_LOGIN.png)

### Jenkins Dashboard

![Jenkins Dashboard](Screenshots/IMAGE_DASHBOARD.png)

## 8. Conclusion

This exercise demonstrates how Jenkins can be run using Docker and accessed through a web browser. It introduces the initial setup process, administrator access, and the Jenkins dashboard. The existing Jenkins installation was verified successfully and provides a foundation for understanding Continuous Integration and automation pipelines.
