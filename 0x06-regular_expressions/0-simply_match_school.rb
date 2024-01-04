#!/usr/bin/env ruby
# Basic matching
string_to_match = ARGV[0]
pattern = /School/
match_data = string_to_match.scan(pattern)
puts "School" * match_data.length()
