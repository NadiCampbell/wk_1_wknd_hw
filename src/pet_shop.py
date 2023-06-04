# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    # returning the name of the pet shop
    return pet_shop["name"]

def get_total_cash(pet_shop):
    # returning the total cash by accessing admin then total cash stored within
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, num, type):
    if type == 'add':
        # add num to total cost
        new_total_cost = pet_shop["admin"]["total_cash"] + int(num)
        # re-assign new_total_cost to total_cash
        updated_total = pet_shop["admin"]["total_cash"] = new_total_cost
        # return new total_cash 
        return updated_total 
    
    elif type == 'subtract':
         new_total_cost = pet_shop["admin"]["total_cash"] - int(num)
         updated_total = pet_shop["admin"]["total_cash"] = new_total_cost
         return updated_total


def get_pets_sold(pet_shop):
    # returning number of pets sold 
    return pet_shop["admin"]["pets_sold"]



def increase_pets_sold(pet_shop, num):  
    # adding num to pets sold
    new_pets_sold = pet_shop["admin"]["pets_sold"] + int(num) 
    # reassigning value of pets sold 
    updated_pets_sold = pet_shop["admin"]["pets_sold"] = new_pets_sold
    # returning new value 
    return updated_pets_sold


def get_stock_count(pet_shop):
    # returning length of the list 
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    breeds = []
    #loop through pets list
    for pet_breed in pet_shop['pets']:
        # check if current item in loop matches the breed in the parameter
        if pet_breed["breed"] == breed:
            # append current item in loop to list if it matches breed
            breeds.append(pet_breed)
    return(breeds)
        
            
def find_pet_by_name(pet_shop, name):
#    loop through pets list 
   for pet in pet_shop["pets"]:
    #    if name matches the name in parameter
       if pet["name"] == name:
        #    return pet
           return pet 
       

def remove_pet_by_name(pet_shop, name):
    # loop through pets list whilst gaining access to the current item and the items index position 
    for index, item in enumerate(pet_shop['pets']):
        # if item name equals name given in parameter 
        if item['name'] == name:
            # remove item from list via items index position 
            pet_shop["pets"].pop(index)


def add_pet_to_stock(pet_shop, new_pet):
    # add new pet to pets list 
    pet_shop['pets'].append(new_pet)


def get_customer_cash(customer):
    # get customers cash value
    return customer["cash"]


def remove_customer_cash(customer, num):
    # create sum for updating cash total
    new_total = customer["cash"] - int(num) 
    # reassign new total using sum 
    updated_cash = customer["cash"] = new_total 
    # return updated total
    return updated_cash


def get_customer_pet_count(customer):
    # return amount of items within the customer pets list 
    return len(customer["pets"])



def add_pet_to_customer(customer, new_pet):
    # add new pet to existing pets list 
    customer["pets"].append(new_pet)


def customer_can_afford_pet(customer, new_pet):
#   if customer cash is greater than or equal to price of new pet, return value of True or False 
  return bool(customer["cash"] >= new_pet["price"])


