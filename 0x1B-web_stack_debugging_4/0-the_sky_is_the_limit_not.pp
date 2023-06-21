# This manifest increases the amount of traffic an Nginx server can handle

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  refreshonly => true,
  notify => Exec['nginx-restart'],
}

# Restart Nginx
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
  subscribe => Exec['fix--for-nginx'],
}

