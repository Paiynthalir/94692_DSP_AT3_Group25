import pandas as pd
import numpy as np

class Dataset:
    """
    --------------------
    Description
    --------------------
    -> Dataset (class): Class that manages a dataset loaded from CSV file

    --------------------
    Attributes
    --------------------
    -> file_path (str): Path to the uploaded CSV file (mandatory)
    -> df (pd.Dataframe): Pandas dataframe (default set to None)
    -> cols_list (list): List of columns names of dataset (default set to empty list)
    -> n_rows (int): Number of rows of dataset (default set to 0)
    -> n_cols (int): Number of columns of dataset (default set to 0)
    -> n_duplicates (int): Number of duplicated rows of dataset (default set to 0)
    -> n_missing (int): Number of missing values of dataset (default set to 0)
    -> n_num_cols (int): Number of columns that are numeric type (default set to 0)
    -> n_text_cols (int): Number of columns that are text type (default set to 0)
    -> table (pd.Series): Pandas DataFrame containing the list of columns, their data types and memory usage from dataframe (default set to None)
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.cols_list = []
        self.n_rows = 0
        self.n_cols = 0
        self.n_duplicates = 0
        self.n_missing = 0
        self.n_num_cols = 0
        self.n_text_cols = 0
        self.n_date_cols = 0
        self.n_bool_cols = 0
        self.table = None

    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.df to be displayed in the Dataframe tab of Streamlit app 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None
        """
        # Load the CSV file and set self.df if it hasn't been provided before
        self.set_df()
        
        # Check if self.df is None or empty
        if self.is_df_none():
            print("Empty Data")
        else:
            # Compute other information if self.df is not None
            self.set_columns()
            self.set_dimensions()
            self.set_duplicates()
            self.set_missing()
            self.set_numeric()
            self.set_text()
            self.set_bool()
            self.set_table()


        # Load the DataFrame and compute the necessary information
       
        
        
    def set_df(self):
        """
        --------------------
        Description
        --------------------
        -> set_df (method): Class method that will load the uploaded CSV file as Pandas DataFrame and store it as attribute (self.df) if it hasn't been provided before.

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if self.df is None:
            self.df = pd.read_csv(self.file_path)
            

    def is_df_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_df_none (method): Class method that checks if self.df is empty or none 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> (bool): Flag stating if self.df is empty or not

        """
        return self.df is None or self.df.empty

    def set_columns(self):
        """
        --------------------
        Description
        --------------------
        -> set_columns (method): Class method that extract the list of columns names and store the results in the relevant attribute (self.cols_list) if self.df is not empty nor None 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_df_none():
            self.cols_list = list(self.df.columns)

    def set_dimensions(self):
        """
        --------------------
        Description
        --------------------
        -> set_dimensions (method): Class method that computes the dimensions (number of columns and rows) of self.df  and store the results in the relevant attributes (self.n_rows, self.n_cols) if self.df is not empty nor None 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_df_none():
            self.n_rows, self.n_cols = self.df.shape

    def set_duplicates(self):
        """
        --------------------
        Description
        --------------------
        -> set_duplicates (method): Class method that computes the number of duplicated of self.df and store the results in the relevant attribute (self.n_duplicates) if self.df is not empty nor None 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_df_none():
            self.n_duplicates = self.df.duplicated().sum()

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing values of self.df and store the results in the relevant attribute (self.n_missing) if self.df is not empty nor None 

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        # To find the no of rows with missing value atleast in one column
        if not self.is_df_none():
            self.n_missing = self.df[self.df.isnull().any(axis=1)].shape[0]

    def set_numeric(self):
        """
        --------------------
        Description
        --------------------
        -> set_numeric (method): Class method that computes the number of columns that are numeric type and store the results in the relevant attribute (self.n_num_cols) if self.df is not empty nor None 
        
        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """
        if not self.is_df_none():
            numeric_cols = self.df.select_dtypes(include=np.number).columns
            self.n_num_cols = len(numeric_cols)

    def set_text(self):
        """
        --------------------
        Description
        --------------------
        -> set_text (method): Class method that computes the number of columns that are text type and store the results in the relevant attribute (self.n_text_cols) if self.df is not empty nor None 
        
        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """

        if not self.is_df_none():
            # Get columns with 'object' dtype (potential text columns)
            text_cols = self.df.select_dtypes(include='object').columns
            date_cols = set()  # Use set() to store date columns

        # Check if the potential text columns actually contain text
        text_cols = [col for col in text_cols if any(self.df[col].apply(lambda x: isinstance(x, str)))]

        # Check if the potential text columns also have a date-like format
        for col in text_cols:
            try:
                # Try converting the column to datetime
                self.df[col] = pd.to_datetime(self.df[col])
            except ValueError:
                # If conversion fails, it's not a date column
                pass
            else:
                # If conversion succeeds, remove from text_cols and add to date_cols
                text_cols.remove(col)
                date_cols.add(col)

        # Update the number of text columns
        self.n_text_cols = len(text_cols)
        self.n_date_cols = len(date_cols)


    def set_bool(self):
        """
        --------------------
        Description
        --------------------
        -> set_date (method): Class method that computes the number of columns that are boolean type and store the results in the relevant attribute (self.n_bool_cols) if self.df is not empty nor None 
        
        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """

        if not self.is_df_none():
            # Get columns with 'object' dtype (potential text columns)
            bool_cols = self.df.select_dtypes(include='bool').columns

        # Update the number of text columns
        self.n_bool_cols = len(bool_cols)

    def get_head(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_head (method): Class method that computes the first rows of self.df according to the provided number of rows specified as parameter (default: 5) if self.df is not empty nor None

        --------------------
        Parameters
        --------------------
        -> n (int): Number of rows to be returned

        --------------------
        Returns
        --------------------
        -> (Pandas.DataFrame): First rows of dataframe

        """
        if not self.is_df_none():
            return self.df.head(n)


    def get_tail(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_tail (method): Class method that computes the last rows of self.df according to the provided number of rows specified as parameter (default: 5) if self.df is not empty nor None

        --------------------
        Parameters
        --------------------
        -> n (int): Number of rows to be returned

        --------------------
        Returns
        --------------------
        -> (Pandas.DataFrame): Last rows of dataframe

        """
        if not self.is_df_none():
            return self.df.tail(n)

    def get_sample(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_sample (method): Class method that computes a random sample of rows of self.df according to the provided number of rows specified as parameter (default: 5) if self.df is not empty nor None

        --------------------
        Parameters
        --------------------
        -> n (int): Number of rows to be returned

        --------------------
        Returns
        --------------------
        -> (Pandas.DataFrame): Sampled dataframe

        """
        if not self.is_df_none():
            return self.df.sample(n)


    def set_table(self):
        """
        --------------------
        Description
        --------------------
        -> set_table (method): Class method that computes the Dataframe containing the list of columns with their data types and memory usage and store the results in the relevant attribute (self.table) if self.df is not empty nor None

        --------------------
        Parameters
        --------------------
        -> None

        --------------------
        Returns
        --------------------
        -> None

        """

        if not self.is_df_none():
            datatypes = self.df.dtypes

            # Memory usage including the index
            memory_with_index = self.df.memory_usage(deep=False, index=True)

            column_names = self.df.columns


            self.table = pd.DataFrame({
                'column': ['Index'] + column_names.tolist(),  # Include 'index' as the first row
                'data_type': [self.df.index.dtype] + datatypes.tolist(),  # Include index dtype
                'memory_usage': memory_with_index.tolist(),  # Include index memory usage
            })
            
    def get_summary(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.df to be displayed in the Dataframe tab of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Returns
        --------------------
        -> (pd.DataFrame): Formatted dataframe to be displayed on the Streamlit app

        """
        if not self.is_df_none():
            summary_data = {
                'Description': ['Number of Rows', 'Number of Columns', 'Number of Duplicated Rows', 'Number of Rows with Missing Values', 'Number of Numeric Columns', 'Number of Text Columns', 'Number of Columns with date format', 'Number of Columns with boolean format' ],
                'Value': [self.n_rows, self.n_cols, self.n_duplicates, self.n_missing, self.n_num_cols, self.n_text_cols, self.n_date_cols, self.n_bool_cols]
            }
            return pd.DataFrame(summary_data)