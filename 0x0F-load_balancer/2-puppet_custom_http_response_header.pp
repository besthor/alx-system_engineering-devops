# Useing Puppet to automate a custom HTTP header response
exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'installed',
  require => Exec['update'],
}

file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => 'add_header X-Served-By $hostname;',
  match => '^http {',
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  hasstatus => true,
  require   => [Package['nginx'], File_line['http_header']],
}
