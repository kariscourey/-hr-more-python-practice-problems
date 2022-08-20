kyle = {'age': 33, 'taken_safety_class': True}

def customer_can_skydive(customer, consent_form=None): # means if you don't pass in consent_form, it defaults to None

    # if customer is over 17 or they have consent_form and have taken safety class
    if customer.get('age') > 17 or (consent_form != None and customer.get('taken_safety_class')):
        return True
    # else
    return False


print(customer_can_skydive(kyle,True))

k = None
print(id(k))
print(id(None))
