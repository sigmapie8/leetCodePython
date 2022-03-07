select person.email from Person as person
group by person.email
having count(person.email) > 1
