select person.firstName, person.lastName, address.city, address.state from Person as person left join Address as address on address.personId = person.personId
