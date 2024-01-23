-- Write your PostgreSQL query statement below
select A.name, B.unique_id from employees as A
left join employeeuni as B
on A.id = B.id;