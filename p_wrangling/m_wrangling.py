#Imports
import pandas as pd
import numpy as np

#Define a function for droping errors
def drop_error(my_df, column_name, value):
    my_df = my_df[my_df[column_name] != value]
    return my_df

#Define a function for spliting elements and keeping only the element that I want
def wrangling_split(df, columns, separator, element):
    for col in columns:
        df[col] = df[col].str.split(separator, expand = True)[element]
    return df

#Define a function for replacing one vale for other
def wrangling_replace(df_replace, columns_replace, str_to_delete, str_to_insert):
    for col_replace in columns_replace:
        df_replace[col_replace] = df_replace[col_replace].str.replace(str_to_delete, str_to_insert)
    return df_replace

# Define a function for casting the columns
def wrangling_to_type(df_to_type, columns_to_type, type_to_type):
    for col_to_type in columns_to_type:
        df_to_type[columns_to_type] = df_to_type[columns_to_type].astype(type_to_type)
    return df_to_type


