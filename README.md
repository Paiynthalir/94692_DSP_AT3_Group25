# 94692_DSP_AT3_Group25
# Building Data Explorer Web App in Python

## Author
    Name: Paiynthalir Samyappan Nallamuthu
    Student ID: 24715435

## Description
    This web application developed using streamlit facilitates exploration of a given dataset in CSV format. This application will explore and analyse the content of an input dataset, to help the data scientists/ analyst perform the basic EDA(Exploratory Data Analysis) like no of rows, columns, name of the columns, the data types and memory usage of each column, the sample data of the data set with interactive slider and option to select 'Head', 'Tail' or 'Random sample'. In addition to the overall dataset information, this application also helps, selection of a numeric column and display data analysis results/charts, selection of a text column and display data analysis results/charts and selection of a datetime column and display data analysis results/charts in corresponding tabs. 

## Challenges faced and how to resolve
    1. The streamlit run command was throwing error when I tried to execute the 'testapp.py'(displaying the title alone). Then found that I missed to select "Add python.exe to PATH" option during python installation. Fixed by uninstall and reinstall python using this option. 
    2. Tried to test  with a json file and found wierd outputs. Fixed in by adding code to check the extention is '.csv' and showed error message if the file type is anything other than csv file. 
    3. When adding the memory usage column, the length mismatch error was popping up all the time. Later found that memory usage with index = 'True' will also return the memory usage of the index column. Fixed it by including index as a new row in the table along with the other list of columns.
    4. Sometimes, the changes made in the streamlit app codes was not reflecting while run. It was because I was running multiple instances of streamlit applications. Later killed all the instances using the right click -> Kill Terminal option in the right pane of the terminal and opened new terminal and executed the streamlit run command. 
    5. Date format fields were also shown as text fields in the data exploration, which I felt is not very useful. So tried to convert the value to datatime, and if the conversion was successful, counted that as a date field. 
    6. Found it difficult to find the versions of the packages used in python. Finally used __version__ option in the print statement in a new python file (version.py inside test folder)

## Futrue additional features 
    This application can be extended to have these features,
    1. Extend the application usage to other file formats like excel, parquet, json to make it more useful to explore wide range of data files
    2. Include visualisations for missing data in first tab
    3. Include corelation matrix after converting all the columns in to numeric. This can help with analysing the linear relationship between the features of the data set. 
    4. Include copy button for each table and chart, to enable easy transfer of summarised data and charts into other documents.

## Project Setup
### How to get the development environment set and running? 
    1. Install VS code from https://code.visualstudio.com/download.
    2. Install Python from https://www.python.org/downloads/.
    3. During installation select "Add python.exe to PATH" (Note: Important step not to miss).
    4. Open the VS code ---> "Manage" --> Click on "Command Palette" --> Select the Python Interpreter(the latest version installed in step 2).
    5. Now to install streamlit package, open the VS code terminal and type "pip install streamlit".
    6. To verify whether the streamlit package was installed correctly and works, on the VS code terminal, type "streamlit hello" it will take us to a demo page of streamlit - http://localhost:8501.
    7. To install the requests package, open the VS code terminal and type "pip install requests".
    8. Unzip the file and copy the folder structure downloaded from from https://drive.google.com/file/d/1IlWK-7Wp0xX-GGZbyOFyuPk8PcK9XBHc/view?usp=drive_link into the local storage.
    9. Open this folder in VS Code.
    10. The prepopulated python files will be loaded into VS code now.
    11. Login to git hub - https://github.com/Paiynthalir/94692_DSP_AT3_Group25/tree/main
    12. Push, Pull and Sync the code into the git hub and the project setup is all set. 

Some basic Git commands are:
```
git status
git add .
git commit -m "summary of changes"
git push -u origin main
```

## Python version
    Python 3.11.5 64-bit Windows

## Packages used
    Package Used                        Version
    ------------------                  ---------
    requests                            2.31.0
    charset-normalizer(from requests)   2.1.1
    idna(from requests)                 3.4
    urllib3(from requests)              2.0.5
    certifi(from requests)              2022.6.15
    pip                                 23.2.1
    streamlit                           1.27.1

