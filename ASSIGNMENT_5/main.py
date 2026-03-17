from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional,List
from fastapi import HTTPException

app=FastAPI()

# -------------------------------
# Day 01
# -------------------------------

# Products Database
products = [
{"id":1,"name":"Wireless Mouse","price":998,"category":"Electronics","in_stock":True},
{"id":2,"name":"Notebook","price":99,"category":"Stationery","in_stock":True},
{"id":3,"name":"USB Hub","price":799,"category":"Electronics","in_stock":False},
{"id":4,"name":"Pen Set","price":99,"category":"Stationery","in_stock":True}
]

# Home Endpoint
@app.get("/")
def home():
    return {"message":"Welcome to My E-commerce Store API"}

# Q1 — Show All Products
@app.get("/products")
def GetProducts():
    return {
        "products":products,
        "total":len(products)
    }

# Q2 — Filter Products by Category
@app.get("/products/category/{CategoryName}")
def GetProductsByCategory(CategoryName:str):

    FilteredProducts=[]

    for product in products:
        if product["category"].lower()==CategoryName.lower():
            FilteredProducts.append(product)

    if len(FilteredProducts)==0:
        return {"error":"No products found in this category"}

    return {
        "category":CategoryName,
        "products":FilteredProducts
    }

# Q3 — Show Only In-Stock Products
@app.get("/products/instock")
def GetInstockProducts():

    InStock=[]

    for product in products:
        if product["in_stock"]==True:
            InStock.append(product)

    return {
        "in_stock_products":InStock,
        "count":len(InStock)
    }

# Q4 — Store Summary
@app.get("/store/summary")
def StoreSummary():

    TotalProducts=len(products)
    InStock=0
    OutOfStock=0
    categories=[]

    for product in products:

        if product["in_stock"]:
            InStock+=1
        else:
            OutOfStock+=1

        if product["category"] not in categories:
            categories.append(product["category"])

    return {
        "store_name":"My E-commerce Store",
        "total_products":TotalProducts,
        "in_stock":InStock,
        "out_of_stock":OutOfStock,
        "categories":categories
    }

@app.get("/products/search")
def SearchProducts(keyword:str):

    matches=[]

    for product in products:
        if keyword.lower() in product["name"].lower():
            matches.append(product)

    if len(matches)==0:
        return {
            "message":f"No products found for: {keyword}",
            "results":[]
        }

    return{
        "keyword":keyword,
        "TotalFound":len(matches),
        "results":matches
    }

# BONUS — Cheapest & Most Expensive Product
@app.get("/products/deals")
def ProductDeals():

    cheapest=min(products,key=lambda x:x["price"])
    expensive=max(products,key=lambda x:x["price"])

    return {
        "best_deal":cheapest,
        "premium_pick":expensive
    }

# -------------------------------
# Day 02
# -------------------------------

# Q1 — Filter Products by Minimum Price
@app.get("/products/filter")
def FilterProducts(min_price:int=0,max_price:int=100000,category:str=None):

    FilteredProducts=[]

    for product in products:
        if product["price"]>=min_price and product["price"]<=max_price:

            if category:

                if product["category"].lower()==category.lower():
                    FilteredProducts.append(product)

            else:
                FilteredProducts.append(product)

    return {
        "filtered_products":FilteredProducts,
        "count":len(FilteredProducts)
    }

# Q2 — Get Product Price by ID
@app.get("/products/{product_id}/price")
def GetProductPrice(product_id:int):

    for product in products:

        if product["id"]==product_id:

            return {
                "name":product["name"],
                "price":product["price"]
            }

    return {"error":"Product not found"}

# Q3 — Customer Feedback System
feedback=[]

class CustomerFeedback(BaseModel):

    CustomerName:str=Field(...,min_length=2)
    product_id:int=Field(...,gt=0)
    rating:int=Field(...,ge=1,le=5)
    comment:Optional[str]=Field(None,max_length=300)

@app.post("/feedback")
def AddFeedback(data:CustomerFeedback):

    feedback.append(data)

    return {
        "message":"Feedback submitted successfully",
        "feedback":data,
        "total_feedback":len(feedback)
    }

