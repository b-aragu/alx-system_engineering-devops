#!/usr/bin/env ruby

# parse logfile and output [sender],[receiver],[flags]

# Check if the command line argument is provided
if ARGV.empty?
  puts 'Usage: ./100-textme.rb <log_entry>'
  exit
end

# Extract relevant information from the log entry
result = ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")

# Output the result
puts result

