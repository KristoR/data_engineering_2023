## Assignment
The Postgres database dump in this folder includes a simple grocery store supply chain for sales orders and product stock. 

Currently, there are often cases where products run out of stock. You are tasked with creating reporting / alerting on stock that has run out or is about to run out. 

The things to consider are: 
* `products` table 
  * `avg_days_to_replenish` - this is the amount of days it takes to order stock from suppliers
  * `expiration_date` - this is the date when the current stock will expire and have to be removed from stock
* `stock` table
  * `status = arriving` indicates that this product and amount is expected to arrive in stock on the specified `date`
* `sales` table
  * Business expects that calculating the average sales per product/day from this table can be used as ground truth for predicting the future.

One indication from business is that they would like the reporting to follow a coloring scheme:
* red --> this product is out of stock, should be replenished immediately 
* orange --> this product is not yet out of stock, but is expected to go out of stock before a new replenishment arrives
* yellow --> this product will go out of stock if a new replenishment is not ordered in the next 7 days
* green --> this product is in stock and not in need of replenishment in the next 7 days

Feel free to implement any additional logic in your solution that you think would be useful.

In your solution, you need to implement at least one dbt **macro** and two dbt **models** to transform the data accordingly.  

Use **snapshotting** for at least the coloring scheme table. 

Once everything is set up, insert data from `sales_lastday` into `sales` and rerun the snapshots accordingly to note any changes that occurred.

The assignment is to be done individually.

Deadline: October 12, 2023.

The assignment will not be graded.

The students who present their solution in the session on Oct 12 can earn up to 5 bonus points towards their course grade.
