# Robot Framework Web UI

![RF WEB UI](https://github.com/molsky/robotframework-webui/blob/master/media/rfwui.png "UI")

# Documentation
Nothing yet.

# Setup
First: update settings.ini file under app_configs folder (absolute path to folder where tests are located)

1. Create 'flask' virtualenv inside 'src' folder
2. Activate virtualenv and install requirements
3. Run app './run.py'
4. Open browser and go to (by default) 'http://127.0.0.1:5000/'

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
* Flask + gunicorn + nginx: To serve result files and images properly for users
  * Ability to view result and log files via WEB UI
* Add user roles?
  * Login page
* Settings page or panel to enable configuration via WEB UI
* Search/filter features
* pabot support
* Handle correctly situations when app has more than 1 user at the same time
* Update to Bootstrap 4 and jQuery 3 when Bootstrap 4 is ready
