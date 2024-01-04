#!/usr/bin/env ruby
# Basic matching
string_to_match = ARGV[0]
form_pattern = /from:[^\]]+/
to_pattern = /to:[^\]]+/
falg_pattern = /flags:[^\]]+/
match_data_from = string_to_match.match(form_pattern)

for i in 5..match_data_from[0].length() do
  print match_data_from[0][i]
end
print ','

match_data_to = string_to_match.match(to_pattern)
for i in 3..match_data_to[0].length() do
  print match_data_to[0][i]
end
print ','

match_data_flag = string_to_match.match(falg_pattern)
for i in 6..match_data_flag[0].length() do
  print match_data_flag[0][i]
end
