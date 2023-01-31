#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a regular expression matching method
puts ARGV[0].scan(/hb?tn/).join
