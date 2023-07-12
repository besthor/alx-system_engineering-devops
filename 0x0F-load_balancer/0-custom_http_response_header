#!/usr/bin/env bash
# Customizing a 404-error_page

# Updating Packages before performing installations
sudo apt-get update
sudo apt-get install -y nginx

# Creating an index.html page
echo "Hello World!" | sudo tee /var/www/html/index.html

# Performing a "moved permanently redirection" (301)
new_string="server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/besthor permanent;"
sudo sed -i "s/server_name _;/$new_string/" /etc/nginx/sites-enabled/default

# Creating a 404 Custom error page
echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html
new_string="listen 80 default_server;\n\terror_page 404 \/404.html;\n\tlocation = \/404.html {\n\t\troot \/var\/www\/html;\n\t\tinternal;\n\t}"

sudo sed -i "s/listen 80 default_server;/$new_string/" /etc/nginx/sites-enabled/default

# Creating an HTTP response header
sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default

# Testing configurations for syntax errors
sudo nginx -t

# Restart nginx after implementing changes
sudo service nginx restart
