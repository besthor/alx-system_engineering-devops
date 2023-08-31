#!/usr/bin/env bash
# Create a script to install and configure HAProxy on lb-01 server
# Configure HAProxy to send traffic to web-01 and web-02 servers
# Distribute requests using a roundrobin algorithm
# Make sure that HAProxy can be managed via an init script

# Install and configure HAproxy on my lb-01 server.
sudo apt-get -y update
apt-get -y install haproxy

# edit config file
server_config=\
"
frontend  besthor_frontend
        bind *:80
        mode http
        default_backend besthor_backend
backend besthor_backend
        balance roundrobin
        server 176572-web-01 54.165.168.252:80 check
        server 176572-web-02 34.237.91.136:80 check
"
echo "$server_config" | sudo tee -a /etc/haproxy/haproxy.cfg

# enable haproxy to be started by init script
echo "ENABLED=1" | sudo tee -a /etc/default/haproxy

# Testing the HAproxy configuration file
sudo haproxy -c -f /etc/haproxy/haproxy.cfg

# Restart the Nginx service
sudo service haproxy restart
