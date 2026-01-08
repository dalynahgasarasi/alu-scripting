#!/usr/bin/env ruby

line = ARGV[0]
line = line.strip if line

if line =~ /from:([^\]]+).*to:([^\]]+).*flags:([^\]]+)/
  puts "#{$1},#{$2},#{$3}"
end

