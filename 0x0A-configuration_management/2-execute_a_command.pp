# Puppet manifest to kill a process named killmenow
exec { 'pkill -9 killmenow':
  command => 'pkill -9 killmenow',
}
