#!/usr/bin/env ruby
# Basic matching
string_to_match = ARGV[0]
pattern = /h.n/
match_data = string_to_match.scan(pattern).join
puts "#{match_data}"
