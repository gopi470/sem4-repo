package com.example.demo.security;

public class JwtUtil {
    public String extractUsername(String token) {
        return token;
    }

    public String extractRole(String token) {
        return token;
    }

    public boolean validateToken(String token, String username) {
        return false;
    }
}
