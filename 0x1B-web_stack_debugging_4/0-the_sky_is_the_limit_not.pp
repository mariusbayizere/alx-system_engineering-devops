# Fixes nginx configuration to handle higher load by increasing worker connections and restarting the service
exec { 'fix--for-nginx':
  command => "bash -c \"sed -iE 's/worker_connections [0-9]\\+/worker_connections 1024/' /etc/nginx/nginx.conf && \
sed -iE 's/worker_processes [0-9]\\+/worker_processes auto/' /etc/nginx/nginx.conf && \
service nginx restart\"",
  path    => '/usr/bin:/usr/sbin:/bin',
}
