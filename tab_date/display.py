import streamlit as st

from tab_date.logics import DateColumn

def display_tab_date_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_date_content (function): Function that will instantiate tab_date.logics.DateColumn class, save it into Streamlit session state and call its tab_date.logics.DateColumn.find_date_cols() method in order to find all datetime columns.
    Then it will display a Streamlit select box with the list of datetime columns found.
    Once the user select a datetime column from the select box, it will call the tab_date.logics.DateColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_date.logics.DateColumn.get_summary() as a Streamlit Table
    - the graph from tab_date.logics.DateColumn.histogram using Streamlit.altair_chart()
    - the results of tab_date.logics.DateColumn.frequent using Streamlit.write
 
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
    # Instantiate DateColumn class
    date_col = DateColumn(file_path=file_path, df=df)

    # Find datetime columns
    date_col.find_date_cols()

    # Display select box with datetime columns
    selected_col = st.selectbox("Select a datetime column:", date_col.cols_list)

    # Set the selected datetime column for analysis
    date_col.set_data(selected_col)

    # Expander container to display results
    with st.expander("Date Column Analysis"):
        # Display summary as a table
        summary_df = date_col.get_summary()
        st.write("Summary:")
        st.write(summary_df)

        # Display histogram using Altair
        st.write("Histogram:")
        st.altair_chart(date_col.barchart, use_container_width=True)
        
        # Display frequent values
        st.write("Frequent Values:")
        st.write(date_col.frequent)
