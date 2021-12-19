package ru.webapp.tamik.dao;

import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;
import ru.webapp.tamik.models.Person;
import ru.webapp.tamik.repositories.PersonRepository;

import java.util.List;

@Service
public class PersonDAO {

    private final PersonRepository personRepository;

    public PersonDAO(PersonRepository personRepository) {
        this.personRepository = personRepository;
    }

    public List<Person> index(){
        return personRepository.findAll();
    }


    public Person show(int id){
        return personRepository.findPersonById(id);
    }

    public void save(Person person){
        personRepository.save(person);
    }

    public void update(int id,Person updatedPerson){
        Person personToBeUpdated=show(id);
        personToBeUpdated.setEmail(updatedPerson.getEmail());
        personToBeUpdated.setName(updatedPerson.getName());
        personToBeUpdated.setLastName(updatedPerson.getLastName());
        save(personToBeUpdated);
    }

    public void delete(int id){
        personRepository.delete(personRepository.findPersonById(id));
    }
}
