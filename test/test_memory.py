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
        self.table = None
        self.table1 = None

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


    # def set_table(self):
    #     """
    #     --------------------
    #     Description
    #     --------------------
    #     -> set_table (method): Class method that computes the Dataframe containing the list of columns with their data types and memory usage and store the results in the relevant attribute (self.table) if self.df is not empty nor None

    #     --------------------
    #     Parameters
    #     --------------------
    #     -> None

    #     --------------------
    #     Returns
    #     --------------------
    #     -> None

    #     """

    #     if not self.is_df_none():
    #         datatypes = self.df.dtypes

    #         # Memory usage including the index
    #         memory_with_index = self.df.memory_usage(deep=True, index=True)

    #         # Extract memory usage for the index
    #         index_memory = memory_with_index.iloc[1:]

    #         column_names = self.df.columns

    #         # Ensure that the lengths of 'column_names', 'datatypes', and 'memory' are the same
    #         length_check = len(column_names) == len(datatypes) == len(memory_with_index)

    #         if length_check:
    #             # Add memory usage for the index to the DataFrame
    #             self.table = pd.DataFrame({
    #                 'column': ['Index'] + column_names.tolist(),  # Include 'index' as the first row
    #                 'data_type': ['Nan'] + datatypes.tolist(),  # Include index dtype
    #                 'memory_usage': [index_memory] + memory_with_index.tolist(),  # Include index memory usage
    #             })
    #         else:
    #             # Handle the case where lengths are not the same
    #             raise ValueError("Lengths of 'column_names', 'datatypes', and 'memory' must be the same.")
            
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
            # Memory usage including the index
            memory_with_index = self.df.memory_usage(deep=False, index=True)

            # Extract memory usage for the index
            index_memory = memory_with_index.iloc[1:]
            memory_without_index = memory_with_index.iloc[1:]

            
            column_names = self.df.columns

            self.table = pd.DataFrame({
                'column': column_names.tolist() + ['Index'] ,  # Include 'index' as the first row
                'data_type': [str(dtype) for dtype in self.df.dtypes] + [str(self.df.index.dtype)] ,  # Include index dtype
                'memory_usage': memory_with_index.tolist(),
            })





            
