def update_inventory(item_number,  total_amount) :
   print(item_number, 'plus', total_amount)
   if not isinstance(item_number, int) or item_number < 0:
       print('Error: item_number must be a positive number and not a float number')
       return None
   if total_amount + item_number > 1000:
       print('Error: total_amount must not exceed total capacity for inventory of 1000')
       return None
   
   total_amount += item_number 
   print(total_amount)
   
   return total_amount



update_inventory(11, 100)

update_inventory(15, 1000)

update_inventory(1.1, 100)
