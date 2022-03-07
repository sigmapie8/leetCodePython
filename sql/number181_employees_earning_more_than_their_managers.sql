select employee.name as Employee from Employee as employee 
inner join Employee as employee2
on employee.managerId = employee2.id
where employee.salary > employee2.salary
