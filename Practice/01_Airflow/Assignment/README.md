## Home assignment

You need to create 2 DAGs:
1) #### "Price trend analyzer"  
    Create a DAG that fetches the Bitcoin price with a 1 minute interval. The API address and access is given to you in the forum.  
    Store the price in the Airflow Postgres database (alternatively: use a separate database for the solution to be more production-like. E.g., you can use an additional Postgres or MySQL database).   
    Calculate the rolling average price over the last 15 minutes, and store it also in the database.  
    Create a buy/sell alert.  
    * Buy alert rule: 
      * if the current price has been below the rolling average price for at least the past 3 minutes, but then moves above the average price, trigger a buy.  
    * Sell alert rule: 
      * if the current price has been above the rolling average price for at least the past 3 minutes, but then moves below the average price, trigger a sell.  
    
    In either case, create and save a JSON file with the keys:  
    * `orderType` (_enum_, options: ["Buy","Sell"])
    * `currentPrice` (_float_)
    * `rollingAveragePrice` (_float_)


2) #### "Order trigger"  
    Set up a sensor so that the DAG is triggered once the JSON file in 1) has been created.  
    Push the JSON payload into the order API. The API access and credentials are given to you in the forum.  
    Occasionally, the API will return with an error (503, Service Unavailable). In such cases, wait 5 seconds and retry again, with a maximum 3 retries.  
    Log all payloads and responses in the database.  

The assignment is to be done individually.

Deadline: October 12, 2023.

The assignment will not be graded.

The students who present their solution in the session on Oct 12 can earn up to 5 bonus points towards their course grade.