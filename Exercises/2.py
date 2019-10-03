class Contact:

    all_contacts = []

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.note =  Contact.all_contacts.append(self)








 
class AddressHolder:
    def __init__(self,street,city,state,code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code




class Friend(Contact,AddressHolder):

    def __init__(self,name,email,phone,street,city,state,code):
        Contact.__init__(self,name,email)
        AddressHolder.__init__(self,street,city,state,code)
        self.phone = phone


   

c = Friend("Suraj","suraj.karki500@gmail.com",9807111049,"afd","afas","afas",12)

