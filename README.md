# AI-Event-Market-Prediction
Prediction of market based on major events in the field of AI

# 1. Data Ingestion
Commands for installing the AIID (AI Incidents Database)

1. ```cd data\raw\aiid
curl.exe --ssl-no-revoke -L -O https://pub-72b2b2fc36ec423189843747af98f80e.r2.dev/backup-20260928101247.tar.bz2
tar -xjf backup-20260928101247.tar.bz2```

2. Extract market data using yfinance
`px = yf.download(tickers, auto_adjust=True, progress=True, start=start)`

3. Download Forecast-Dojo for MArket reaction and news database
run the below python script in the terminal 
``