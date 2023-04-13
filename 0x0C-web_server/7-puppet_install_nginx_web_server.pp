# Install Nginx
package { 'nginx':
  ensure => 'installed',
}

# Start Nginx service
service { 'nginx':
  ensure => 'running',
  enable => true,
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => 'server {
                listen 80;
                root /var/www/html;
                index index.html;

                location /redirect_me {
                    return 301 https://www.example.com/;
                }

                location / {
                    add_header X-Content-Type-Options nosniff;
                    add_header X-Frame-Options "SAMEORIGIN";
                    add_header X-XSS-Protection "1; mode=block";
                    add_header Content-Security-Policy "default-src 'self';";
                    try_files $uri $uri/ =404;
                }
            }',
}

# Create the Hello World! page
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}
