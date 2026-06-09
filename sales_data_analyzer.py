import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        print("Data loaded successfully.")

    def __del__(self):
        print("Analyzer object deleted.")

    def explore_data(self):
        print("\nFirst 5 Rows:")
        print(self.data.head())
        print("\nInfo:")
        print(self.data.info())
        print("\nStatistics:")
        print(self.data.describe())

    def clean_data(self):
        self.data.drop_duplicates(inplace=True)
        self.data.fillna(0, inplace=True)
        print("Data cleaned.")

    def mathematical_operations(self):
        print("Total Sales:", self.data["Sales"].sum())
        print("Average Sales:", self.data["Sales"].mean())
        print("Maximum Sales:", self.data["Sales"].max())
        print("Minimum Sales:", self.data["Sales"].min())

    def combine_data(self, other_df):
        combined = pd.concat([self.data, other_df])
        return combined

    def split_data(self):
        return dict(tuple(self.data.groupby("Region")))

    def search_sort_filter(self):
        print(self.data[self.data["Sales"] > 30000])
        print(self.data.sort_values(by="Sales", ascending=False))

    def aggregate_functions(self):
        print(self.data.groupby("Region")["Sales"].agg(["sum","mean","count"]))

    def statistical_analysis(self):
        print("Std:", self.data["Sales"].std())
        print("Variance:", self.data["Sales"].var())
        print("Quantiles:")
        print(self.data["Sales"].quantile([0.25,0.5,0.75]))

    def create_pivot_table(self):
        pivot = pd.pivot_table(self.data, values="Sales",
                               index="Region",
                               columns="Product",
                               aggfunc="sum")
        print(pivot)

    def visualize_data(self):
        plt.figure(figsize=(6,4))
        self.data.groupby("Product")["Sales"].sum().plot(kind="bar")
        plt.title("Sales by Product")
        plt.tight_layout()
        plt.savefig("bar_chart.png")
        plt.close()

        plt.figure(figsize=(6,4))
        plt.plot(self.data["Date"], self.data["Sales"])
        plt.title("Sales Trend")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("line_chart.png")
        plt.close()

        sns.scatterplot(data=self.data, x="Sales", y="Profit")
        plt.savefig("scatter_chart.png")
        plt.close()

        print("Charts saved successfully.")

def menu():
    analyzer = SalesDataAnalyzer("sales_data.csv")

    while True:
        print("\\n===== SALES DATA ANALYZER =====")
        print("1. Explore Data")
        print("2. Clean Data")
        print("3. Mathematical Operations")
        print("4. Search/Sort/Filter")
        print("5. Aggregate Functions")
        print("6. Statistical Analysis")
        print("7. Pivot Table")
        print("8. Visualizations")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            analyzer.explore_data()
        elif choice == "2":
            analyzer.clean_data()
        elif choice == "3":
            analyzer.mathematical_operations()
        elif choice == "4":
            analyzer.search_sort_filter()
        elif choice == "5":
            analyzer.aggregate_functions()
        elif choice == "6":
            analyzer.statistical_analysis()
        elif choice == "7":
            analyzer.create_pivot_table()
        elif choice == "8":
            analyzer.visualize_data()
        elif choice == "9":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
