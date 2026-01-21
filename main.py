from fastapi import FastAPI
from modals import Product

app = FastAPI()
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
        return products

@app.get("/product/{id}")
def get_all_productby_id(id:int):
      for product in products:
            if(product.id==id):
                  return product              
      return "Product not found"

      