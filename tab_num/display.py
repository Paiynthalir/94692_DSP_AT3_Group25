import streamlit as st

from tab_num.logics import NumericColumn

def display_tab_num_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_num_content (function): Function that will instantiate tab_num.logics.NumericColumn class, save it into Streamlit session state and call its tab_num.logics.NumericColumn.find_num_cols() method in order to find all numeric columns.
    Then it will display a Streamlit select box with the list of numeric columns found.
    Once the user select a numeric column from the select box, it will call the tab_num.logics.NumericColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_num.logics.NumericColumn.get_summary() as a Streamlit Table
    - the graph from tab_num.logics.NumericColumn.histogram using Streamlit.altair_chart()
    - the results of tab_num.logics.NumericColumn.frequent using Streamlit.write
 
    --------------------
    Parameters
    --------------------
    -> file_path (str): File path to uploaded CSV file (optional)
    -> df (pd.DataFrame): Loaded dataframe (optional)

    --------------------
    Returns
    --------------------
    -> None

    """

    numeric_column = NumericColumn(file_path, df)

    numeric_column.find_num_cols()

    selected_col = st.selectbox("Select a numeric column:", numeric_column.cols_list)

    if selected_col:
        numeric_column.set_data(selected_col)

        with st.expander("Numeric Column Summary"):
            st.write("Summary:")
            summary_df = numeric_column.get_summary()
            st.write(summary_df)
            st.write("Histogram:")
            st.altair_chart(numeric_column.histogram, use_container_width=True)
            st.write("Frequent Values:")
            st.write(numeric_column.frequent)
    
