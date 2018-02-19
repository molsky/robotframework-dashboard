#!/bin/bash

echo -e "=== Running setup script...\n"

APP_RESULTS_DIRECTORY="$PWD/src/rfwebui/results"
VENV_DIRECTORY=rfd-venv
NGINX_DIRECTORY=/etc/nginx

if [ -d "$VENV_DIRECTORY" ]; then
    rm -rf $VENV_DIRECTORY
fi

virtualenv -p python3 $VENV_DIRECTORY
source "$VENV_DIRECTORY/bin/activate"
pip install -r requirements.pip

echo -e "\n=== Setting nginx configuration files..."

if [ -d "$NGINX_DIRECTORY" ]; then
    cp setup_confs/rf_dashboard.orig setup_confs/rf_dashboard

    sed -i -e "s|__RF_RESULTS_FOLDER_PATH__|$APP_RESULTS_DIRECTORY|g" setup_confs/rf_dashboard

    sudo mkdir -p /etc/nginx/sites-available
    sudo mkdir -p /etc/nginx/sites-enabled

    sudo cp setup_confs/rf_dashboard /etc/nginx/sites-available/

    if [ -f "/etc/nginx/sites-enabled/rf_dashboard" ]; then
        sudo unlink /etc/nginx/sites-enabled/rf_dashboard
    fi
    sudo ln -s /etc/nginx/sites-available/rf_dashboard /etc/nginx/sites-enabled/rf_dashboard

    systemctl restart nginx.service
else
    echo "=== Skipping nginx configuration - nginx is not installed or requires manual configuration."
fi

echo -e "\n=== Done!"

echo "=== To run server:"
echo "=== source rfd-venv/bin/activate"
echo "=== In rfwebui -folder run following:"
echo "=== gunicorn --bind 0.0.0.0:8000 wsgi:app"
