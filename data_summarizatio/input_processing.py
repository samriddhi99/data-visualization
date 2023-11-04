import pandas as pd


def pd_dataframe(csv_file):
    df = pd.read_csv(csv_file)
    return df


def pd_dataframe(csv_file):
    df = pd.read_csv(csv_file)
    return df

def sort_and_filter(compared: list, df: pd.DataFrame) -> pd.DataFrame:
    """
    Sort and return a DataFrame based on a specified numeric column or columns.

    Parameters:
    -----------
    compared : list
        A list of column names to be compared or returned.

    df : pd.DataFrame
        The input DataFrame that will be sorted and filtered.

    Returns:
    --------
    pd.DataFrame
        If a numeric column specified in 'compared' is found in the DataFrame, the DataFrame will be sorted
        by that column, and a subset of the DataFrame containing only the specified 'compared' columns will be returned.
        If no valid numeric columns are found, the original DataFrame will be returned with the specified 'compared' columns.
    """
    for column in compared:
        if column in df.columns and pd.api.types.is_numeric_dtype(df[column]):
            sorted_df = df.sort_values(by=column)
            return sorted_df[compared]
    return df[compared]

def longest_element_length_in_columns(df):
    """
    Calculate the maximum length of elements in each column of a DataFrame.

    This function iterates through the columns of a given DataFrame and computes the maximum length
    of elements in each column, including both numeric and string data types. The maximum length is
    determined by applying the len(str(x)) function to each element in the column. For NaN (null) values,
    a length of 0 is assumed.

    Parameters:
    df (pandas.DataFrame): The DataFrame for which to calculate column element lengths.

    Returns:
    list: A list containing the maximum element length for each column in the DataFrame.
          The list is in the same order as the columns in the DataFrame.
    """
    column_lengths = []
    
    for column in df.columns:
        max_length = df[column].apply(lambda x: len(str(x)) if not pd.isnull(x) else 0).max()
        column_lengths.append(max_length)
    
    return column_lengths

def shorten_dataframe_by_uniform_distribution(df, len_of_longest_element_in_column: list) -> pd.DataFrame:
    """
    Calculate the maximum length of elements in each column of a DataFrame.

    This function iterates through the columns of a given DataFrame and computes the maximum length
    of elements in each column, including both numeric and string data types. The maximum length is
    determined by applying the len(str(x)) function to each element in the column. For NaN (null) values,
    a length of 0 is assumed.

    Parameters:
    df (pandas.DataFrame): The DataFrame for which to calculate column element lengths.

    Returns:
    list: A list containing the maximum element length for each column in the DataFrame.
          The list is in the same order as the columns in the DataFrame.

    Example:
    >>> import pandas as pd
    >>> data = {'Name': ['Alice', 'Bob', 'Carol', 'David'],
    ...         'Age': [25, 30, 22, 35],
    ...         'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
    >>> df = pd.DataFrame(data)
    >>> column_lengths = longest_element_length_in_columns(df)
    >>> print(column_lengths)
    [5, 2, 13]
    """
    
    x = 0
    for i in len_of_longest_element_in_column:
        x = x + i
    k = 3500 // x  
    
    total_rows = df.shape[0]
    z = total_rows//k
    
    selected_rows = df.iloc[::z].reset_index(drop=True) 
    return selected_rows

def final_dataframe(df, columns: list) -> pd.DataFrame:
    x = sort_and_filter(columns, df)
    y = longest_element_length_in_columns(x)
    z = shorten_dataframe_by_uniform_distribution(x, y)
    return z