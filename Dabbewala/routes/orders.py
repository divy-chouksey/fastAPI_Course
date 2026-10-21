from fastapi import APIRouter, Depends,HTTPException,Query
from database import get_session
from models import Order , OrderCreate, OrderUpdate, StatusLog , OrderStatus
from sqlmodel import Session, select
from datetime import datetime,date


router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=Order)
def create_order(order: OrderCreate, session:Session=Depends(get_session)):
    db_order = Order(**order.model_dump())
    session.add(db_order)
    session.commit()
    session.refresh(db_order)
    return db_order

@router.get("/", response_model=list[Order])
def list_orders(
    status : OrderStatus | None = Query(default=None, description="Filter orders by status"),
    created_date:date | None = Query(default=None, description="Filter orders by creation date in YYYY-MM-DD format"),
    skip:int = Query(default=0, ge=0, description="Number of records to skip"),
    limit:int = Query(20, ge=1, le=100, description="Number of records to return"),
    session:Session = Depends(get_session)

):
    query=select(Order)
    if status:
        query = query.where(Order.status == status)
    if created_date:
        start = datetime.combine(created_date, datetime.min.time())
        end = datetime.combine(created_date, datetime.max.time())
        query = query.where(Order.created_at >= start , Order.created_at <= end)

    query = query.offset(skip).limit(limit)

    return session.exec(query).all()

@router.patch("/update_order/{customer_name}",response_model=Order,tags=["orders"])
def update_order_status(
    customer_name:str,
    session: Session = Depends(get_session),
    new_status:OrderStatus | None = None,
):
    if new_status is None:
        return {"Message":"Thanks For using our services"}
    query = select(Order).where(Order.customer_name == customer_name)
    order = session.exec(query).first()
    if not order:
        raise HTTPException(status_code=404,detail="Order Not Found")
    order.status = new_status
    order.updated_at = datetime.now()
    session.add(order)
    session.commit()
    session.refresh(order)
    return order