# Q4 — Product Summary Dashboard
@app.get("/products/summary")
def ProductSummary():

    TotalProducts=len(products)
    InStockCount=0
    OutOfStockCount=0
    categories=[]

    for product in products:

        if product["in_stock"]:
            InStockCount+=1
        else:
            OutOfStockCount+=1

        if product["category"] not in categories:
            categories.append(product["category"])

    cheapest=min(products,key=lambda x:x["price"])
    MostExpensive=max(products,key=lambda x:x["price"])

    return {
        "total_products":TotalProducts,
        "in_stock_count":InStockCount,
        "out_of_stock_count":OutOfStockCount,
        "most_expensive":{
            "name":MostExpensive["name"],
            "price":MostExpensive["price"]
        },
        "cheapest":{
            "name":cheapest["name"],
            "price":cheapest["price"]
        },
        "categories":categories
    }

# Q5 — Bulk Order Processing

class OrderItem(BaseModel):

    product_id:int=Field(...,gt=0)
    quantity:int=Field(...,ge=1,le=50)

class BulkOrder(BaseModel):

    company_name:str=Field(...,min_length=2)
    contact_email:str=Field(...,min_length=5)
    items:List[OrderItem]

@app.post("/orders/bulk")
def BulkOrders(order:BulkOrder):

    confirmed=[]
    failed=[]
    grand_total=0

    for item in order.items:

        product=None

        for p in products:
            if p["id"]==item.product_id:
                product=p
                break

        if not product:
            failed.append({
                "product_id":item.product_id,
                "reason":"Product not found"
            })
            continue

        if not product["in_stock"]:
            failed.append({
                "product_id":item.product_id,
                "reason":product["name"]+" is out of stock"
            })
            continue

        subtotal=product["price"]*item.quantity
        grand_total+=subtotal

        confirmed.append({
            "product":product["name"],
            "qty":item.quantity,
            "subtotal":subtotal
        })

    return {
        "company":order.company_name,
        "confirmed":confirmed,
        "failed":failed,
        "grand_total":grand_total
    }

# BONUS — Simple Order Tracking
orders=[]

class SimpleOrder(BaseModel):

    product_id:int
    quantity:int

@app.post("/orders")
def CreateOrder(order:SimpleOrder):

    OrderData={
        "id":len(orders)+1,
        "product_id":order.product_id,
        "quantity":order.quantity,
        "status":"pending"
    }

    orders.append(OrderData)

    return OrderData


@app.patch("/orders/{order_id}/confirm")
def ConfirmOrder(order_id:int):

    for order in orders:

        if order["id"]==order_id:

            order["status"]="confirmed"
            return order

    return {"error":"Order not found"}

# -------------------------------
# Day 03
# -------------------------------

# Q1 - Add New Product Using POST
class ProductCreate(BaseModel):

    name:str=Field(...,min_length=2)
    price:int=Field(...,gt=0)
    category:str
    in_stock:bool


@app.post("/products",status_code=201)
def AddProduct(product:ProductCreate):

    for p in products:
        if p["name"].lower()==product.name.lower():
            raise HTTPException(status_code=400,detail="Product already exists")

    NewProduct={
        "id":len(products)+1,
        "name":product.name,
        "price":product.price,
        "category":product.category,
        "in_stock":product.in_stock
    }

    products.append(NewProduct)

    return {
        "message":"Product added",
        "product":NewProduct
    }


# Q5 — Inventory Audit (Must be above /products/{product_id})
@app.get("/products/audit")
def ProductsAudit():

    TotalProducts=len(products)
    InStockCount=0
    OutOfStockNames=[]
    TotalStockValue=0

    for product in products:

        if product["in_stock"]:
            InStockCount+=1
            TotalStockValue+=product["price"]*10
        else:
            OutOfStockNames.append(product["name"])

    MostExpensive=max(products,key=lambda x:x["price"])

    return{
        "total_products":TotalProducts,
        "in_stock_count":InStockCount,
        "out_of_stock_names":OutOfStockNames,
        "total_stock_value":TotalStockValue,
        "most_expensive":{
            "name":MostExpensive["name"],
            "price":MostExpensive["price"]
        }
    }


