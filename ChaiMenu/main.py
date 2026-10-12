from fastapi import FastAPI,Query,HTTPException #Query helps to handle the query parameters auto matically 
#HttpsExceptions helps standardize all the error in fastapi
from models import MenuResponse,MenuItem
from data import menu_items

app = FastAPI(
    title="Chai Point Menu API",
    description="Read only menu API for kiosk displays and mobile app"
)


@app.get("/")
def root():
    return {"message" : "Welcome to chai point menu api"}


# /menu -> path
# /menu?category=char  -> query

@app.get("/menu", response_model=MenuResponse)
def get_menu(category : str | None = Query(None , description="Filter by chai ,snacks, coolers etc")):
    if category:
        filtered = [item for item in menu_items if item["category"] == category.lower()]
        if not filtered:
            raise HTTPException(status_code=404,detail = f"No item found in category : {category}")
        return MenuResponse(count  = len(filtered) , items=filtered)

    return MenuResponse(count = len(menu_items), items = menu_items)        

@app.get("/menu/{item_id}" , response_model=MenuItem)
def get_item_by_id(item_id:int):
    for item in menu_items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404 , detail=f"No item with item_id : {item_id} found in the menu")

