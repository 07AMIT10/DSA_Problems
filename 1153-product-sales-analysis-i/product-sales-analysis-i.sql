# Write your MySQL query statement below
select product_name, year, price from Product p
right join Sales s
on s.product_id=p.product_id;