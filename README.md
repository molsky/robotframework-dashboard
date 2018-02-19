# Robot Framework Dashboard

![RF WEB UI](https://github.com/molsky/robotframework-webui/blob/master/media/rfwebui.png "UI")

# Documentation
**Notes:**
* This project is still more of less in Proof of Concept state. Software is not in this state suitable for any real
use in live environments.
* This application should never be set visible to public Internet when making changes to nginx config files.

# Setup
1. Install nginx
2. Run `./setup.sh` in project's root folder
3. Run `source rfd-venv/bin/activate` and then navigate to rfwebui folder and run `gunicorn --bind 0.0.0.0:8000 wsgi:app`
4. Navigate to `localhost:8000`

## nginx configuration manually
```
sudo touch /etc/nginx/sites-available/rf_dashboard
sudo ln -s /etc/nginx/sites-available/rf_dashboard /etc/nginx/sites-enabled/rf_dashboard
```
Add following lines to `rf_dashboard` file and then restart nginx with `systemctl restart nginx.service` or
`service nginx restart`
```
server {
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /results {
        include proxy_params;
        # By default rfwebui/results
        alias [complete_path_to_results_folder];
        autoindex on;
    }
}
```

# Technologies
* Python 3
* Flask
* jQuery 3
* Bootstrap 3

# Todo
* Ability to abort test execution
* Show real time execution status via WEB UI (Console -page)
  * Show newest execution messages in footer section
* Show more test suite related information & statistics (documentation, last run time, pass/total ratio, etc.)
* pabot support
* Module bundler for JS/HTML/CSS files (for example webpack with npm)
* Update to Bootstrap 4 when Bootstrap 4 is ready
