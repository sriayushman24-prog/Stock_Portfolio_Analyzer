
# Stock Market Analyzer & Portfolio Analyzer

## About This Project

I built this project to explore how Python can be used to analyze the stock market and understand investment performance. I wanted to work on something beyond what I learn in the classroom and apply my programming skills to a real-world topic.
I started by building a program that analyzes individual stocks and then expanded it to simulate an investment portfolio. The application uses historical stock price data to calculate returns, compare stocks, create graphs, and analyze portfolio performance.
I divided the project into two levels, gradually adding more features as I developed my Python skills.

## Features

### Level 1: Individual Stock Analysis

- **Stock Selection:** Choose a stock from the available tickers in the dataset.
- **Date Range:** Select a specific start and end date for the analysis or use the full available date range.
- **Stock Statistics:** Calculate the starting price, ending price, total return, and average daily return.
- **Best and Worst Days:** Find the days with the largest daily gain and loss, including their dates.
- **Stock Price Graph:** Visualize how a stock's closing price changes over time.
- **Daily Returns Graph:** View the percentage change in a stock's price from one trading day to the next.
- **Stock Comparison:** Compare two stocks using graphs and numerical statistics.

### Level 2: Portfolio Analysis

- **Build a Portfolio:** Choose multiple stocks and assign an investment percentage to each one.
- **Investment Simulation:** Enter an initial investment amount and see how the portfolio would have performed historically.
- **Portfolio Value:** Track how the total value of the portfolio changes over time.
- **Profit and Loss:** Calculate the portfolio's ending value, dollar profit or loss, and total return.
- **Portfolio Allocation:** View how the investment is divided among the selected stocks.
- **Daily Portfolio Returns:** Analyze daily changes in the portfolio's value.
- **Annualized Volatility:** Estimate how much the portfolio's returns fluctuate over a year.
- **Maximum Drawdown:** Measure the largest percentage drop from a previous portfolio peak.
- **Moving Averages:** Calculate 20-day and 50-day moving averages to examine stock price trends.
- **Portfolio Dashboard:** Choose which portfolio graphs to view through a menu.

## Technologies Used

- **Python:** Used to build the application and perform calculations.
- **Pandas:** Used to read, clean, filter, and analyze stock price data.
- **Matplotlib:** Used to create graphs and visualize stock and portfolio performance.
- **CSV:** Used to store the historical stock market data.

## Getting Started

### 1. Requirements

You will need Python installed on your computer, along with the Pandas and Matplotlib libraries.
Install the libraries by running this command in your terminal:

```bash
pip install pandas matplotlib
```

### 2. Clone the Repository

Run the following commands in your terminal:

```bash
git clone https://github.com/sriayushman24/Stock_Portfolio_Analyzer.git
cd Stock_Portfolio_Analyzer
```
### 3. Add the Dataset

The program uses a CSV file named:

`tech_stock_prices_2020_to_today.csv`

Place this file in the same folder as the Python program.

The dataset must contain these columns:

- `Date` — The date of the stock record.
- `Ticker` — The stock symbol.
- `Close` — The closing price of the stock.

The program checks and cleans the data before using it for analysis. If the dataset is not included in the repository, you will need to obtain it separately.

### 4. Run the Program

```bash
python main.py
```
## How to Use the Application

When the program starts, it displays a main menu with two main options.

### Individual Stock Analysis

1. Choose the individual stock analysis option.
2. Select a stock from the available tickers.
3. Enter a start date and end date, or press Enter to use the full available date range.
4. Review the stock analysis report.
5. Choose which graphs to view, compare stocks, or compare their statistics.

### Portfolio Analysis

1. Choose the portfolio analysis option.
2. Select a date range.
3. Enter your initial investment amount.
4. Choose the stocks you want to include in your portfolio.
5. Assign a percentage to each stock until the total reaches 100%.
6. Review the portfolio report, including returns, annualized volatility, and maximum drawdown.
7. Use the dashboard to explore the portfolio graphs.

## What I Learned

While building this project, I practiced using Python functions, loops, dictionaries, conditional statements, and exception handling. I also learned how to use Pandas to clean and analyze data and Matplotlib to create graphs.
One of the more interesting parts of the project was learning how to calculate investment returns and use them to analyze a portfolio instead of looking at individual stock prices alone.
Building the project in two levels helped me start with simpler calculations before moving on to more advanced features, such as portfolio simulations, moving averages, volatility, and maximum drawdown.

## Author

**Ayushman Sri Murugathas**

GitHub: https://github.com/sriayushman24
