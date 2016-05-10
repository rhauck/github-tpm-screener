#!/usr/bin/env python

import subprocess
from collections import Counter
  
#
# Author: Rebecca Hauck
#
# Short demo script for Part 2 of the Technical Program Manager screener 
#
# I solved the problem (mostly) with Python here to fulfill the request to 
# submit a script. However, this simpler shell command that will do 
# the same thing:
#
# > git log --all --format='%ae' | sort | uniq -c | sort -r
#
# I sorted just for bonus points. :)
#
 
def main():
  
  PIPE = subprocess.PIPE
  
  # Ask git for the emails associated with all commits on this repo
  process = subprocess.Popen(['git', 'log', '--all', '--format=\'%ae\''], stdout=PIPE)
  output = process.communicate()
  
  # Convert them into list
  emails = output[0].split()
  
  # Get counts of each email in list
  count = Counter(emails)
  
  # Sort the list in descending order
  sorted_list = count.items()
  sorted_list.sort(key=lambda tup: tup[1], reverse=True) 
  
  one_line_result = ''
  
  # Print results each on a new line for readability
  for email in sorted_list:
    print str(email[1]) +' '+ (str(email[0])).replace('\'', '')  
    one_line_result += str(email[1]) +' '+ str(email[0]) +' '
    
  # The sample output suggested no newlines, so this will do it 
  # print one_line_result.replace('\'', '')  
     
 
if __name__ == '__main__':
  main()