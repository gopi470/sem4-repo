package com.example.demo.service;

import com.example.demo.dto.AuthResponse;
import com.example.demo.dto.LoginRequest;
import com.example.demo.dto.RegisterRequest;
import jakarta.validation.Valid;

public class UserService {
    public AuthResponse login(@Valid LoginRequest request) {
        return null;
    }

    public AuthResponse register(@Valid RegisterRequest request) {
        return null;
    }
}
