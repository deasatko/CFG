import matplotlib.pyplot as plt
import seaborn as sns

class SalesVisualisation:
    def __init__(self, sales_analysis):
        self.sales_analysis = sales_analysis

    def plot_bar_chart(self):
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        changes = self.sales_analysis.calculate_percentage_changes()

        series = {"Months": months, "Changes": changes}

        sns.barplot(data=series, y="Changes", x="Months", hue="Months", palette="pastel", legend=False)
        plt.show()