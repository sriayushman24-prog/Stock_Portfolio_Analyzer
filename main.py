import pandas as pd

# Load the dataset
file_path = "tech_stock_prices_2020_to_today.csv"
df = pd.read_csv(file_path)

# Ensure the Date column is parsed as datetime
df["Date"] = pd.to_datetime(df["Date"])

# Display available tickers for the user
available_tickers = df["Ticker"].unique()
print("Available Stocks:", ", ".join(available_tickers))

# Get user inputs for stock selection and date range
stock_input = input("Enter stock (e.g., AAPL): ").strip().upper()
start_date_input = input("Enter start date (YYYY-MM-DD): ").strip()
end_date_input = input("Enter end date (YYYY-MM-DD): ").strip()

# Filter dataframe based on user selections
filtered_df = df[df["Ticker"] == stock_input].sort_values("Date")

if filtered_df.empty:
    print(f"Error: No data found for ticker '{stock_input}'.")
else:
    # Filter by date range
    mask = (filtered_df["Date"] >= start_date_input) & (
        filtered_df["Date"] <= end_date_input
    )
    stock_data = filtered_df.loc[mask]

    if stock_data.empty:
        print(
            f"Error: No data found for {stock_input} between {start_date_input} and {end_date_input}."
        )
    else:
        # Extract metrics
        start_date_str = stock_data["Date"].iloc[0].strftime("%b %d, %Y")
        end_date_str = stock_data["Date"].iloc[-1].strftime("%b %d, %Y")

        starting_price = stock_data["Close"].iloc[0]
        ending_price = stock_data["Close"].iloc[-1]
        total_return = ((ending_price - starting_price) / starting_price) * 100

        # Calculate daily returns if not already present or compute fresh
        stock_data["Return"] = stock_data["Close"].pct_change() * 100

        avg_daily_return = stock_data["Return"].mean()
        best_day = stock_data["Return"].max()

        worst_day = stock_data["Return"].min()

        # Print the formatted report
        print("\n" + "=" * 40)
        print("       STOCK MARKET ANALYZER")
        print("=" * 40)
        print(f"\nStock: {stock_input}")
        print(
            f"Period: {start_date_str} → { end_date_str}"
        )
        print("-" * 40)
        print(f"{stock_input} ANALYSIS")
        print("-" * 40)
        print(f"Starting Price:        ${starting_price:.2f}")
        print(f"Ending Price:          ${ending_price:.2f}")
        print(f"\nTotal Return:          {total_return:+.2f}%")
        print(f"Average Daily Return:   {avg_daily_return:+.2f}%")
        print(f"Best Day:              {best_day:+.2f}%")
        print(f"Worst Day:             {worst_day:+.2f}%")
        print("=" * 40)