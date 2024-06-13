# Fix nginx to accept and serve more requests by increasing worker connections and worker processes

exec { 'increase-worker-connections':
  command => 'sed -i "s/worker_connections [0-9]\\+/worker_connections 4096/" /etc/nginx/nginx.conf',
  path    => '/usr/bin:/usr/sbin:/bin',
}

exec { 'increase-worker-processes':
  command => 'sed -i "s/worker_processes [0-9]\\+/worker_processes auto/" /etc/nginx/nginx.conf',
  path    => '/usr/bin:/usr/sbin:/bin',
}

exec { 'modify-max-open-files-limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}
