from fastapi import FastAPI
from enum import Enum
app=FastAPI()


@app.get("/")
async def root():
    return{"message":'hello world'}


@app.get("/testo")
async def get():
    return{"message": "i love u !"}

@app.get("/items/{item_id}")
async def get_item(item_id:str):

 return{ "your item_id:":item_id}
    

@app.get("user/me")
async def get_current_user():
   return{"message":'this is the current user'}

class FoodEnum(str,Enum):
   fruits='fruits'
   vegetables='vegetables'
   dairy='dairy'




@app.get("/foods/{food_name}")
async def FunctionName(food_name:FoodEnum):
   if food_name==FoodEnum.vegetables:
        return{"food_name":food_name,"message":"you are healty"}
   if food_name== FoodEnum.fruits:
        return{"food_name":food_name,"message":"you are a sweety  healty" }
   return{"food_name":food_name,'message':"unhealty"}
    