## How to Run the Program
    1. Right click on the app.py from the left pane of VS Code -> and click on 'Open the integrated terminal'.
    2. In the terminal ->  type streamlit run app.py and hit ENTER.

    You can now view your Streamlit app in your browser.

    Local URL: http://localhost:8502
    Network URL: http://192.168.1.110:8502

    3. Now the CSV data exploration APP is available are the web application in the browser to use.
    4. In addition to the above steps, the app can also be accessed through https://dataexplorer-paiynthalir.streamlit.app/
        since this app is also deployed using streamlit cloud. 

## How the app works 
    This interactive web application, developed using Streamlit and Python, facilitates exploratory data analysis (EDA) on CSV files provided by users. 
    The application is structured into distinct sections:

### CSV File Upload Menu 
    - Users can upload a CSV file through a menu.
    - Upon file selection, the application proceeds to display a Tabs container.

### Tabs Container
    - The Tabs container consists of four main tabs: Overall, DataFrame, Numeric Serie, Text Serie, and Datetime Serie.
    - Users can navigate through these tabs for detailed analysis.

### DataFrame Tab
    - Overview: Displays key information about the dataset, including the number of rows, columns, duplicated rows, and rows with missing values.
    - Columns Information: Provides a static table showcasing column names, data types (text, numeric, date), and memory usage.
    - Interactive Exploration: Allows users to interactively explore the dataset using sliders and radio buttons to control the number of displayed rows and display logic.

### Numeric Serie Tab
    - Numeric Column Selection: Users can select a numeric column to explore.
    - Statistical Information: Displays key statistics such as unique values, missing values, occurrences of 0 values, average, standard deviation, minimum, maximum, and median.
    - Interactive Histogram Chart: Features an interactive Altair histogram chart for visualizing numeric column distribution.
    - Top 20 Most Frequent Values: Lists occurrences and percentages of the top 20 most frequent values.

### Text Serie Tab 
    - Text Column Selection: Users can choose a text column for analysis.
    - Text Information: Presents information on unique values, missing values, rows with empty strings, rows with only whitespaces, and various character-based statistics.
    - Interactive Bar Chart: Displays an Altair bar chart depicting the number of occurrences for each value.
    - Top 20 Most Frequent Values: Lists occurrences and percentages of the top 20 most frequent values.

### Datetime Serie Tab 
    - Datetime Column Selection: Users can select a datetime column for exploration.
    - Datetime Information: Displays statistics on unique values, missing values, minimum and maximum dates, occurrences during weekends and weekdays, cases with future dates, and occurrences of specific date values.
    - Interactive Histogram Chart: Features an Altair histogram chart for visualizing datetime distribution.
    - Top 20 Most Frequent Values: Lists occurrences and percentages of the top 20 most frequent values.

    This application streamlines the process of gaining insights into dataset characteristics, making it a valuable tool for exploratory data analysis.

## Project Structure
### Folder 
  dsp_at3_group25.zip

### Files in the folder 
1. **README.md **

    This mardown file with all the handover documentation needed for anyone to resume, continue and maintain this project. This file contains a description of this project, listing of all Python functions and instructions for running your web app.

2. **requirements.txt**

    This document contains the techinical requirements - the version of each package used for this project setup. 

3. **tab_df/display.py**

    This Python script defines a function, display_tab_df_content, that is intended to be used in a Streamlit application for exploring the DataFrame tab. The function takes a file path to an uploaded CSV file as input. Inside the function:

    - It creates an instance of the Dataset class from the tab_df.logics module, passing the file path as an argument.
    - The set_data method of the Dataset class is then called to compute necessary information about the dataset.
    - The Dataset object is saved into the Streamlit session state for later use.
    - Information about the dataset, such as a summary and column details, is displayed using Streamlit's st.write and st.table functions.
    - The function also includes an expander container for interactive exploration of the dataset. Users can select the number of rows to display using a slider and - - choose the exploration method (head, tail, or sample) using a radio button. Depending on user selections, a subset of the dataset is displayed using Streamlit's st.write.
    - The Dataset class from the tab_df.logics module is responsible for handling the computation of various dataset statistics and properties.

