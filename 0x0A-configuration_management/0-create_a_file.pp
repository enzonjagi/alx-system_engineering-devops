file { '/tmp/school':
  ensure  => 'present',
  replace => 'no',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love puppet'
  }
