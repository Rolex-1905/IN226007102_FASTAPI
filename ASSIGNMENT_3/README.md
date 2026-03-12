# FastAPI Assignment 3 – Internship Task

## Intern Details

**Name:** Neeraj  
**Intern ID:** IN226007102  
**Module:** FastAPI – Assignment 3  
**Organization:** Innomatics Research Labs  

---

## Project Description

This assignment focuses on implementing CRUD (Create, Read, Update, Delete) operations in a FastAPI-based E-commerce API.

The objective of the task was to extend the existing product management system by allowing products to be added, updated, removed, and analyzed through additional API endpoints.

The assignment demonstrates how FastAPI can be used to build dynamic and maintainable backend systems that support real-world operations such as inventory updates, product lifecycle management, and store analytics.

---

## Concepts Implemented

During this assignment the following FastAPI concepts were implemented:

- POST Requests for creating new product entries
- PUT Requests for updating product attributes such as price and stock status
- DELETE Requests for removing products from the catalogue
- Query Parameters for updating product fields dynamically
- Path Parameters for targeting specific product resources
- Business Logic to handle product updates, deletion checks, and duplicate validation
- Inventory Summary Calculations to analyze store data and generate audit reports

These concepts help simulate the backend behavior of a real-world product inventory management system.

---

## Features Implemented

### Product Creation

A product creation feature was implemented using the **POST /products** endpoint.

This allows new products to be added dynamically without modifying the source code. The system automatically generates unique product IDs and prevents duplicate product names to maintain catalogue integrity.

---

### Product Updates

A product update mechanism was implemented using the **PUT /products/{product_id}** endpoint.

This allows product attributes such as price and stock availability to be modified. Multiple fields can be updated in a single request using query parameters, making the API flexible for real-time inventory updates.

---

### Product Deletion

A product deletion feature was implemented using the **DELETE /products/{product_id}** endpoint.

This allows administrators to remove discontinued or unavailable products from the catalogue. Error handling ensures that attempts to delete non-existent products return appropriate responses.

---

### Complete Product Lifecycle (CRUD Workflow)

A full CRUD workflow was demonstrated by performing the following operations sequentially:

1. Creating a new product using POST
2. Retrieving product details using GET
3. Updating product attributes using PUT
4. Deleting the product using DELETE

This workflow simulates how a product may be introduced, updated, and eventually removed from an e-commerce system.

---

### Inventory Audit Dashboard

An inventory audit endpoint was implemented to generate a summary of the store’s inventory.

The dashboard provides the following information:

- Total number of products
- Number of products currently in stock
- Names of products that are out of stock
- Total value of available inventory
- The most expensive product in the catalogue

This endpoint demonstrates how APIs can provide analytical insights in addition to basic data retrieval.

---

### Category-Wide Discount System (Bonus)

A bulk discount system was implemented using the **PUT /products/discount** endpoint.

This feature allows administrators to apply a percentage discount to all products within a specified category in a single request.

The API calculates updated prices dynamically and returns the list of modified products, making it useful for seasonal sales or promotional campaigns.

---

## Conclusion

This assignment demonstrates the implementation of CRUD operations and inventory management features using FastAPI.

By integrating product creation, updates, deletion, and analytical reporting, the API simulates a practical backend system for an e-commerce platform.

The project highlights how FastAPI can efficiently handle data manipulation, validation, and business logic, making it well suited for building scalable backend services.
