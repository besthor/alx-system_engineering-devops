##!/usr/bin/pup
# Using Puppt to install flask from pip3

package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem'
}