# ⭐ BONUS — Category Discount
@app.put("/products/discount")
def CategoryDiscount(category:str,discount_percent:int):

    UpdatedProducts=[]

    for product in products:

        if product["category"].lower()==category.lower():

            NewPrice=int(product["price"]*(1-discount_percent/100))
            product["price"]=NewPrice

            UpdatedProducts.append({
                "name":product["name"],
                "new_price":NewPrice
            })

    if len(UpdatedProducts)==0:
        return {"message":"No products found in this category"}

    return{
        "updated_products":len(UpdatedProducts),
        "products":UpdatedProducts
    }


# Q2 — Update Product (PUT)
@app.put("/products/{product_id}")
def UpdateProduct(product_id:int, price:int=None, in_stock:bool=None):

    for product in products:

        if int(product["id"]) == int(product_id):

            if price is not None:
                product["price"] = price

            if in_stock is not None:
                product["in_stock"] = in_stock

            return {
                "message": "Product updated",
                "product": product
            }

    raise HTTPException(status_code=404, detail="Product not found")

# Q3 — Delete Product
@app.delete("/products/{product_id}")
def DeleteProduct(product_id:int):

    for product in products:

        if product["id"]==product_id:

            products.remove(product)

            return {
                "message":f"Product '{product['name']}' deleted"
            }

    raise HTTPException(status_code=404,detail="Not found")



# -------------------------------
# Day 04
# -------------------------------

cart=[]
orders_list=[]


# Helper Function
def CalculateSubtotal(product,quantity):
    return product["price"]*quantity


# Q1 — Add Item to Cart
@app.post("/cart/add")
def AddToCart(product_id:int,quantity:int=1):

    Product=None

    for p in products:
        if p["id"]==product_id:
            Product=p
            break

    if Product is None:
        raise HTTPException(status_code=404,detail="Product not found")

    if Product["in_stock"]==False:
        raise HTTPException(status_code=400,detail=f"{Product['name']} is out of stock")


    # Check if product already in cart
    for item in cart:
        if item["product_id"]==product_id:

            item["quantity"]+=quantity
            item["subtotal"]=CalculateSubtotal(Product,item["quantity"])

            return{
                "message":"Cart updated",
                "cart_item":item
            }


    Subtotal=CalculateSubtotal(Product,quantity)

    CartItem={
        "product_id":Product["id"],
        "product_name":Product["name"],
        "quantity":quantity,
        "unit_price":Product["price"],
        "subtotal":Subtotal
    }

    cart.append(CartItem)

    return{
        "message":"Added to cart",
        "cart_item":CartItem
    }


# Q2 — View Cart
@app.get("/cart")
def GetCart():

    if len(cart)==0:
        return {"message":"Cart is empty"}

    GrandTotal=0

    for item in cart:
        GrandTotal+=item["subtotal"]

    return{
        "items":cart,
        "item_count":len(cart),
        "grand_total":GrandTotal
    }


# Q3 — Remove Item From Cart
@app.delete("/cart/{product_id}")
def RemoveFromCart(product_id:int):

    for item in cart:
        if item["product_id"]==product_id:

            cart.remove(item)

            return{
                "message":f"{item['product_name']} removed from cart"
            }

    raise HTTPException(status_code=404,detail="Item not found in cart")


# Checkout Model
class CheckoutData(BaseModel):
    CustomerName:str=Field(...,min_length=2)
    delivery_address:str=Field(...,min_length=10)


# Q4 — Checkout
@app.post("/cart/checkout")
def Checkout(data:CheckoutData):

    if len(cart)==0:
        raise HTTPException(status_code=400,detail="Cart is empty — add items first")

    OrdersPlaced=[]
    GrandTotal=0

    OrderID=len(orders_list)+1

    for item in cart:

        OrderData={
            "order_id":OrderID,
            "CustomerName":data.CustomerName,
            "product":item["product_name"],
            "quantity":item["quantity"],
            "total_price":item["subtotal"],
            "delivery_address":data.delivery_address
        }

        orders_list.append(OrderData)
        OrdersPlaced.append(OrderData)

        GrandTotal+=item["subtotal"]
        OrderID+=1


    cart.clear()

    return{
        "message":"Checkout successful",
        "orders_placed":OrdersPlaced,
        "grand_total":GrandTotal
    }


