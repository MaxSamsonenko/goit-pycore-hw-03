import random 

def  get_numbers_ticket(min, max, quantity):
    list = set() 
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []
    
    while len(list) < quantity:
        num = random.randint(min, max + 1)
        list.add(num)
    return sorted(list)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)