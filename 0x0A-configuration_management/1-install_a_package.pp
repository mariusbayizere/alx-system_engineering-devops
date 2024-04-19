# Define the package for Python 3 pip
package { 'python3-pip':
  ensure => installed,
}
# Install Flask version 2.1.0 using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/pip3 show flask | grep -q "^Version: 2.1.0$"',
}
# Notify user that Flask installation is complete
notify { 'Flask installed successfully':
  require => Exec['install_flask'],
}


