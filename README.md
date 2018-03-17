# data_shape
Python utility to shape/convert datasets, with saved configs for reuse

## Usage
python shapes.py --input test_data/test.json --config config.json --output datasets/testout.csv

## Config

**Columns**

Declare your wanted columns here. If you include a column in the config that is not in the input dataset, it will just be ignored.

You can choose to simply include the column by just passing the column name as the key, and an empty string as the value.

To rename a column, set the column value to a dictionary, and add the key "col_name" with the new column name.

To transform a column, include a lambda function in the "transform" key.

```
{
"columns":{
    "name" : {
        "transform" : "lambda x: str(x)[::-1]"
    },
    "age" : "",
    "_id" : {
        "col_name" : "id",
        "transform" : "lambda x: x + 'test'"
    },
    "not_on_this_table" : ""
}
}
```

## Todo

* Add more config options
* Considering adding a data generation feature for randomized data, either by using ML or just a configuration file
