# FastAPI Assignment 2 – Internship Task

## Intern Details

**Name:** Neeraj  
**Intern ID:** IN226007102  
**Module:** FastAPI – Assignment 2  
**Organization:** Innomatics Research Labs  

---

## Project Description

This assignment extends the E-commerce Store API developed in Day 1 using FastAPI.  
The objective of this task was to implement additional API features including query parameter filtering, lightweight data retrieval, data validation using Pydantic, and business logic for handling orders.

The assignment demonstrates how FastAPI can be used to build structured and validated APIs for real-world applications such as an online store system.

---

## Concepts Implemented

During this assignment the following FastAPI concepts were implemented:

- Query Parameters for filtering products based on conditions such as minimum price.
- Path Parameters for retrieving specific product information.
- Pydantic Models for validating request data.
- POST Requests to accept and process user input.
- Business Logic implementation inside API endpoints.
- Data validation rules such as minimum length, value ranges, and optional fields.

These concepts help ensure that the API handles user input securely and returns structured responses.

---

## Features Implemented

### Product Price Lookup

A lightweight endpoint was implemented to retrieve only the name and price of a product based on its product ID.  
This allows applications such as shopping carts to access minimal data without loading full product details.

### Product Filtering

Product filtering functionality was enhanced using query parameters.  
Users can now filter products based on price conditions, allowing more flexible product searches.

### Customer Feedback System

A feedback system was implemented to allow customers to submit ratings and comments for products.  
The input data is validated using Pydantic to ensure that ratings fall within an acceptable range and customer details follow the required format.

### Product Summary Dashboard

A dashboard-style endpoint was implemented to provide an overview of the store.  
It calculates statistics such as the total number of products, stock availability, price extremes, and category distribution.

### Bulk Order Processing

A bulk ordering system was developed for corporate clients who may need to purchase multiple products at once.  
The API validates order data, checks product availability, calculates totals, and processes valid items while reporting failures for invalid or unavailable products.

### Order Status Tracking (Bonus)

A simple order tracking system was introduced where newly created orders start with a pending status.  
Orders can later be confirmed through a dedicated endpoint, allowing a two-step order approval workflow.

---

## Conclusion

This assignment demonstrates the use of FastAPI for building more advanced REST APIs with validation, filtering, and structured business logic.  
By combining Pydantic models with FastAPI endpoints, the application ensures reliable input validation and organized API responses.

The project highlights how FastAPI can be used to design scalable backend services for applications such as e-commerce platforms.
