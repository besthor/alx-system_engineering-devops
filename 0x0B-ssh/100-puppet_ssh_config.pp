#setting up my client configuration file
include stdlib

file_line { "Turn off passwd autthentification":
ensure => present,
path => 'etc/ssh/ssh_config',
line => '		PasswordAuthentification no',
replace => true,
}

file_line { "Declare identity file':
ensure => present,
path => 'etc/ssh/ssh_config',
line =>'	IdentityFile ~/,ssh/school',
replace => true,
}