# Q5 — View All Orders
@app.get("/orders")
def GetOrders():

    return{
        "orders":orders_list,
        "total_orders":len(orders_list)
    }

# -------------------------------
# Day 05
# -------------------------------

# Q1 — SEARCH (ALREADY DONE ABOVE ✔)

# Q2 — SORT PRODUCTS
@app.get("/products/sort")
def SortProducts(sort_by:str="price",order:str="asc"):

    if sort_by not in ["price","name"]:
        return {"error":"sort_by must be 'price' or 'name'"}
    reverse=True if order=="desc" else False

    SortedList=sorted(products,key=lambda x:x[sort_by],reverse=reverse)

    return {
        "sort_by":sort_by,
        "order":order,
        "products":SortedList
    }

# Q3 — PAGINATION
@app.get("/products/page")
def PaginateProducts(page:int=1,limit:int=2):
    start=(page-1)*limit
    end=start+limit

    total=len(products)
    TotalPages=(total+limit-1)//limit

    return {
    "page":page,
    "limit":limit,
    "total_pages":TotalPages,
    "products":products[start:end]
    }

# Q4 — SEARCH ORDERS (orders_list)
@app.get("/orders/search")
def SearchOrders(customer_name:str):

    matches=[]

    for order in orders_list:
        if customer_name.lower() in order["CustomerName"].lower():
            matches.append(order)

    if len(matches)==0:
        return {"message":f"No orders found for: {customer_name}"}

    return {
        "customer_name":customer_name,
        "total_found":len(matches),
        "orders":matches
    }

# Q5 — SORT BY CATEGORY THEN PRICE
@app.get("/products/sort-by-category")
def SortByCategory():

    SortedProducts=sorted(products, key=lambda x: (x["category"], x["price"]))

    return {
        "message":"Sorted by category then price",
        "products":SortedProducts
    }

# Q6 — COMBINED BROWSE
@app.get("/products/browse")
def BrowseProducts(
    keyword:str=None,
    sort_by:str="price",
    order:str="asc",
    page:int=1,
    limit:int=4
):

    result=products

    # FILTER
    if keyword:
        temp=[]
        for p in result:
            if keyword.lower() in p["name"].lower():
                temp.append(p)
        result=temp

    # SORT
    if sort_by not in ["price","name"]:
        return {"error":"sort_by must be 'price' or 'name'"}

    reverse=True if order=="desc" else False
    result=sorted(result,key=lambda x:x[sort_by],reverse=reverse)

    # PAGINATION
    start=(page-1)*limit
    end=start+limit

    TotalFound=len(result)
    TotalPages=(TotalFound+limit-1)//limit

    return {
        "keyword":keyword,
        "sort_by":sort_by,
        "order":order,
        "page":page,
        "limit":limit,
        "total_found":TotalFound,
        "total_pages":TotalPages,
        "products":result[start:end]
    }

# ⭐ BONUS — PAGINATE ORDERS
@app.get("/orders/page")
def PaginateOrders(page: int=1,limit:int=3):

    start=(page-1)*limit
    end=start+limit

    total=len(orders_list)
    TotalPages=(total+limit-1)//limit

    return {
    "page":page,
    "limit":limit,
    "total_pages":TotalPages,
    "orders":orders_list[start:end]
    }

# Q4 — Get Product by ID
@app.get("/products/{product_id}")
def GetProduct(product_id:int):

    for product in products:

        if product["id"]==product_id:
            return product

    return {"error":"Product not found"}

@app.get("/orders/{order_id}")
def GetOrder(order_id:int):

    for order in orders:

        if order["id"]==order_id:
            return order

    return {"error":"Order not found"}