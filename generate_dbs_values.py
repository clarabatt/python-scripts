import random

def choosingStatus(num):
    if num == 1: return "Ordered"
    elif num == 2: return "Prepared"
    elif num == 3: return "Concluded"
    else: return "Canceled" 

def choosingPaymentStatus(num):
    if num == 1: return "Pending"
    elif num == 2: return "Concluded"
    else: return "Canceled" 

def generatingOrders():
    list = []
    for i in range(22):
        luck = random.randint(0, 1)
        luckStatus = random.randint(1,4)
        newValue = {
            'id': random.randint(1, 99999), 
            'customerId': random.randint(1, 99999) if luck else 'NULL',
            'employeeId': random.randint(1, 99999),
            'storeId': random.randint(1, 99999),
            'date': "{dd}/{mm}/{yyyy}".format(dd=random.randint(1, 28), mm=random.randint(1, 12), yyyy=random.randint(2020, 2022)),
            'status': choosingStatus(luckStatus)
        }
        list.append(newValue)

    for i in list:
        print("INTO orders VALUES ({id}, {customerId}, {employeeId}, {storeId}, '{date}', '{status}')".format(
            id=i['id'],
            customerId=i['customerId'],
            employeeId=i['employeeId'],
            storeId=i['storeId'],
            date=i['date'],
            status=i['status'],
        ))

def generatingPayments():
    list = []
    for i in range(22):
        luck = random.randint(0, 1)
        luckStatus = random.randint(1,3)

        price = random.randint(500, 50000)
        taxes = (price/100)*13/100
        tip = (price/100)*20/100

        newValue = {
            'id': random.randint(1, 999999), 
            'taxes': taxes,
            'tip': tip,
            'subtotal': price/100,
            'total': price/100 + taxes + tip,
            'status': choosingPaymentStatus(luckStatus)
        }
        list.append(newValue)

    for i in list:
        print("INTO payments VALUES ({id}, {taxes}, {tip}, {subtotal}, {total}, '{status}')".format(
            id=i['id'],
            taxes=round(i['taxes'], 2),
            tip=round(i['tip'], 2),
            subtotal=round(i['subtotal'], 2),
            total=round(i['total'], 2),
            status=i['status'],
        ))

generatingOrders()