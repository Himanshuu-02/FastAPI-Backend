from fastapi import FastAPI
from modals import Product
from database import session,engine
import database_models

app = FastAPI()
database_models.Base.metadata.create_all(bind= engine)
@app.get("/")

def greet():
    return "Hey this is my first project of fastapi"

products=[
      Product(id=1,name="laptop",description="budget phine",price=99.00,quantity=2),
      Product(id=2,name="macbook",description="high price",price=9.00,quantity=3),
      Product(id=3,name="watch",description="easy to afford",price=91.00,quantity=3),
      Product(id=4,name="apple",description="osm",price=4.00,quantity=4),
      Product(id=5,name="monitor",description="for big screen",price=39.00,quantity=3),
     ## Product(2,"phone"," phone",990.00,3)
]
@app.get("/products")
def get_all_products():
         db=session()
         db_query()
         return products

    
       # db-connection
      
       #db_query
     

@app.get("/product/{id}")
def get_all_productby_id(id:int):
      for product in products:
            if(product.id==id):
                  return product              
      return "Product not found"

#write a post commant to create/add a product
@app.post("/product")
def add_new_product(product:Product):
      products.append(product)
      return product

      
#write a put command for update a product 
@app.put("/product")
def update_product_data(id:int,product:Product):
      for i in range(len(products)):
            if(products[i].id==id):
                  products[i]=product
                  return "product update successfully"
      return "that product doesnot exist"

#write command to delete a product
@app.delete("/product")
def delete_product(id:int):
      for i in range(len(products)):
             if(products[i].id==id):
                   del products[i]
                   return "product delete succesfully"
      return "product not found"
                   
           

     
            
      


            

      



      