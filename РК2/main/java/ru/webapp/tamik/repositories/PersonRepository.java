package ru.webapp.tamik.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import ru.webapp.tamik.models.Person;

@Repository
public interface PersonRepository extends JpaRepository<Person,Integer> {
    Person findPersonById(int id);
}
