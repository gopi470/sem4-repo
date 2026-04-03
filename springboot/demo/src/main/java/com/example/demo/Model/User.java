package com.example.demo.Model;



import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.List;


@Data
@NoArgsConstructor
@AllArgsConstructor


@Document(collection="lab")
public class User {



    @Id
    private String id;


    private String name;
    private Integer age;
}