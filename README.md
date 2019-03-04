MYOB Pre Interview Test - README

This is a test Hello World application written in Python using the Flask framework.
The application has the following endpoints:
   1. Root (/) - This is the root URL which will return the text "Hello World".
   2. myapplication - This endpoint returns some metadata about the application.
   3. healtcheck - This endpoint does a status check of the root url.

The Application also has a couple of Unit tests.

Deployment is done via Jenkins job from the following URL:
https://13.239.146.81/job/MYOB/job/hello_world_deploy_pipeline/

Unit Tests can be run from the following URL:
https://13.239.146.81/job/MYOB/job/unit_test/

The deployment code is stored in Github Repo > jenkins > deploy_job > Jenkinsfile.