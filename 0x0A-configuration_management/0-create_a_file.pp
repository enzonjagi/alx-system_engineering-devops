# puppet manifest to create a file in /tmp
file { '/tmp/school':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love puppet',
  path    => '/tmp/school',
  }
