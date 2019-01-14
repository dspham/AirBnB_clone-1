#!/usr/bin/env bash
# Prepare web servers for deployment of web_static

# Install nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# Create web folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file
sudo touch /data/web_static/releases/test/index.html
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" | sudo tee /data/web_static/releases/test/index.htm\
l

# Recreate a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content
# of /data/web_static/current/ to hbnb_static
sudo sed -i "38i \\\tlocation /hbnb_static {\n\talias /data/web_static/current;\n}" /etc/nginx/sites-available/default
sudo service nginx restart
