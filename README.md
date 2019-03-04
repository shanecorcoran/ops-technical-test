MYOB Pre Interview Test - README

This is a test Hello World application written in Python using the Flask framework.
The application has the following endpoints:
   1. Root (/) - This is the root URL which will return the text "Hello World".
   2. myapplication - This endpoint returns some metadata about the application.
   3. healthcheck - This endpoint does a status check of the root url.

The deployment code is stored in Github Repo > jenkins > deploy_job > Jenkinsfile.

Sequence:

1. 1_MYOB_hello_world_deploy_pipeline
   https://13.239.146.81/job/MYOB/job/1_MYOB_hello_world_deploy_pipeline/

This is the main deployment job and is built using Jenkins Pipeline.
The pipeline will checkout the git repository, install python, install all application dependencies and unzip the packaged tar file.
Finally it will run the python application as a background process listening on Port 5000.

2. 2_MYOB_unit_test
   https://13.239.146.81/job/MYOB/job/2_MYOB_unit_test/

The Unit test file checks the following endpoints for a 200 response code:
- Root (/)
- /healthcheck
- /todo/api/v1.0/myapplication

If any of the URLs does not return 200 response then the Job will fail.

3. 3_MYOB_stop_hello_world
   https://13.239.146.81/job/MYOB/job/3_MYOB_stop_hello_world/

This is a simple one line bash command to kill the python process running the application in the background.