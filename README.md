# Robot Framework Dashboard

![RF WEB UI](https://github.com/molsky/robotframework-webui/blob/master/media/rfwebui.png "UI")

# Documentation
**Note:** This project is still more of less in Proof of Concept state. Software is not in this state suitable for any real
use in live environments.

# Setup

You can either use docker to execute the robotdashboard as a container or you can follow the manual setup to have the full control. 

## Docker Setup
`cd` to the repository and execute the following docker command: 
```
docker build -t robotdashboard:dev . && docker run -p 8000:8000 -v $(pwd)/tests/:/usr/tests/ -v $(pwd)/src/:/usr/work/ -d robotdashboard:dev
```
By default, it will mount all the tests in $(pwd)/tests/ into the tests directory of the container. 

## Manual Setup
1. Install nginx and configure it (see nginx section)
2. Create Python3 virtualenv: `virtualenv -p python3 [envname]`
3. Activate your virtualenv and install requirements `pip install -r requirements.pip`
4. Test that everything works
  * Run `rfwebui.py` in project folder
  * Open browser and go to (by default) `http://127.0.0.1:5000/`
  * Close development server
5. Test Gunicorn's ability to serve the project
  * Run `gunicorn --bind 0.0.0.0:8000 wsgi:app` in project folder
  * Navigate to `localhost`

## nginx configuration
```
sudo touch /etc/nginx/sites-available/flask_project
sudo ln -s /etc/nginx/sites-available/flask_project /etc/nginx/sites-enabled/flask_project
```
Add following lines to `flask_project` file and then restart nginx: `sudo /etc/init.d/nginx restart`
```
server {
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /results {
        include proxy_params;
        alias [path_to_results_folder];
        autoindex on;
    }
}
```

# Technologies
* Python 3.5
* Flask
* jQuery 2
* Bootstrap 3

# Todo
* Automated installation process
* Ability to abort test execution
* Show real time execution status via WEB UI (Console -page)
  * Show newest execution messages in footer section
* Show more test suite related information (documentation, last run time, pass/total ratio, etc.)
* pabot support
* Handle correctly situations when app has more than 1 user at the same time
* Add user roles?
  * Login page
* Update to Bootstrap 4 and jQuery 3 when Bootstrap 4 is ready
* Python 2 support?
