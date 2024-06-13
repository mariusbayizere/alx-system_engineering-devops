# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message

exec { 'increase-hard-file-limit-holberton-user':
  command => 'sed -i "/holberton hard nofile/s/[0-9]\\+/50000/" /etc/security/limits.conf',
  path    => '/usr/bin:/usr/sbin:/bin',
}

exec { 'increase-soft-file-limit-holberton-user':
  command => 'sed -i "/holberton soft nofile/s/[0-9]\\+/50000/" /etc/security/limits.conf',
  path    => '/usr/bin:/usr/sbin:/bin',
}
