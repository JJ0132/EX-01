# Issues

After the EDA analysis by ydata-profiling we got the nexts issues.

## Columns

**Item**
- Is highly overall correlated with Price Per Unit column.
- Has 333 (3.3%) missing values.

**Quantity**
- Is highly overall correlated with Total Spent column.
- Has 138 (1.4%) missing values.

**Price Per Unit**
- Is highly overall correlated with Item and Total Spent columns.
- Has 179 (1.8%) missing values.

**Total Spent**
- Is highly overall correlated with Price Per Unit and Quantity columns.
- Has 173 (1.7%) missing values.

**Payment Method**
- Has 2579 (25.8%) missing values.

**Location**
- Has 3265 (32.6%) missing values.

**Transaction Date**
- Has 159 (1.6%) missing values.

**Transaction ID**
- Has unique values.

# Solutions

**Item** and **Price Per Unit** are highly correlated so we can deduce, items by their price and vice versa. The missing values can be deducted by this correlation.

**Quantity**, **Total Spent** and **Price Per Unit** are highly correlate, thats because the total spent can be calculated by the following formula, `Total Spent = Quantity * Price Per Unit`. Using this formula we can deduct most of the missing values.

**Payment Method** and **Location** has high missing values, 26% and 33% respectively, for that we are changing this missing value to `Unregistered`. In that way we do not mess up or remove huge amount of information from the dataset.

In **Transaction Date** there are some missing values, as it is date information we can deduct them by the above or below rows assuming that the date is aproximated to one of them because is a chronological measure.

# Steps

First of all we need to convert invalid values such as `ERROR` or `UNKNOWN` into valid non-numerical values `NaN`.