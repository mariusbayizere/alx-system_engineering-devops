#  use the exec Puppet resource

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
