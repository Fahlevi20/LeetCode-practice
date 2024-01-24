select  A.name, B.unique_id from employees as A
left join employeeuni as B
on B.id=A.id
order by unique_id; 