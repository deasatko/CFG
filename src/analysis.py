from statistics import mean

class SalesAnalysis:
    def __init__(self, sales_data):
        self.sales_data = sales_data

    def calculate_total_sales(self):
        return sum(int(row['sales']) for row in self.sales_data)

    def calculate_average_sales(self):
        sales_values = [int(row['sales']) for row in self.sales_data]
        return mean(sales_values)

    def find_highest_sales_month(self):
        sales_dict = {row['month']: int(row['sales']) for row in self.sales_data}
        return max(sales_dict, key=sales_dict.get)

    def find_lowest_sales_month(self):
        sales_dict = {row['month']: int(row['sales']) for row in self.sales_data}
        return min(sales_dict, key=sales_dict.get)

    def calculate_percentage_changes(self):
        sales_values = [int(row['sales']) for row in self.sales_data]
        changes = [0]
        for i in range(1, len(sales_values)):
            percentage_change = ((sales_values[i] - sales_values[i-1]) / sales_values[i-1]) * 100
            changes.append(percentage_change)
        return changes