import sys
import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])
    return df


# Display available stocks
def display_tickers(df):
    available_tickers = df["Ticker"].unique()
    print("\nAvailable Stocks:", ", ".join(available_tickers))


# Get stock data for the selected ticker
def get_stock_data(df, stock_input):
    return df[df["Ticker"] == stock_input].sort_values("Date").copy()


# Calculate stock statistics
def analyze_stock(stock_data):
    starting_price = stock_data["Close"].iloc[0]
    ending_price = stock_data["Close"].iloc[-1]

    total_return = ((ending_price - starting_price) / starting_price) * 100

    # Calculate daily returns
    stock_data["Return"] = stock_data["Close"].pct_change() * 100

    avg_daily_return = stock_data["Return"].mean()

    best_day = stock_data["Return"].max()
    worst_day = stock_data["Return"].min()

    best_day_date = stock_data.loc[
        stock_data["Return"].idxmax(), "Date"
    ].strftime("%b %d, %Y")

    worst_day_date = stock_data.loc[
        stock_data["Return"].idxmin(), "Date"
    ].strftime("%b %d, %Y")

    return (
        starting_price,
        ending_price,
        total_return,
        avg_daily_return,
        best_day,
        worst_day,
        best_day_date,
        worst_day_date
    )


# Display the analysis report
def display_report(stock_input, stock_data, results):
    (
        starting_price,
        ending_price,
        total_return,
        avg_daily_return,
        best_day,
        worst_day,
        best_day_date,
        worst_day_date
    ) = results

    start_date_str = stock_data["Date"].iloc[0].strftime("%b %d, %Y")
    end_date_str = stock_data["Date"].iloc[-1].strftime("%b %d, %Y")

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

# Main program
def main():

    file_path = "tech_stock_prices_2020_to_today.csv"

    # Load data once
    df = load_data(file_path)

    while True:

        # Display available stocks
        display_tickers(df)

        # Get original stock selection
        stock_input = input(
            "\nEnter stock symbol (e.g., AAPL): "
        ).strip().upper()

        # Exit program
        if stock_input == "EXIT":
            print("\nThank you for using the Stock Market Analyzer")
            sys.exit(0)

        # Get data for selected stock
        stock_data = get_stock_data(df, stock_input)

        # Check if stock exists
        if stock_data.empty:
            print(
                f"Error: No data found for ticker '{stock_input}'."
            )
            continue

        # Analyze stock
        results = analyze_stock(stock_data)

        # Display text report
        display_report(
            stock_input,
            stock_data,
            results
        )


        print(
            "\nEnter another symbol to continue "
            "or enter Exit to exit."
        )

# Start the program
main()