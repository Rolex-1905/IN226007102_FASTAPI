from fastapi import FastAPI

app=FastAPI()

# Products Database
products=[
{"id":1,"name":"Wireless Mouse","price":599,"category":"Electronics","in_stock":True},
{"id":2,"name":"Notebook","price":49,"category":"Stationery","in_stock":True},
{"id":3,"name":"Pen Set","price":99,"category":"Stationery","in_stock":False},
{"id":4,"name":"USB Cable","price":199,"category":"Electronics","in_stock":True},
{"id":5,"name":"Laptop Stand","price":899,"category":"Electronics","in_stock":True},
{"id":6,"name":"Mechanical Keyboard","price":2499,"category":"Electronics","in_stock":True},
{"id":7,"name":"Webcam","price":1299,"category":"Electronics","in_stock":False}
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


# Q5 — Search Products by Name
@app.get("/products/search/{keyword}")
def SearchProducts(keyword:str):

    matches=[]

    for product in products:
        if keyword.lower() in product["name"].lower():
            matches.append(product)

    if len(matches)==0:
        return {"message":"No products matched your search"}

    return {
        "matched_products":matches,
        "count":len(matches)
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