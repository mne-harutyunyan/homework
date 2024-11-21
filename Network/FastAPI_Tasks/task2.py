from fastapi import FastAPI, HTTPException
users:list = []
products:list = []

app = FastAPI()

def is_valid_email(email)->bool:
    if "@" not in email or email.count("@") != 1:
        return False
    left, right = email.split("@")

    if not left or not right:
        return False 
    
    if "." not in right or right.startswith(".") or right.endswith("."):
        return False  
    return True

def is_valid_name(name)->bool:
    if name == "" or "-" in name or "." in name:
        return False
    if name.isdigit() == True:
        return False
    if len(name) == 1 or len(name) > 30:
        return False
    return True

def is_valid_username(username)->bool:
    if username == "":
        return False
    if not username.isalnum():
        return False
    if len(username) < 5 or len(username) > 15:
        return False
    return True
    
def is_valid_price(price)->bool:
    if str(price).isdigit()!=True:
        return False
    if price < 0:
        return False
    
@app.get("/")
def welcome_get():
    """Get method to ensure that server is running... """

    return {"message":"Welcome to our server..."}

@app.get("/users")
def get_users():
    """Get method for viewing users list"""

    return {"Users":users}

@app.post("/users", status_code=201)
def create_user(user:dict):
    """Post method for creating a user"""
    name = user.get("name")
    email = user.get("email")
    username = user.get("username")
    if is_valid_name(name) == False:
        raise HTTPException(status_code=400, detail="Enter valid name...")
    if is_valid_email(email) == False:
        raise HTTPException(status_code=400, detail="Enter valid email...")
    if is_valid_username(username) == False:
        raise HTTPException(status_code=400, detail="Enter valid username...")
    if any(u["email"] == email for u in users):
        raise HTTPException(status_code=400, detail="Email already exists...")
    if any(u["username"] == username for u in users):
        raise HTTPException(status_code=400, detail="Username already exists...")
    if not name or not email or not username:
        raise HTTPException(status_code=400, detail="Both 'name', 'username' and 'email' are required...")
    
    max_id = max([u['id'] + 1 for u in users]) if users else 1

    new_user = {"id":max_id,"name":name,"email":email, "username":username}
    users.append(new_user)
    return {"message": "User created successfully", "user": new_user}

@app.get("/users/{user_id}", status_code=200)
def get_user(user_id: int):
    """Get method for viewing a user by ID"""

    for user in users:
        if user["id"] == user_id:
            return {"user": user}
    raise HTTPException(status_code=404, detail="User not found.")

@app.delete("/users", status_code=200)
def deleting_user(user: dict):
    """Delete method for deleting a user by username"""
    for u in users:
        if u['username'] == user['username']:
            users.remove(u) 
            return {"detail": "User deleted successfully."}
    raise HTTPException(status_code=404, detail= "User not found.")

@app.put("/users", status_code=200)
def update_user(user:dict):
    """Put method for updating a user email"""
    for u in users:
        if u['username'] == user['username']:
            u["email"] = user["email"]
            u["name"] = user['name']
            return {"detail": "User updated successfully."}
    raise HTTPException(status_code=404, detail= "User not found.")

@app.get("/products")
def get_products():
    """Get method for viewing product list.."""

    return {"Products":products}

@app.post("/products", status_code=201)
def create_product(product_details:dict):
    """Post method for creating a product"""

    name = product_details.get("name")
    price = product_details.get("price")
    productCode = product_details.get("productCode")
    if is_valid_name(name) == False:
        raise HTTPException(status_code=400, detail="Enter valid name...")
    if is_valid_price(price) == False:
        raise HTTPException(status_code=400, detail="Price must be positive number...")
    if str(productCode).isdigit() == False or productCode <= 0 or len(str(productCode)) <= 7:
        raise HTTPException(status_code=400, detail= "Enter a valid Product Code (e.g. 01234567)...")
    if any(p['productCode']== productCode for p in products):
        raise HTTPException(status_code=400, detail="Product code already exists...")
    if not name or not price or not productCode:
        raise HTTPException(status_code=400, detail="Both 'name','product code' and 'price' are required...")
    
    max_id = max([p['id'] + 1 for p in products]) if products else 1
    new_product = {"id":max_id,"name":name, "price":price, "productCode":productCode}

    products.append(new_product)
    return {"message": "product created successfully", "product": new_product}

@app.get("/products/{product_id}", status_code=200)
def get_product(product_id: int):
    """Get method for viewing a product by ID"""
    for product in products:
        if product["id"] == product_id:
            return {"product": product}
    raise HTTPException(status_code=404, detail="product not found.")

@app.delete("/products", status_code=200)
def deleting_product(product: dict):
    """Delete method for deleting a product by product code"""
    for p in products:
        if p['productCode'] == product['productCode']:
            products.remove(p) 
            return {"detail": "product deleted successfully."}
    raise HTTPException(status_code=404, detail= "Product not found.")

@app.put("/products", status_code=200)
def update_product(product:dict):
    """Put method for updating a product price"""
    for p in products:
        if p['productCode'] == product['productCode']:
            p["price"] = product["price"]
            return {"detail": "Product price updated successfully."}
    raise HTTPException(status_code=404, detail= "Product not found.")