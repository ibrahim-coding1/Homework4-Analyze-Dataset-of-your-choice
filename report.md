# Data Analysis Report

For this assignment, I used a small dataset that I created for practicing basic pandas operations. The dataset represents different food items along with a category label, a numeric value, and a numeric score. Even though it is a simple dataset, it was helpful for learning how to work with CSV files, inspect data, filter rows, and perform groupby operations in pandas.

In my analysis, I loaded the dataset into a DataFrame and began by printing out the first few rows, the structure of the data, and summary statistics. I practiced using both `loc` and `iloc` to grab specific rows, slices, and single cells. I also filtered the dataset with a simple condition and with two conditions combined using the `&` operator.

After that, I added a new column called `DoubleValue`, which was just the `Value` column multiplied by two, and then I removed it using the `.drop()` method. Finally, I used `groupby()` on the `Category` column to calculate the mean `Score` for each category.

One thing I noticed is that the dataset is very clean. There were no missing values or strange entries, which made the operations straightforward. In a real dataset, I would expect more complications, like inconsistent formatting or null values. This assignment helped me understand how pandas works and made me feel more confident manipulating and analyzing data with Python.
