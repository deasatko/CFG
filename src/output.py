import csv

class OutputWriter:
    def __init__(self, sales_analysis):
        self.sales_analysis = sales_analysis

    def write_to_csv(self, filename):
        with open(filename, "w", newline="") as summary_csv:
            writer = csv.writer(summary_csv)
            writer.writerow(["Total Sales", "Average Sales", "Highest Sales Month", "Lowest Sales Month", "Monthly Changes (%)"])
            
            total_sales = self.sales_analysis.calculate_total_sales()
            average_sales = self.sales_analysis.calculate_average_sales()
            highest_sales_month = self.sales_analysis.find_highest_sales_month()
            lowest_sales_month = self.sales_analysis.find_lowest_sales_month()
            changes = self.sales_analysis.calculate_percentage_changes()
            
            writer.writerow([total_sales, average_sales, highest_sales_month, lowest_sales_month, changes])