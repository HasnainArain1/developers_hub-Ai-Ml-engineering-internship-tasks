# Task 2 – Stock Price Prediction (Short-Term)

## Objective
To predict the next day’s closing price of a selected stock using historical market data and machine learning models.

## Dataset Used
- Source: Yahoo Finance
- Library: yfinance
- Stock Selected: Apple (AAPL)
- Time Period: 2018–2024
- Features:
  - Open
  - High
  - Low
  - Volume
- Target Variable:
  - Next Day Closing Price (shifted Close value)

## Models Applied
- Linear Regression

## Key Results & Findings
- Linear Regression achieved strong predictive performance.
- MAE: 1.65
- RMSE: 2.22
- R² Score: 0.956
- The model explains approximately 95.6% of the variance in next-day closing prices.
- Stock prices show strong autocorrelation, which supports short-term prediction.
- High statistical accuracy does not guarantee trading profitability.
- The model does not account for external factors such as news events or market sentiment.

## Tools & Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- yfinance
- Jupyter Notebook
