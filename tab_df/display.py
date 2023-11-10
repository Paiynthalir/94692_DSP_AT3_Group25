import streamlit as st

from tab_df.logics import Dataset

def display_tab_df_content(file_path):
    """
    --------------------
    Description
    --------------------
    -> display_overall_df (function): Function that will instantiate tab_df.logics.Dataset class, save it into Streamlit session state and call its tab_df.logics.Dataset.set_data() method in order to compute all information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    1. the results of tab_df.logics.Dataset.get_summary() as a Streamlit Table
    2. the results of tab_df.logics.Dataset.table using Streamlit.write()
    Finally it will display a second Streamlit Expander container with a slider to select the number of rows to be displayed and a radio button to select the method (head, tail, sample).
    According to the values selected on the slider and radio button, display the subset of the dataframe accordingly using Streamlit.dataframe
    
    --------------------
    Parameters
    --------------------
    -> file_path (str): File path to uploaded CSV file

    --------------------
    Returns
    --------------------
    -> None
    
    """
    # Instantiate the Dataset class
    dataset = Dataset(file_path)
    # Compute all the necessary information
    dataset.set_data()

    # Save the Dataset object into Streamlit session state
    st.session_state.dataset = dataset

    summary_df = dataset.get_summary()

    # Display dataset summary as a Streamlit Table
    st.write("Dataframe")
    st.table(summary_df)

    # Extract relevant information from dataset for display
    columns_info = dataset.table

    # Display dataset table
    st.write("Columns")
    st.table(columns_info)

    # Second Expander container for displaying a subset of the dataset
    with st.expander("Explore Dataframe"):
        # Slider for selecting the number of rows to display
        num_rows_max = len(dataset.df)  # Get the number of rows from the dataset
        num_rows = st.slider("Select the number of rows to be displayed", min_value=5, max_value=num_rows_max,)

        # Radio button for selecting the method (head, tail, sample)
        display_method = st.radio("Exploration Method", ("Head", "Tail", "Sample"))

        if display_method == "Head":
            st.write("Top rows of Selected Table")
            st.write(dataset.get_head(num_rows))
        elif display_method == "Tail":
            st.write("Bottom rows of Selected Table")
            st.write(dataset.get_tail(num_rows))
        elif display_method == "Sample":
            st.write("Random Sample of Selected Table")
            st.write(dataset.get_sample(num_rows))