4. **tab_df/logics.py**

    This Python file defines a class named Dataset that is designed to manage a dataset loaded from a CSV file. The class has various attributes to store information about the dataset, including the file path, DataFrame (df), a list of column names (cols_list), and counts of rows, columns, duplicates, missing values, numeric columns, text columns, date columns, and boolean columns. The class provides methods to compute and set these attributes based on the loaded dataset.

    The Dataset class methods include:
    - set_data: Computes various information about the dataset, such as dimensions, duplicates, missing values, numeric columns, text columns, boolean columns, and creates a summary table.
    - set_df: Loads the CSV file into a Pandas DataFrame and stores it as an attribute (self.df) if it hasn't been provided before.
    - is_df_none: Checks if the DataFrame is empty or None.
    - Methods for setting and computing information about columns, dimensions, duplicates, missing values, numeric columns, text columns, boolean columns, and a summary table.
    - Methods for retrieving the head, tail, and a random sample of rows from the DataFrame.
    - set_table: Computes a DataFrame containing the list of columns with their data types and memory usage.
    - get_summary: Formats the computed information into a Pandas DataFrame with two columns: Description and Value, suitable for display in the Streamlit app.
    In summary, this class encapsulates functionality for loading, managing, and computing various statistics and properties of a dataset loaded from a CSV file, facilitating exploratory data analysis in a Streamlit application.

5. **tab_date/display.py**

    This Python script defines a function, display_tab_date_content, intended for use in a Streamlit application to explore datetime columns. The function, given a file path or a loaded DataFrame (both optional), instantiates the DateColumn class from the tab_date.logics module. It then saves this instance into Streamlit session state and calls its find_date_cols() method to identify all datetime columns. Subsequently, the function displays a Streamlit select box containing the list of detected datetime columns. Upon selecting a datetime column from the box, the function calls the set_data() method of the DateColumn class to compute relevant information. It then presents this information in a Streamlit Expander container, including a summary table, a histogram graph, and the results of a frequency analysis. Overall, this function facilitates the exploration and visualization of datetime columns within the Streamlit app.

6. **tab_date/logics.py**

    This Python script defines a class, DateColumn, that manages the analysis and visualization of a column from a DataFrame with a datetime data type. The class includes various attributes such as file path, DataFrame, and several statistical properties of the datetime column, such as the number of unique values, missing values, minimum and maximum values, occurrences during weekends, occurrences not during weekends, occurrences in the future, occurrences equal to '1900-01-01', and occurrences equal to '1970-01-01'. Additionally, it includes attributes for an Altair barchart and a DataFrame containing the most frequent values. The class has methods to find datetime columns, set relevant data for analysis, convert a Pandas Series to datetime data type, and compute various statistical properties. Methods are also provided for generating an Altair barchart and identifying the most frequent values in the column. The class offers a method, get_summary, to format all the computed information for display in a Streamlit application's Overall section. Overall, this class facilitates detailed analysis and visualization of datetime columns in a Streamlit app.

7. **tab_numeric/display.py**

    This Python script defines a function, display_tab_num_content, for a Streamlit application. The function is designed to display the content of a numeric tab, leveraging the functionalities of the NumericColumn class from the tab_num.logics module. It takes optional parameters, file_path (string) and df (Pandas DataFrame), allowing the user to either upload a CSV file or use an already loaded DataFrame.
    Within the function, it instantiates the NumericColumn class, saves it to the Streamlit session state, and calls its methods to find numeric columns and set relevant data for analysis. The function then displays a Streamlit select box with the list of numeric columns found. Once the user selects a numeric column from the select box, it calls the NumericColumn methods to compute the necessary information. Finally, it displays a Streamlit Expander container with a summary table, a histogram graph, and the most frequent values of the selected numeric column.
    This function serves as a modular and interactive way to explore and analyze numeric columns in a Streamlit application.

