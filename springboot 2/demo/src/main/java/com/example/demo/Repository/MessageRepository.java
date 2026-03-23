package com.example.demo.Repository;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface MessageRepository extends MongoRepository<Task, String> {
}