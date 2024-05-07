import csv
import statistics
import matplotlib.pyplot as plt 
import seaborn as sns

# 1. Read the data from the spreadsheet
# 2. Collect all of the sales from each month into a single list
# 3. Output the total sales across all months

def read_data(): 
    data = []

    with open("sales.csv", "r") as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    # Task 1
    return data

def calculate_percentage_change(sales):
    changes = [0]
    for i in range(1, len(sales)):
        percentage_change = ((sales[i] - sales[i-1]) / sales[i-1]) * 100
        changes.append(percentage_change)
    return changes


def run():
    data = read_data()

    sales = []
    months = []
    for row in data:
        months.append(row["month"])
        sale = int(row["sales"])
        sales.append(sale)
    # Task 2
    print(sales)
        
# Extended task: Calculate the following:
# Monthly changes as a percentage
# The average
# Months with the highest and lowest sales

    changes = calculate_percentage_change(sales)

    average_sales = statistics.mean(sales)


    highest_sales_month = months[sales.index(max(sales))]
    lowest_sales_month = months[sales.index(min(sales))]
# Extended task, Output a summary of the results to a spreadsheet
    with open("summary.csv", "w", newline = "") as summary_csv:
        writer = csv.writer(summary_csv)
        writer.writerow(["Total Sales", "Average Sales", "Highest Sales Month", "Lowest Sales Month", "Monthly Changes (%)"])
        writer.writerow([sum(sales), average_sales, highest_sales_month, lowest_sales_month, changes])
    # Task 3
    print(sum(sales))


# Creation of Barplot with % Monthly Changes:

    series = {
        "Months":[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sept",
            "Oct",
            "Nov",
            "Dec"
        ],
        "Changes": changes
    }


    sns.barplot(data = series, y = "Changes", x = "Months", palette = "pastel")
    plt.show()

run()
