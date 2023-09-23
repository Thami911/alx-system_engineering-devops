# Execute a command
exec { 'kill_killmenow_process':
  command => 'pkill killmenow',
  path    => '/usr/bin',
  onlyif  => 'pgrep killmenow',
}
