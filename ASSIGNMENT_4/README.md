# FastAPI Assignment 4 – Internship Task

## Intern Details

**Name:** Neeraj  
**Intern ID:** IN226007102  
**Module:** FastAPI – Assignment 4  
**Organization:** Innomatics Research Labs  

---

## Project Description

This assignment focuses on implementing a complete **Shopping Cart System** using FastAPI.  
The objective of this task was to simulate a real-world e-commerce cart workflow by connecting multiple API endpoints that manage cart operations.

The system allows users to add products to a cart, view cart contents, update quantities, remove items, and complete the checkout process.  
The assignment demonstrates how multiple endpoints can work together to build a fully functional backend feature commonly used in online shopping platforms.

---

## Concepts Implemented

During this assignment the following FastAPI concepts were implemented:

- API endpoint integration to create a full shopping cart workflow.
- Query parameters for passing product ID and quantity values.
- Conditional logic to handle product availability and validation.
- Business logic for calculating subtotals and grand totals.
- Error handling using HTTP status codes such as **400 Bad Request** and **404 Not Found**.
- Data validation for checkout inputs such as customer name and delivery address.
- Order creation and tracking after successful checkout.

These concepts demonstrate how backend systems manage user actions and maintain application logic across multiple API routes.

---

## Features Implemented

### Add Items to Cart

A cart system endpoint was implemented to allow customers to add products to their shopping cart.  
When a product is added, the system calculates the subtotal based on the product price and quantity.  
If the same product is added again, the system updates the existing cart item instead of creating a duplicate entry.

### View Cart Contents

A dedicated endpoint was created to display all items currently in the cart.  
The response includes details such as product information, item quantities, subtotals, the number of unique items, and the overall grand total for the cart.

### Out-of-Stock and Invalid Product Handling

The API validates product availability before adding items to the cart.  
If a product is out of stock, the system returns an appropriate error response.  
Similarly, if an invalid product ID is requested, the API responds with a **404 Not Found** error to ensure data consistency.

### Cart Item Quantity Updates

When a product that already exists in the cart is added again, the system increases the quantity of that item rather than creating a duplicate record.  
This ensures the cart maintains a clean and organized structure while updating the subtotal and grand total accordingly.

### Remove Items from Cart

Customers are able to remove products from the cart using a delete endpoint.  
Once an item is removed, the cart automatically recalculates the total cost and updates the remaining cart contents.

### Checkout and Order Creation

The checkout process allows users to place an order using the items currently in their cart.  
During checkout, the API validates customer details and creates order records for each product in the cart.  
After successful checkout, the cart is cleared and the order details are stored in the order history.

### Multi-Customer Order Flow

The system supports sequential shopping sessions where multiple customers can perform cart operations and complete checkouts.  
Each successful checkout creates new order records that can later be retrieved through the orders endpoint.

### Empty Cart Checkout Handling (Bonus)

An additional validation rule was implemented to prevent users from checking out with an empty cart.  
If a checkout request is made when the cart contains no items, the API returns a **400 Bad Request** response instead of processing an invalid order.

---

## Conclusion

This assignment demonstrates how FastAPI can be used to build a **complete shopping cart backend system** by connecting multiple API endpoints into a single workflow.

By implementing features such as cart management, order processing, validation, and error handling, the project simulates a key component of real-world e-commerce platforms.

The assignment highlights how FastAPI enables developers to design clean, structured, and scalable APIs for complex backend operations such as managing shopping carts and processing customer orders.
