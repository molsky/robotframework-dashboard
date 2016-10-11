# Robot Framework Web UI

![RF WEB UI](https://github.com/molsky/robotframework-webui/blob/master/media/rfwui.png "UI")

# Documentation
Nothing yet.

# Setup
* First:
  * Update settings.ini file under app_configs folder (absolute path to folder where tests are located)
  * Install nginx and configure it (see nginx section)

1. Create Python3 virtualenv: 'virtualenv -p python3 envname'
2. Activate virtualenv and install requirements 'pip install -r requirements.pip'
3. Test that everything works
  * Run 'rfwebui.py' in project folder
  * Open browser and go to (by default) 'http://127.0.0.1:5000/'
  * Close development server
4. Test Gunicorn's ability to serve the project
  * Run 'gunicorn --bind 0.0.0.0:8000 wsgi:app' in project folder

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
* Python 2 support
* Ability to abort test execution
* Show real time execution status via WEB UI (Console -page)
  * Show newest execution messages in footer section
* Add user roles?
  * Login page
* Settings page or panel to enable configuration via WEB UI
* Search/filter features
* pabot support
* Handle correctly situations when app has more than 1 user at the same time
* Update to Bootstrap 4 and jQuery 3 when Bootstrap 4 is ready
