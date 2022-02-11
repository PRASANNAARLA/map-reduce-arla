# map-reduce-arla
## Prasanna Arla -SupermarketSales
## Dataset:
Link: [Raw Dataset reference](https://www.kaggle.com/aungpyaeap/supermarket-sales)

## About data:
The dataset which I have used is the super market sales which contains of 1000 values.

Initially I have took the dataset and mapped to the key value pairs- date and the count then I have sorted the dataset incase if they are not sorted and then I have reduced the dataset and obtained the output after reducing and sorting. The graph is used to show the count of sales according to the date.

## Command to get the output: 

```
cat supermarket_sales.csv | python mapper.py | sort | python reducer.py > prasannaoutput.txt

```

## Summary: 

**I wanted to know on which day of the year 2019 the highest number of super market sales were sold? </br>
From the graph I got to know that on february 2nd 2019 the highest sales occured.

![super market sales](/image/Newgraph.PNG)



