class apache_fix {
  # Ensure apache2 package is installed
  package { 'apache2':
    ensure => installed,
  }

  # Ensure apache2 service is running and enabled at boot
  service { 'apache2':
    ensure     => running,
    enable     => true,
    subscribe  => Exec['apache-configtest'],
  }

  # Ensure proper permissions for web content directory
  file { '/var/www/html':
    ensure  => directory,
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0755',
    recurse => true,
  }

  # Ensure apache configuration syntax is correct
  exec { 'apache-configtest':
    command     => '/usr/sbin/apachectl configtest',
    refreshonly => true,
    notify      => Service['apache2'],
  }

  # Restart Apache if any of the files change
  exec { 'restart-apache':
    command     => '/usr/sbin/systemctl restart apache2',
    refreshonly => true,
    subscribe   => [
      File['/var/www/html'],
    ],
  }
}

# Include the class
include apache_fix
