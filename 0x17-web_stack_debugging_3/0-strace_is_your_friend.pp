# Find out why Apache is returning a 500 error, fix and automate using Puppet
# command: curl -sI 127.0.0.1

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
