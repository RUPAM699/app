import streamlit as st
import pandas as pd
from file_handler import process_data, plot_pie_chart, plot_line_charts
from datetime import datetime  # Add this import

st.title('Financial Analysis App')

st.subheader("User Details")

# Use text input as a dialog box
user_input = st.text_input("Enter Username:")

# Display the current date and time
current_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H:%M:%S")
st.write(f"Date: {current_date}")
st.write(f"Time: {current_time}")

st.subheader("Upload Your Excel File")

uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
        months, row_sums, income_list, savings_list = process_data(df)
        
        # Create a DataFrame for the month-wise summary
        summary_df = pd.DataFrame({
            'Months': months,
            'Income': income_list,
            'Expenditure': row_sums,
            'Savings': savings_list
        })
        st.subheader('Monthly Summary')
        st.dataframe(summary_df)

        # Calculate total income, expenditure, and savings
        total_income = sum(income_list)
        total_expenditure = sum(row_sums)
        total_savings = total_income - total_expenditure
        percentage_savings = (total_savings / total_income) * 100

        # Create a DataFrame for the yearly summary
        yearly_summary_df = pd.DataFrame({
            'Total Income': [total_income],
            'Total Expenditure': [total_expenditure],
            'Total Savings': [total_savings],
            'Savings (%)': [percentage_savings]
        })
        st.subheader('Yearly Summary')
        st.dataframe(yearly_summary_df)

        st.subheader('Monthly Expenditure Distribution')
        plot_pie_chart(months, row_sums)
        
        st.subheader('Monthly Income vs Monthly Expenditure')
        plot_line_charts(months, income_list, row_sums, savings_list)

        st.subheader('Suggestions and Recommendations')
        if percentage_savings < 20:
            st.warning("Your savings percentage is below 30%. Try to save more.")
        else:
            st.success("Your savings percentage is good. Keep up the good work!")    
        
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.write("Please check the uploaded file and try again.")