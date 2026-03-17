# FastAPI Assignment 5 – Internship Task

## Intern Details

**Name:** Neeraj  
**Intern ID:** IN226007102  
**Module:** FastAPI – Assignment 5  
**Organization:** Innomatics Research Labs  

---

## Project Description

This assignment focuses on implementing three essential features used in real-world APIs: **Search, Sort, and Pagination** using FastAPI.

The objective of this task was to enhance an existing e-commerce API by adding advanced data handling capabilities. These features simulate how modern applications allow users to efficiently find, organize, and navigate large datasets.

The assignment includes testing existing endpoints as well as building new endpoints that integrate search, sorting, and pagination logic into a complete backend system.

---

## Concepts Implemented

During this assignment, the following FastAPI concepts were implemented:

- Query parameter handling for search, sorting, and pagination.
- Case-insensitive searching using string matching.
- Sorting data dynamically based on different fields and order.
- Pagination logic using page and limit calculations.
- Combining multiple operations (search + sort + pagination) in a single endpoint.
- Conditional logic and validation for query parameters.
- Error handling with meaningful messages for invalid inputs.
- API design for scalable and user-friendly data retrieval.

These concepts demonstrate how APIs manage large datasets efficiently and provide flexible data access to users.

---

## Features Implemented

### Product Search Functionality

A search endpoint was tested to allow users to find products using keywords.  
The search is case-insensitive, ensuring consistent results regardless of input format.  
If no matching products are found, the API returns a user-friendly message instead of an empty list.

---

### Product Sorting System

Sorting functionality was implemented to organize products based on:

- Price (Low to High and High to Low)
- Name (A to Z and Z to A)

Default sorting is applied when no parameters are provided.  
The API also validates sorting fields and returns an error message for invalid inputs such as unsupported fields.

---

### Product Pagination

Pagination was implemented to divide product data into smaller chunks for better usability.  
Users can navigate through pages using page number and limit parameters.

The system calculates:
- Total number of pages
- Products per page
- Behavior when page exceeds available data (returns empty list)

---

### Orders Search Feature

A new endpoint was developed to search orders based on customer name.  
The search is case-insensitive and returns all matching orders.

If no matching orders are found, a clear message is returned instead of an empty response.

---

### Category-Based Sorting

A custom sorting endpoint was created to organize products:

- First by category (alphabetically)
- Then by price within each category (ascending)

This feature demonstrates multi-level sorting commonly used in admin dashboards and product listings.

---

### Combined Search, Sort, and Pagination

An advanced endpoint was built to combine all three functionalities into a single API call.

The system processes data in the following order:
1. Filter products using keyword (if provided)
2. Sort the filtered results
3. Apply pagination on the sorted data

All parameters are optional, making the endpoint flexible and powerful for real-world usage.

---

### Orders Pagination (Bonus)

Pagination was also implemented for the orders list to handle large datasets.

Users can:
- Navigate through pages of orders
- Control number of records per page
- View total pages and structured order data

This ensures scalability for growing order data.

---

## Conclusion

This assignment demonstrates how FastAPI can be used to implement advanced API features such as **searching, sorting, and pagination**, which are critical in modern web applications.

By combining multiple operations into efficient endpoints, the project simulates real-world API behavior used in e-commerce platforms and data-driven applications.

The assignment highlights the importance of clean API design, efficient data handling, and user-friendly responses in backend development.
