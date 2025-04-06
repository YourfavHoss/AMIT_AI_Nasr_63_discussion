"""
                                        +------------------------+
                                        |  Start                 |
                                        +------------------------+
                                                  |
                                                  v
                                        +------------------------+
                                        |  Display Product Catalog|
                                        +------------------------+
                                                  |
                                                  v
                                        +------------------------+
                                        |  Customer Selects Product|
                                        +------------------------+
                                                  |
                                                  v
                                        +------------------------+
                                        |  Check Product Availability|
                                        +------------------------+
                                                  |
                                                  v
                                        +------------------------+
                                        |  Product Available?     |
                                        +------------------------+
                                              /       \
                                            Yes        No
                                            /           \
                                            v             v
                                        +---------------------+      +---------------------+
                                        | Customer Specifies  |      | Prompt Customer for |
                                        | Quantity            |      | Valid Product Name  |
                                        +---------------------+      +---------------------+
                                                |
                                                v
                                        +---------------------+
                                        | Check Stock Quantity|
                                        +---------------------+
                                                |
                                                v
                                        +---------------------+
                                        | Quantity Available? |
                                        +---------------------+
                                                /      \
                                              Yes       No
                                              /           \
                                            v             v
                                        +---------------------+      +---------------------+
                                        | Calculate Discount  |      | Prompt Customer for |
                                        | and Total Price     |      | New Quantity        |
                                        +---------------------+      +---------------------+
                                                |
                                                v
                                        +------------------------+
                                        | Display Discounted Price|
                                        +------------------------+
                                                |
                                                v
                                        +------------------------+
                                        | Ask for More Products?  |
                                        +------------------------+
                                              /       \
                                            Yes        No
                                            /           \
                                            v             v
                                        +----------------------+  +------------------------+
                                        | Repeat Product Flow   |  | Checkout Process      |
                                        +----------------------+  +------------------------+
                                                |                     |
                                                v                     v
                                        +------------------------+    +--------------------+
                                        | Add Delivery/Pick-Up   |    | Apply Delivery Fee |
                                        +------------------------+    | and Finalize Order |
                                                |                     +--------------------+
                                                v
                                        +-----------------------+
                                        | Complete Purchase     |
                                        +-----------------------+
                                                  |
                                                  v
                                              +----------+
                                              |   End    |
                                              +----------+

"""


from prettytable import PrettyTable

products_table = [

  {"Name" : "Water" , "Price" : 88.0 , "Quantity" : 1200}
, {"Name" : "Soda" , "Price" : 130.0 , "Quantity" : 1200}
, {"Name" : "Chips" , "Price" : 75.0 , "Quantity" : 1200}
, {"Name" : "Water" , "Price" : 45.0 , "Quantity" : 1200}

]

from OOP_class_auth import UserAuth


class Product:
  def __init__(self,name: str , price: int , quantity: int):
    self.name = name
    self.price = price
    self.quantity = quantity

  def get_quantity(self):
    for product in products_table:
      if product["Name"] == self.name:
        return product["Quantity"]
      
  def get_price(self):
    for product in products_table:
      if product["Name"] == self.price:
        return product["Price"]
  
  
