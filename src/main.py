from data_loader import DataLoader
from analysis import SalesAnalysis
from visualisation import SalesVisualisation
from output import OutputWriter

def main():
    data_loader = DataLoader("resources/input/sales.csv")
    sales_data = data_loader.load_data()

    sales_analysis = SalesAnalysis(sales_data)

    sales_visualisation = SalesVisualisation(sales_analysis)
    sales_visualisation.plot_bar_chart()

    output_writer = OutputWriter(sales_analysis)
    output_writer.write_to_csv("resources/output/summary.csv")

if __name__ == "__main__":
    main()