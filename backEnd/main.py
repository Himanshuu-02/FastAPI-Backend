from fastapi import Depends,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modals import Product
from database import session,engine
import database_models as database_models
from sqlalchemy.orm import Session
from time import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
   # allow_origins=["http://localhost:3000"],  # React / Next.js
   # allow_credentials=True,
   allow_origins=["*"],
   allow_credentials=False,
    allow_methods=["*"],  # GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],
)
@app.middleware("http")
async def add_process_time_header(request, call_next):
      start = time()
      response = await call_next(request)
      process_time = time() - start
      response.headers["X-Process-Time"] = str(process_time)
      return response
#database_models.Base.metadata.create_all(bind= engine)
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


#crate this function for get the data from database in our swagger
def get_db():
      db=session()       #start the connection 
      try:
            yield db
      finally: 
            db.close() # close the connection 


# def init_db():       #by this function we can add our data in the used database like postgreql 
#       db= session()
#       count= db.query(database_models.Product).count
#       if(count==0):
#             for product in products:
#                   db.add(database_models.Product(**product.model_dump()))
#             db.commit()
# init_db()

@app.get("/products")
def get_all_products(db:Session= Depends(get_db)):
               #now change this function because now we want data from database (postgresql not from the list by inject the dependency)
      db_products= db.query(database_models.Product).all()      
      return db_products

    
       # db-connection
      
       #db_query
     

@app.get("/products/{id}")
# def get_all_productby_id(id:int):      #this code mainly use for get the data by id and this give that which stay in the list form in our code now we create the same function where we get the data from database
#       for product in products:
#             if(product.id==id):
#                   return product              
#       return "Product not found"

#write function to get the data by id and get the data from the original database postgresql

def get_all_productby_id(id:int, db:Session=Depends(get_db)):
      db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
      if db_product:
            return db_product
      return "Product not found"


# #write a post commant to create/add a product from the given list
@app.post("/products")
# def add_new_product(product:Product):
#       products.append(product)
#       return product

#write post/add data command for add a new product that is also shown in our postgreql database and also fetch the data from there
def add_new_product(product:Product,db:Session=Depends(get_db)):
       db.add(database_models.Product(**product.model_dump()))
       db.commit()
       return product


      
#write a put command for update a product in the give data in list 
@app.put("/products/{id}")
# def update_product_data(id:int,product:Product):
#       for i in range(len(products)):
#             if(products[i].id==id):
#                   products[i]=product
#                   return "product update successfully"
#       return "that product doesnot exist"

#this will update the data api when we update data it will automatically update data in our database (postgresql) and data also comes from there
def update_product_data(id:int,product:Product, db:Session=Depends(get_db)):
       db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
       if db_product:
             db_product.name=product.name
             db_product.description=product.description
             db_product.price=product.price
             db_product.quantity=product.quantity
             db.commit()
             return "product updated"
       else:
             return"Product not found"
      
            

#write command to delete a product in the already written database which is written in the list form not in the database connected
@app.delete("/products/{id}")
# def delete_product(id:int):
#       for i in range(len(products)):
#              if(products[i].id==id):
#                    del products[i]
#                    return "product delete succesfully"
#       return "product not found"

#this command is mainly use for deleted the data in our table but it will direct deleted the data in the database (postgresql) not in the list form data

def delete_product(id:int, db:Session=Depends(get_db)):
      db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
      if db_product:
            db.delete(db_product)
            db.commit()
            return "product deleted"
      else:
            return"product not found"

                   
           

     
            
      


            

      



      