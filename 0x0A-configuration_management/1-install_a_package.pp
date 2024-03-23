#!/usr/bin/pup
# Using Puppet install flask from pip
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
