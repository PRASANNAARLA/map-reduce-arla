# Case 2 - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 6) : 
    index,season_Num,episode,episode_name,name,line = datalist

    # print intermediate key-value pairs to standard output
    print(line,"\t",1)
