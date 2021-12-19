package ru.webapp.tamik.models;

import lombok.Data;

import javax.persistence.*;

import javax.validation.constraints.Email;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.Size;


@Data
@Entity
@Table(name="Person")
public class Person {
    @Id
    @Column(name="id")
    @GeneratedValue
    Integer id;

    @NotEmpty(message= "Имя не может быть пустым")
    @Size(min=2,max=30,message="Имя должно быть не меньше 2 и не больше 30 букв")
    @Column(name="name")
    private String name;

    @NotEmpty(message= "Фамилия не может быть пустой")
    @Size(min=2,max=30,message="Фамилия должна быть не меньше 2 и не больше 30 букв")
    @Column(name="lastName")
    private String lastName;

    @Email(message="Емаил введен неправильно")
    @Column(name="email")
    private String email;

    public Person() {
    }

    public Person(String name, String lastName, String email) {
        this.name = name;
        this.lastName = lastName;
        this.email = email;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
