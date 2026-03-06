# FastAPI Assignment 1 – Internship Task

## Intern Details

**Name:** Neeraj
**Intern ID:** IN226007102
**Module:** FastAPI – Assignment 1
**Organization:** Innomatics Research Labs

---

## Project Description

This project implements a simple **E-commerce Store API** using **FastAPI**.
The API allows users to retrieve products, filter them by category, search products, view store statistics, and get the best product deals.

All endpoints were tested using the FastAPI **Swagger UI**.

---

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Swagger UI

---

## API Endpoints Implemented

### Q1 – Add Products

Added three new products to the product list.

**Endpoint**

GET /products

**Output**

* Returns all products
* Displays total number of products in the store

---

### Q2 – Category Filter

Filter products by category.

**Endpoint**

GET /products/category/{category_name}

**Example**

* /products/category/Electronics
* /products/category/Stationery

If no products exist in the category, an error message is returned.

---

### Q3 – In-Stock Products

Show only products that are currently available.

**Endpoint**

GET /products/instock

**Output**

* Returns only products where `in_stock = True`
* Displays the count of available products

---

### Q4 – Store Summary

Provides an overview of the store.

**Endpoint**

GET /store/summary

**Output Includes**

* Total products
* In-stock products
* Out-of-stock products
* Available categories

---

### Q5 – Product Search

Search products by keyword (case-insensitive).

**Endpoint**

GET /products/search/{keyword}

**Examples**

* /products/search/mouse
* /products/search/book

Returns all matching products and total match count.

---

### Bonus Task – Product Deals

Shows the cheapest and most expensive products.

**Endpoint**

GET /products/deals

**Output**

* Best Deal (Lowest price product)
* Premium Pick (Highest price product)

---

## Testing

All endpoints were tested using:

Swagger UI
http://127.0.0.1:8000/docs

Screenshots of outputs are included in the **ASSIGNMENT 1** folder.

---

## Repository Structure

IN226007102_FASTAPI
└── ASSIGNMENT 1
    ├── main.py
    ├── Q1_Output.png
    ├── Q2_Output.png
    ├── Q3_Output.png
    ├── Q4_Output.png
    ├── Q5_Output_BOOK.png
    ├── Q5_Output_mouse.png
    ├── Bonus_Output.png
    └── Docs_Output.png

---

## Conclusion

This assignment demonstrates the implementation of REST API endpoints using FastAPI including filtering, searching, and summarizing product data.

All endpoints were successfully implemented and tested.
