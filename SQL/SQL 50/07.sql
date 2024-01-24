-- Write your PostgreSQL query statement below
select B.product_name, A.year, A.price from sales as A 
left join product as B
on A.product_id = B.product_id ;