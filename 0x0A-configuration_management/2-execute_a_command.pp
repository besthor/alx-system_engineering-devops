# Using Puppe to create a manifest that kills a process named killmenow.

exec { 'pkill':
  command => 'pkill -9 -f killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
