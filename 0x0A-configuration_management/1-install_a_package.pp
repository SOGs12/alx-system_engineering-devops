# 1-install_a_package.pp

class { 'python':
  ensure => 'present',
}

class { 'python::pip':
  ensure => 'present',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Class['python::pip'],
}
