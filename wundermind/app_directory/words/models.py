from mongoengine import *

'''
Creating user collection
Fields to be filled in by facebook
'''

class User(Document):
    first_name = StringField(required=True)
    last_name = StringField(required = True)
    email = StringField(required=True)
    gender = StringField(required=True)
    dob = StringField(required=True)
    access_token = StringField(required=True)

    

class Words(Document):
    wm_word = StringField(max_length=150, required=True)
    person = ReferenceField(User, reverse_delete_rule=CASCADE)










