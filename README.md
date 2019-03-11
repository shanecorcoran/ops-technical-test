# MYOB Pre Interview Test

This is a test Hello World application written in Python using the Flask framework.
The application has the following endpoints:

* **Root (/)** - This is the root URL which will return the text "Hello World".
* **myapplication (/todo/api/v1.0/myapplication)** - This endpoint returns some metadata about the application. Uses api versions.
* **Healthcheck (/healthcheck)** - This endpoint does a status check of the root url.

The deployment code is stored in Github Repo > jenkins > deploy_job > Jenkinsfile.

## Sequence of Jobs:

**1_MYOB_hello_world_deploy_pipeline** - [Deploy Job](https://13.55.189.176/job/MYOB/job/1_MYOB_hello_world_deploy_pipeline/)

This is the deployment job and is built using Jenkins Pipeline.
The pipeline will checkout the git repository, install python, install all application dependencies and unzip the packaged tar file.
Finally it will run the python application as a background process listening on Port 5000.

**2_MYOB_unit_test** - [Unit Tests](https://13.55.189.176/job/MYOB/job/2_MYOB_unit_test/)

The Unit test file checks the following endpoints for a 200 response code:
- Root (/)
- /healthcheck
- /todo/api/v1.0/myapplication

If any of the URLs does not return 200 response then the Job will fail.

**3_MYOB_stop_hello_world** - [Stop Application](https://13.55.189.176/job/MYOB/job/3_MYOB_stop_hello_world/)

This is a simple one line bash command to kill the python process running the application in the background.

Once code has been deployed, check the following URLs to see the responses:
http://13.55.189.176:5000/
http://13.55.189.176:5000/todo/api/v1.0/myapplication
http://13.55.189.176:5000/healthcheck


# NOTES

* The python application currently does not support SSL.
* Port 5000 does not yet get Port 80 traffic as this is currently configured for Jenkins.
