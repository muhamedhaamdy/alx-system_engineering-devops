# palying with some configurations

$configuration = file('2-ssh_config')

#file {'etc/ssh/ssh_config':
#  ensure  => file,
#  content => $configuration,
#}
notify {'file message': 
  message => $configuration
}
