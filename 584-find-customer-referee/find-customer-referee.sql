-- # Write your MySQL query statement below
-- -- select name from Customer 
-- -- where referee_id!=2 or referee_id is null;


-- select name from customer where referee_id not in (select referee_id from customer where referee_id = 2);



SELECT name FROM customer WHERE referee_id != 2 OR referee_id IS NULL;