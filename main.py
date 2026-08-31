import sys
import pandas as pd

# Load the dataset
file_path = "tech_stock_prices_2020_to_today.csv"
df = pd.read_csv(file_path)

# Ensure the Date column is parsed as datetime
df["Date"] = pd.to_datetime(df["Date"])
while True:

    # Display the available tickers for the user
    available_tickers = df["Ticker"].unique()
    print("\nAvailable Stocks:", ", ".join(available_tickers))

    # Get user input for stock selection
    stock_input = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
    if stock_input == "EXIT":
        print("\nThank you for using the Stock Market Analyzer")
        sys.exit(0)
    # Filter dataframe for the selected stock and sort by date
    stock_data = df[df["Ticker"] == stock_input].sort_values("Date").copy()

    if stock_data.empty:
        print(f"Error: No data found for ticker '{stock_input}'.")
    else:
        # Extract the first and last available dates
        start_date_str = stock_data["Date"].iloc[0].strftime("%b %d, %Y")
        end_date_str = stock_data["Date"].iloc[-1].strftime("%b %d, %Y")

        # Get starting and ending prices
        starting_price = stock_data["Close"].iloc[0]
        ending_price = stock_data["Close"].iloc[-1]

        # Calculate total return over the entire dataset
        total_return = ((ending_price - starting_price) / starting_price) * 100

        # Calculate daily returns
        stock_data["Return"] = stock_data["Close"].pct_change() * 100

        # Calculate average daily return
        avg_daily_return = stock_data["Return"].mean()

        # Find best and worst daily returns
        best_day = stock_data["Return"].max()
        worst_day = stock_data["Return"].min()

        # Find the dates of the best and worst days
        best_day_date = stock_data.loc[
            stock_data["Return"].idxmax(), "Date"
        ].strftime("%b %d, %Y")

        worst_day_date = stock_data.loc[
            stock_data["Return"].idxmin(), "Date"
        ].strftime("%b %d, %Y")

        # Print the formatted report
        print("\n" + "=" * 60)
        print("                    STOCK MARKET ANALYZER")
        print("=" * 60)
        print(f"\nStock: {stock_input}")
        print(f"Period: {start_date_str} → {end_date_str}")
        print("-" * 60)
        print(f"{stock_input} ANALYSIS")
        print("-" * 60)
        print(f"Starting Price:         ${starting_price:.2f}")
        print(f"Ending Price:           ${ending_price:.2f}")
        print(f"\nTotal Return:           {total_return:+.2f}%")
        print(f"Average Daily Return:   {avg_daily_return:+.2f}%")
        print(f"Best Day:               {best_day:+.2f}% ({best_day_date})")
        print(f"Worst Day:              {worst_day:+.2f}% ({worst_day_date})")
        print("=" * 60)
        print("\nEnter another symbol to continue or enter Exit to exit.")