#!/usr/bin/env ruby
# Expression that are display ten phone number
puts ARGV[0].scan(/^[0-9]{10}$/).join
