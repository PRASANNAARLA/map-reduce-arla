# Case 2 - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 17) : 
    InvoiceID,Branch,City,Customertype,Gender,Productline,Unitprice,Quantity,Tax,Total,Date,Time,Payment,cogs,grossmarginpercentage,grossincome,Rating = datalist

    # print intermediate key-value pairs to standard output
    print(Date,"\t",1)
