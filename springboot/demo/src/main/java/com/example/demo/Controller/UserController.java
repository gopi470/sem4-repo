package com.example.demo.Controller;


import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.RequestBody;

import com.example.demo.Model.User;
import com.example.demo.Repository.UserRepository;

import java.util.List;

@RestController
@RequestMapping("/api")



public class UserController {
    @Autowired
    private UserRepository userRepository;

    // public UserController(UserRepository userRepository) {
    //     this.userRepository = userRepository;
    // }


    @GetMapping
    public String home() {
        return "API is running";
    }


//Read all

 
    @GetMapping("/users")
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    @GetMapping("/raw")
    public Object raw() {
        return userRepository.findAll();
    }

    @GetMapping("/users/{id}")
    public User getUserById(@PathVariable String id) {
        return userRepository.findById(id).orElse(null);
    }

    @PostMapping("/post")
    public User createUser(@RequestBody User user) {
        return userRepository.save(user);
    }

    @DeleteMapping("/{id}")
    public String deleteUser(@PathVariable String id) {
        userRepository.deleteById(id);
        return "User deleted successfully";
    }

    @PutMapping("/{id}")
    public User updateUser(@PathVariable String id,
                           @RequestBody User updatedUser) {

        return userRepository.findById(id).map(user -> {
            user.setName(updatedUser.getName());
            user.setAge(updatedUser.getAge());
            return userRepository.save(user);
        }).orElse(null);
    }

    @PatchMapping("/{id}")
    public User patchUser(@PathVariable String id, @RequestBody User partialUpdate) {
        return userRepository.findById(id).map(existingUser -> {

            if (partialUpdate.getName() != null) {
                existingUser.setName(partialUpdate.getName());
            }

            if (partialUpdate.getAge() > 0) {
                existingUser.setAge(partialUpdate.getAge());
            }
            return userRepository.save(existingUser);
        }).orElseThrow(() -> new RuntimeException("User not found"));

    }




}