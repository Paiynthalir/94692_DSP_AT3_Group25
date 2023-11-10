import streamlit as st
from tab_date.logics import DateColumn

def display_tab_date_content(file_path=None, df=None):
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


