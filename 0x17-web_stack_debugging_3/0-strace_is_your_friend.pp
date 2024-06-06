# This Puppet manifest installs the missing PHP module and restarts Apache

exec { 'install-php-module':
  command => '/usr/bin/apt-get install -y php-mysql',
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
  unless  => '/usr/bin/dpkg -l | grep -q "^ii  php-mysql"',
}

service { 'apache2':
  ensure     => 'running',
  enable     => true,
  require    => Exec['install-php-module'],
}

# Ensure Apache is restarted after the PHP module is installed
exec { 'restart-apache2':
  command     => '/usr/sbin/service apache2 restart',
  refreshonly => true,
  subscribe   => Exec['install-php-module'],
}
