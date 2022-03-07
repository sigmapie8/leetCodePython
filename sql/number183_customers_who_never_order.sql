select customers.name as Customers from Customers as customers
left join Orders as orders
on customers.id = orders.customerId
where orders.id is null
