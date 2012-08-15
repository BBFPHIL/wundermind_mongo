from mongoengine import *
from mongoengine.django.auth import User

'''
Creating user collection
Fields to be filled in by facebook
'''

class UserProfile(Document): 

    """
    class for the users to make their profiles of their skills in developing
    """

    user = ReferenceField(User)
    pos_type = BooleanField(EmbeddedDocument(PosType))
    gender = StringField(required=True)
    dob = StringField(required=True)
    lang_skills = ListField(EmbeddedDocumentField(LangSkill)) #Referencing LandSkill
    portfolio_link = StringField()
    profile_pic = FileField()
    interests = StringField()

class PosType(EmbeddedDocument):
    
    """
    Type of position that the Profile User is this will be used in search filtering
    """
    
    back_end = BooleanField()
    front_end = BooleanField()
    sys_admin = BooleanField()
    algo_Design = BooleanField()
    graphic_designer = BooleanField()

class LangSkill(EmbeddedDocument):
       
    """
    Language class to hold all the profile langauges
    """

    langs = StringField()


class Crew(Document):

    """
    Class to hold all the Crew Page's information
    """
    members = ListField(DynamicField(Member))
    crew_name = StringField(required=True)
    crew_picture = FileField()
    project_names = StringField()
    


class Member(DynamicDocument):
    
    """
    If a user is apart of crew, get the profile 
    """
    
    member_id = ListField(ReferenceField()
    member = ReferenceField(User)
        



    
    
