# Name:
# Date: 6/28/21
# Description: Creates product, customer, and store- objects then allows them to interact with each other. Products can
# be added to the store's inventory and purchased by customers or searched by id number

class Product:
    """Creates products that can be added to the store and purchased by customers"""
    def __init__(self, id_code, title, description, price, quantity_available):
        self._id_code = id_code
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_id_code(self):
        return self._id_code

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_price(self):
        return self._price

    def get_quantity_available(self):
        return self._quantity_available

    def decrease_quantity_available(self):
        """when product is moved from store to customer, the inventory of the store is reduced by 1"""
        self._quantity_available -= 1



class Customer:
    """customer objects that can buy products from the store as long as they are members of the store"""
    def __init__(self, name, customer_id, is_premium_member):
        self._name = name
        self._customer_id = customer_id
        self._is_premium_member = is_premium_member
        self._customer_cart = []

    def get_customer_cart(self):
        return self._customer_cart

    def get_name(self):
        return self._name

    def get_customer_id(self):
        return self._customer_id

    def is_premium_member(self):
        return self._is_premium_member

    def add_product_to_cart(self.id_code):

    def empty_cart(self):
        """empties the customer's cart"""
        return self._customer_cart = []

class Store:
    """SUPPOSED to be able to search products/ members by their ID numbers add products to the customers cart and check out"""
    #inventory "": "": """""""""" we want to use dictionaries
    #stores members can be a list

    def __init__(self, products, members):
        self._products = []
        self.members = []

    def add_product(self, Product):
        """"""
        self._products += self._id_code

    def add_member(self, Customer):
        """"""
        self._members += self._customer_id

    def product_search():



class InvalidCheckoutError(Exception):
    pass

# p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
# c1 = Customer("Yinsheng", "QWF", False)
# myStore = Store()
# myStore.add_product(p1)
# myStore.add_member(c1)
# myStore.add_product_to_member_cart("889", "QWF")
# result = myStore.check_out_member("QWF")

if __name__ == '__main__':
    main()

# I feel lost and I don't think that the modules cover all that is expected of us