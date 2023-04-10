#Configures ubuntu server with nginx and add a custom HTTP header response
#Name = X-Served-By, value = hostname of server Nginx is running on

exec {'update':
  provider =>  shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install nginx'],
}

exec {'install nginx':
  provider =>  shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['custom_header'],
}

exec {'custom_header':
  provider =>  shell,
  command  => 'sudo sed -i "25i\\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default',
  before   => Exec['restart nginx'],
}

exec {'restart nginx':
  provider =>  shell,
  command  => 'sudo service nginx restart',
}
