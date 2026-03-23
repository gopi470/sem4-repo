package com.example.demo.controller;

import com.example.demo.dto.AuthResponse;
import com.example.demo.dto.LoginRequest;
import com.example.demo.dto.RegisterRequest;
import com.example.demo.entity.User;
import com.example.demo.repository.UserRepository;
import com.example.demo.security.JwtUtil;
import com.example.demo.service.UserService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/auth")
@RequiredArgsConstructor
public class UserController {

	private final UserService userService;
	private final JwtUtil jwtUtil;
	private final UserRepository userRepository;

	@PostMapping("/register")
	public ResponseEntity<AuthResponse> register(@Valid @RequestBody RegisterRequest request) {
		try {
			AuthResponse response = userService.register(request);
			return ResponseEntity.status(HttpStatus.CREATED).body(response);
		} catch (RuntimeException e) {
			return ResponseEntity.badRequest()
					.body(new AuthResponse(null, null, null, null, e.getMessage()));
		}
	}

	@PostMapping("/login")
	public ResponseEntity<AuthResponse> login(@Valid @RequestBody LoginRequest request) {
		try {
			AuthResponse response = userService.login(request);
			return ResponseEntity.ok(response);
		} catch (RuntimeException e) {
			return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
					.body(new AuthResponse(null, null, null, null, e.getMessage()));
		}
	}

	@GetMapping("/validate-token")
	public ResponseEntity<AuthResponse> validateToken(@RequestHeader("Authorization") String authorizationHeader) {
		try {
			// Extract token from "Bearer {token}" format
			String token = authorizationHeader.substring(7);

			// Extract username and role from token
			String username = jwtUtil.extractUsername(token);
			String role = jwtUtil.extractRole(token);

			// Validate token
			if (!jwtUtil.validateToken(token, username)) {
				return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
						.body(new AuthResponse(null, null, null, null, "Invalid or expired token"));
			}

			// Get user details from database
			User user = userRepository.findByUsername(username)
					.orElseThrow(() -> new RuntimeException("User not found"));

			return ResponseEntity.ok(new AuthResponse(
					user.getId(),
					user.getUsername(),
					user.getRole().name(),
					null,
					"Token is valid"));
		} catch (Exception e) {
			return ResponseEntity.status(HttpStatus.UNAUTHORIZED)
					.body(new AuthResponse(null, null, null, null, "Invalid token"));
		}
	}
}
