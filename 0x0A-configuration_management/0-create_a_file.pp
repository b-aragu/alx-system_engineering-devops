# Creating puppet file
file { '/tmp/school':
  ensure => file,
  mode => '0744',
  owner => 'www-dat'a,
  group => 'www-data',
  content => 'I love Puppet',
}
