import pandas as pd
import altair as alt

class TextColumn: 
    def __init__(self, file_path=None, df=None):
        self.file_path = file_path
        self.df = df
        self.cols_list = []
        self.serie = None
        self.n_unique = None
        self.n_missing = None
        self.n_empty  = None
        self.n_mode = None
        self.n_space = None
        self.n_lower = None
        self.n_upper = None
        self.n_alpha = None
        self.n_digit = None
        self.barchart = alt.Chart()
        self.frequent = pd.DataFrame()

# Method to find text columns by selecting those with data type 'object'.
    def find_text_cols(self):
        if self.df is not None:
            self.cols_list = self.df.select_dtypes(include=["object"]).columns.tolist()
            return self.cols_list

# Method to set various statistics and visualizations for a selected text column.
    def set_data(self, col_name):
        self.serie = self.df[col_name].astype(str)  # Convert all data to strings
        self.convert_serie_to_text()
        self.is_serie_none()
        self.set_unique()
        self.set_missing()
        self.set_empty()
        self.set_mode()
        self.set_whitespace()
        self.set_lowercase()
        self.set_uppercase()
        self.set_alphabet()
        self.set_digit()
        self.set_barchart()
        self.set_frequent()

# Convert series to string, ensuring all data is treated as text
    def convert_serie_to_text(self):
        self.serie = self.serie.astype(str)

# Check if the series is None or empty, which would indicate no data to analyze.
    def is_serie_none(self):
        return self.serie is None or self.serie.empty

# Set the number of unique values in the series.
    def set_unique(self):
        self.n_unique = self.serie.nunique()

# Set the number of missing values in the series.
    def set_missing(self):
        self.n_missing = self.df[self.serie.name].isnull().sum()

# Set the number of empty strings in the series.
    def set_empty(self):
        self.n_empty = (self.serie == '').sum()

# Set the mode (most frequent value) of the series.
    def set_mode(self):
        mode_vals = self.serie.mode()
        self.n_mode = mode_vals[0] if not mode_vals.empty else 'None'

# Set the number of values that are purely whitespace or empty strings.
    def set_whitespace(self):
        self.n_space = (self.serie.str.isspace() | (self.serie == '')).sum()

# Set the number of values that are in lowercase.
    def set_lowercase(self):
        self.n_lower = self.serie.str.islower().sum()

# Set the number of values that are in uppercase.
    def set_uppercase(self):
        self.n_upper = self.serie.str.isupper().sum()

# Set the number of values that contain only alphabetic characters.
    def set_alphabet(self):
        self.n_alpha = self.serie.str.isalpha().sum()

# Set the number of values that contain only digits.
    def set_digit(self):
        self.n_digit = self.serie.str.isdigit().sum()

# Generate a bar chart visualization of the value counts of the series.
    def set_barchart(self, width=600, height=400):
        value_counts = self.serie.value_counts().reset_index().rename(columns={'index': 'value', self.serie.name: 'occurrence'})
        self.barchart = alt.Chart(value_counts.head(20)).mark_bar().encode(
            x='value:N',
            y='occurrence:Q'
        )
# Determine the most frequent values and their percentages in the series.      
    def set_frequent(self, end=20):
        # Calculate frequency and percentage of the most common values.
        self.frequent = self.serie.value_counts().head(end).reset_index()
        self.frequent.columns = ['value', 'occurrence']
        self.frequent['percentage'] = (self.frequent['occurrence'] / len(self.serie)) * 100

# Compile a summary of the text analysis into a DataFrame.
    def get_summary(self):
        # Create a summary dictionary with descriptions and values.
        summary_data = {
            'Description': [
                'Number of Unique Values',
                'Number of Rows With Missing Values',
                'Number of Empty Rows',
                'Number of Rows with Only Whitespace',
                'Number of Rows with Only Lowercases',
                'Number of Rows with Only Uppercases',
                'Number of of Rows with only Alphabet',
                'Number of Rows with Only Digits',
                'Mode value'
            ],
            'Value': [
                self.n_unique,
                self.n_missing,
                self.n_empty,
                self.n_space,
                self.n_lower,
                self.n_upper,
                self.n_alpha,
                self.n_digit,
                self.n_mode,
            ]
        }
        return pd.DataFrame(summary_data) # Return summary as a DataFrame.

