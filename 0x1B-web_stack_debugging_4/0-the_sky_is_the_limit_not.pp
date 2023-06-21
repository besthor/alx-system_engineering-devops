# This manifest adjusts the web stack configuration for Nginx to handle 1000 requests with 100 at a time

# Increase the worker connections in Nginx
file { '/etc/nginx/nginx.conf':
  ensure  => present,
  content => "# Adjusted Nginx configuration\n\nworker_connections 100;\nevents {\n  worker_connections 1000;\n}\n",
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  subscribe  => File['/etc/nginx/nginx.conf'],
}

