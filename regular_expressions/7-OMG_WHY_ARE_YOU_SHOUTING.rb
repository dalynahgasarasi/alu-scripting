#!/usr/bin/env ruby

arg = ARGV[0]
arg = arg.strip if arg

puts arg.scan(/[A-Z]/).join