8. **tab_numeric/logics.py**

    This Python script defines a NumericColumn class designed for managing numeric columns within a Pandas DataFrame. The class provides functionalities for analyzing and visualizing numeric data, including computing descriptive statistics such as mean, standard deviation, minimum, maximum, and median, as well as identifying unique values, missing values, occurrences of zeros, and negative values. The class also generates an Altair histogram and a DataFrame of the most frequent values for a selected numeric column. The script includes methods for loading data, setting up column-specific attributes, and computing various statistical measures and visualizations. Additionally, a Streamlit integration is outlined in a separate function (display_tab_num_content), which uses the NumericColumn class to create an interactive Streamlit app for exploring numeric columns in a dataset, displaying relevant statistics and visualizations. Users can upload a CSV file or use an existing DataFrame, select a numeric column, and explore its characteristics through the Streamlit app.

9. **tab_text/display.py**

    This Python script defines a Streamlit function, display_tab_text_content, intended for exploring and visualizing text columns within a dataset. The function utilizes the TextColumn class from the tab_text.logics module. Upon providing a CSV file path or an existing DataFrame, users can invoke this function to instantiate the TextColumn class, save it in Streamlit session state, and identify all text columns using the find_text_cols method. Subsequently, a Streamlit select box is displayed, enabling users to choose a specific text column for analysis. Upon selection, the set_data method is invoked to compute relevant information about the chosen text column. The function then showcases this information within a Streamlit Expander container, including a table of summary statistics (get_summary), an Altair histogram (histogram), and details about the most frequent values (frequent). This script extends the capabilities of Streamlit for interactive exploration of text data in a user-friendly manner.

10. **tab_text/logics.py**

    The provided Python script defines a TextColumn class for handling text columns within a DataFrame, with associated methods for analysis and visualization. The class attributes include information about the dataset, the text column, and various computed statistics such as unique values, missing values, mode, presence of whitespace, uppercase and lowercase characters, and more. The class provides methods like find_text_cols to identify text columns, set_data to load and analyze a specific text column, and get_summary to format the results for display. Additionally, the script utilizes Altair for generating a barchart and provides a DataFrame containing the most frequent values in the text column. This TextColumn class is designed to be integrated with Streamlit, allowing users to interactively explore and visualize textual data within a Streamlit app.

11. **app/streamlit_app.py**

    This is the main streamlit applicaition, that contains code that allows users to upload a CSV file and explore its content across different tabs, each dedicated to various aspects of data analysis (DataFrame overview, numeric column analysis, text column analysis, and datetime column analysis). The application structure and functionality promote an interactive and user-friendly approach to data exploration.

12. **test/**

    This folder contains some test python files which was used to test some parts of the code to help debug an isolated issue when developing the tab_df functions. These files do not follow a standard unit testing format. 



## Citations
    1. Collaborate on GitHub. https://code.visualstudio.com/docs/sourcecontrol/github. Accessed 14 Oct. 2023.
    2. St.Slider - Streamlit Docs. https://docs.streamlit.io/. Accessed 14 Oct. 2023.
    3. St.Radio - Streamlit Docs. https://docs.streamlit.io/. Accessed 14 Oct. 2023.
    4. St.Table - Streamlit Docs. https://docs.streamlit.io/. Accessed 5 Nov. 2023.
    5. St.Altair_chart - Streamlit Docs. https://docs.streamlit.io/. Accessed 5 Nov. 2023.
    6. St.Dataframe - Streamlit Docs. https://docs.streamlit.io/. Accessed 5 Nov. 2023.
    7. Check the Versions of Python Packages and Libraries | Note.Nkmk.Me. 16 Aug. 2023, https://note.nkmk.me/en/python-package-version/.
    8. Pandas DataFrame Memory_usage() Method. https://www.w3schools.com/python/pandas/ref_df_memory_usage.asp#:~:text=The%20memory_usage()%20method%20returns,memory%20usage%20of%20each%20column. Accessed 5 Nov. 2023.
    9. Converting Object Column in Pandas Dataframe to Datetime A Data Scientists Guide | Saturn Cloud Blog. 19 June 2023, https://saturncloud.io/blog/converting-object-column-in-pandas-dataframe-to-datetime-a-data-scientists-guide/.





