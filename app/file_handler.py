import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st  # Add this import

def process_data(df):
    try:
        # Adjust column names to match those in your Excel file
        df = df.iloc[0:13, 0:11]
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        expenditure = df.iloc[1:13, 1:10]
        income = df.iloc[0:13, 10]
        row_sums = expenditure.sum(axis=1).tolist()
        income_list = income.tolist()
        savings_list = [income - expenditure for income, expenditure in zip(income_list, row_sums)]

        # Ensure all lists have the same length
        min_length = min(len(months), len(row_sums), len(income_list), len(savings_list))
        months = months[:min_length]
        row_sums = row_sums[:min_length]
        income_list = income_list[:min_length]
        savings_list = savings_list[:min_length]

        return months, row_sums, income_list, savings_list

    except Exception as e:
        print(f"Error in process_data: {e}")
        raise

def plot_pie_chart(months, row_sums):
    try:
        colors = plt.cm.tab20.colors[:len(months)]
        plt.figure(figsize=(10, 6))
        plt.pie(row_sums, labels=months, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.title('Monthly Expenditure Distribution')
        plt.ylabel('')
        st.pyplot(plt)  # Use st.pyplot() to display the plot
    except Exception as e:
        print(f"Error in plot_pie_chart: {e}")
        raise

def plot_line_charts(months, monthly_income, monthly_expenditure, monthly_savings):
    try:
        plt.figure(figsize=(24, 10))
        
        # Line plot for monthly income vs monthly expenditure
        plt.subplot(2, 1, 1)
        sns.lineplot(data=monthly_income, label='Income', marker='o', linestyle='-', color='blue')
        sns.lineplot(data=monthly_expenditure, label='Expenditure', marker='o', linestyle='-', color='red')
        plt.title('Monthly Income vs Monthly Expenditure')
        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.legend()
        plt.xticks(ticks=range(len(months)), labels=months)
        
        # Line plot for monthly savings
        plt.subplot(2, 1, 2)
        sns.lineplot(data=monthly_savings, label='Savings', marker='o', linestyle='-', color='green')
        plt.title('Monthly Savings')
        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.legend()
        plt.xticks(ticks=range(len(months)), labels=months)
        
        plt.tight_layout()
        st.pyplot(plt)  # Use st.pyplot() to display the plot
    except Exception as e:
        print(f"Error in plot_line_charts: {e}")
        raise


