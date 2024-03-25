# SSH client configuration must be configured to use the private key ~/.ssh/school
# SSH client configuration must be configured to refuse to authenticate using a password

include stdlib

file_line { 'SSH Private Key':
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => '^[#]+[\s]*(?i)IdentityFile[\s]+~/.ssh/id_rsa$',
  replace            => true,
  append_on_no_match => true
}

# match explanation
# ^    stand for starting of the line
# [#]*  one hash character
# [\s]*  zero or more white space characters
# (?i)IdentityFile case insensitive "IdentityFile"
# [\s]+ at least one whitespace character
# ~/.ssh/id_rsa this ssh private key file path we may replace
# $      last 

file_line { 'Deny Password Auth':
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => '^[#]+[\s]*(?i)PasswordAuthentication[\s]+(yes|no)$',
  replace            => true,
  append_on_no_match => true
}
