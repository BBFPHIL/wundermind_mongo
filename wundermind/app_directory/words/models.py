from mongoengine import *


connect('words')


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



Phil = User(first_name = 'Phillip', last_name='Walker', email='pwalker@fordham.edu', gender='M', access_token='eufh234jh4fjh3843ufhi4n3irfri3')
Phil.save()


Wordphil = Words(wm_word="Angry", person = Phil)
Wordphil.save()


for info in User.objects:
    print info.first_name
    print info.last_name
    print info.email
    print info.gender
    print info.access_token









