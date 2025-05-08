def NULL_not_found(object: any)->int:
    if object is None:
       print ("Nothing: None <class 'NoneType'>")
    elif object != object:
       print ("Cheese: nan <class 'float'>")
    elif object == 0 and object is not False:
       print ("Zero: 0 <class 'int'>")
    elif object == '':
       print ("Empty: <class 'str'>")
    elif object is False:
       print ("Fake: False <class 'bool'>")
    else:
        print("Type not Found")
        return 1

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))