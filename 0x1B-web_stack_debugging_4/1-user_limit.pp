# Ensure that the user 'holberton' can log in and open files without encountering errors.

# Increase the hard file limit for the 'holberton' user in /etc/security/limits.conf.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf', # Replace the hard file limit value for 'holberton' with 50000.
  path    => '/usr/local/bin/:/bin/'
}

# Increase the soft file limit for the 'holberton' user in /etc/security/limits.conf.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf', # Replace the soft file limit value for 'holberton' with 50000.
  path    => '/usr/local/bin/:/bin/'
}
