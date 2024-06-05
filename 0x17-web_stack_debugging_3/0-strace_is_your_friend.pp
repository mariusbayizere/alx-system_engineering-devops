# 0-strace_is_your_friend.pp
# This Puppet manifest installs PHP and the missing php-mysql module to fix the 500 Internal Server Error in Apache

exec { 'install_php':
  command => '/usr/bin/apt-get update && /usr/bin/apt-get install -y php',
  path    => ['/usr/bin', '/usr/sbin'],
  unless  => 'which php',
}

exec { 'install_php_mysql':
  command => '/usr/bin/apt-get install -y php-mysql',
  path    => ['/usr/bin', '/usr/sbin'],
  unless  => '/usr/bin/php -m | grep mysql',
  require => Exec['install_php'],
}

service { 'apache2':
  ensure  => 'running',
  enable  => true,
  require => Exec['install_php_mysql'],
}
