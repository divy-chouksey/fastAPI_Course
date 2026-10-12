from fastapi import FastAPI
from fastapi import Request
import uvicorn

app = FastAPI(
    title="Swiggy Order Service",
    description=(
        "Internal API for managing orders. "
        "Handles creation and tracking of delivery systems."
    ),
    version="1.2.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    """Root endpoint - Health check"""
    #FastAPI converts this dict into JSON
    return { "message" : "Welcome to swiggy order service",
            "status" : "healthy"}

@app.get("/about")
def about():
    """Returns API metadata"""
    return {
        "Service" : "order-service",
        "team":"backend platform",
        "region":"ap-south-1",
        "version":"1.2.2"
    }

@app.get("/orders")
def list_orders():
    """List recent orders"""
    return {
        "orders" : [
            {"id":1,"item":"Butter Paneer","status":"delivered"},
            {"id":2,"item":"Masala Dosa","status":"preparing"},
            {"id":3,"item":"Butter Paneer","status":"delivered"},
            ]
    }

@app.get("/order/status")
def order_status():
    """Get order status"""
    return {
        "total_today" : 2_340_23,
        "top_city":"Bengaluru"
    }

@app.get("/debug/request-info")
async def request_info(request : Request):
    """Inspect the raw request object"""
    return {
        "method" : request.method,
        "url":str(request.url),
        "headers" : dict(request.headers),
        "path_params" : request.path_params,
        "query_params" : dict(request.query_params)
    }

@app.get(
    "/orders/active",
    summary="Get Active Orders",
    description=(
        "Return all orders that are currently being prepared"
        "Or are out for delivery"
    ),
    tags=["orders"],
    response_description="List of active order objects",
    deprecated=False
)
def get_active_order():
    """This docstring also appears in docs"""
    return {
        "active_orders" : [
            {"id":1,"item":"Masala Dosa","status":"Out_for_delivery"}
        ]
    }

@app.get("/restaurants" , tags = ["Restaurants"])
def list_restro():
    """Another docstring for another"""
    return{
        "restaurants" : [
            {"test":"test"}
        ]
    }
@app.get("/restaurants/delhi" , tags = ["Restaurants"])
def list_restro():
    """Another docstring for another"""
    return{
        "restaurants" : [
            {"test":"test"}
        ]
    }

