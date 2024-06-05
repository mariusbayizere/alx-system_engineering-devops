# This Puppet manifest ensures that the Apache user has the correct permissions on the /var/www/html directory

exec { 'fix-permissions':
  command => '/bin/chown -R www-data:www-data /var/www/html',
  onlyif  => '/usr/bin/find /var/www/html ! -user www-data',
}

file { '/var/www/html':
  ensure => directory,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
  recurse => true,
}
