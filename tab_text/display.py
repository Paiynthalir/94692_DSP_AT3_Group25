import altair as alt
import streamlit as st
from tab_text.logics import TextColumn
import altair as alt


def display_tab_text_content(file_path=None, df=None):
    if df is not None:
        # Instantiate the TextColumn class with the dataframe
        text_col_analyser = TextColumn(df=df)
        
        # Call find_text_cols to get all text columns and store them in session state
        text_columns = text_col_analyser.find_text_cols()
        if not text_columns:
            st.write("No text columns found in the dataset.")
            return

        # Display a select box with the list of text columns
        selected_col = st.selectbox("Which column do you want to explaore?", text_columns)

        # Once a user selects a column, compute all information for that column
        text_col_analyser.set_data(selected_col)
        chart = text_col_analyser.barchart
        # Display the results in an expander
        with st.expander("Text Column"):
            # Display the summary as a Streamlit Table
            st.table(text_col_analyser.get_summary())

            st.subheader('Bar Chart')
            # Display the bar chart using Streamlit's altair_chart function
            chart = chart.encode(
              x=alt.X('value:N', title=selected_col),
              y=alt.Y('occurrence:Q', title='Count of Records')
            ).properties() 
            st.altair_chart(chart, use_container_width=True)
            st.subheader('Most Frequent Values')
            # Display the most frequent values using Streamlit's write function
            st.write(text_col_analyser.frequent)
    else:
        st.error("No DataFrame provided.")