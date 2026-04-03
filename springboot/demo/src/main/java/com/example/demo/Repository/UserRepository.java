package com.example.demo.Repository;

import com.example.demo.Model.User;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

public interface  UserRepository extends MongoRepository <User,String>
{

}
