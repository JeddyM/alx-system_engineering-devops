# Increasing the number of requests nginx webserver can handle
exec { 'increase_nginx_connections':
  command     => 'sed -i "s/worker_connections [0-9]\+/worker_connections 2048/" /etc/nginx/nginx.conf',
  path        => '/bin:/usr/bin',
  refreshonly => true,
  notify      => Service['nginx'],
}
