# 34 - Data Input and Output

## Data Sources

4 main data sources in this tutorial:

* CSV
* Excel
* HTML
* SQL

In order to work with HTML files and SQL Datbases, the following libraries need to be installed.

* pip install sqlalchemy
* pip install lxml
* pip install html5lib
* pip install BeautifulSoup4

## Reading CSV Files

To read files, the common function is `pd.read_` followed by the file format that the data is in.

```py
# Reading the CSV File
df = pd.read_csv('example.csv')
```

## Exporting DataFrames

To export files, the common funcion is 'df.to_' followed by the file format that the data is written into.

**NOTE:** By setting `index=False`, this won't save the index to the CSV file. If `index=False` is not set, when importing the CSV file again, the index will be saved to the CSV file and will appear as an unnamed column when reimporting the CSV file.

```py
# Exporting to CSV (With Index)
df.to_csv('My_output')

# Exporting to CSV (Without Index)
df.to_csv('My_output',index=False)
```

## Reading Excel Files

Reading Excel files requires two parameters:

* `filename` The name of the Excel File
* `sheet_name` The name of the sheet to be read

```py
# Reading an Excel File
df.read_excel('Excel_Sample.xlsx',sheetname='Sheet1')
```

## Exporting Excel Files

Exporting Excel files requires two parameters, similar to reading it:

* `filename` The name of the Excel File
* `sheet_name` The name of the sheet to be created

```py
# Reading an Excel File
df.to_excel('Excel_Sample.xlsx',sheetname='NewSheet')
```

## Reading HTML 

What pandas does is try to read every table within the HTML file. This results in the type that is returned from the `.read_html()` method to be a list. It'll be a list of tables. To get around this, cycle through the list until the target table is acquired. 

*For this case, it should be `df[0]`*

```py
# Reading a HTML Link
df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
```

## Reading SQL

The pandas.io.sql module provides a collection of query wrappers to both facilitate data retrieval and to reduce dependency on DB-specific API. Database abstraction is provided by SQLAlchemy if installed. In addition you will need a driver library for your database. Examples of such drivers are psycopg2 for PostgreSQL or pymysql for MySQL. For SQLite this is included in Python’s standard library by default. You can find an overview of supported drivers for each SQL dialect in the SQLAlchemy docs.


If SQLAlchemy is not installed, a fallback is only provided for sqlite (and for mysql for backwards compatibility, but this is deprecated and will be removed in a future version). This mode requires a Python database adapter which respect the Python DB-API.

See also some cookbook examples for some advanced strategies.

The key functions are:

* `read_sql_table(table_name, con[, schema, ...])`
    * Read SQL database table into a DataFrame.
* `read_sql_query(sql, con[, index_col, ...])`	
    * Read SQL query into a DataFrame.
* `read_sql(sql, con[, index_col, ...])`	
    * Read SQL query or database table into a DataFrame.
* `DataFrame.to_sql(name, con[, flavor, ...])`	
    * Write records stored in a DataFrame to a SQL database.

**NOTE:** Pandas isn't the best way to read a SQL database. Because there are many SQL engines. The specific driver for the specific SQL engine should be used to read data from SQL.

* PostgreSQL `pip install psycopg2`
* MySQL `pip install pymysql`

Additional information for the specific SQL driver can be found in the sqlalchemy documentation.

```py
# Simple SQL Engine
from sqlalchemy import create_engine

# Creating a temporary SQL engine
engine = create_engine('sqlite:///:memory:')

# Writing to SQL
df.to_sql('my_table',engine)

# Reading from SQL
sqldf = pd.read_sql('my_table',con=engine)
```


