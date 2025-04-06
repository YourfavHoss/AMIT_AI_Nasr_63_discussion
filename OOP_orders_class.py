

from OOP_class_auth import UserAuth
from OOP_products_class import Product , products_table

class Order:
  def __init__(self,Customer_name: UserAuth , product: Product ):
    self.Customer_name = Customer_name
    self.product = product
    

  def order_check(self,product_name: str) -> bool:
    for product in products_table:
      if product_name.lower() == product["Name"].lower() and product.get_quantity() <= product["Quantity"] :
        return True
  
    return False
  
from typing import List

class OrdersList:
  def __init__(self,ordersList: List[Order]):
    self.ordersList = []
     
  def appendOrder(self, order: Order):
    if order.order_check:
      OrdersList.append(order.product.name)
        
    