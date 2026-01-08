#!/usr/bin/env ruby

arg = ARGV[0]
arg = arg.strip if arg
puts arg if arg =~ /^hb?t*n$/
