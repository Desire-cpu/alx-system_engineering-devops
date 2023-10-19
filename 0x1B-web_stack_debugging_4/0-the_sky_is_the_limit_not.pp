# Increases the ULIMIT of the default file for the Nginx server.

# Increase the ULIMIT in the default Nginx configuration file.
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx', # Replace the ULIMIT value from 15 to 4096.
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx after changing the ULIMIT.
exec { 'nginx-restart':
  command => 'nginx restart', # Restart the Nginx server.
  path    => '/etc/init.d/'
}
