from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
class Team(Model):
    team_id = Column(Integer, primary_key=True)
    #team_id = Column(Integer)
    team_name =  Column(String(150), unique=True, nullable=False)
    series_id = Column(Integer)

    def __repr__(self):
        return self.team_name        

class Midfield(Model):
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer)
    midfield_rating = Column(Integer)
    team_id = Column(Integer, ForeignKey('team.team_id'), nullable=False)
    team = relationship("Team")

    def __repr__(self):
        return self.team_id

class Defence(Model):
    id = Column(Integer, primary_key=True)
    defence_rating = Column(Integer)
    match_id = Column(Integer)
    team_id = Column(Integer, ForeignKey('team.team_id'), nullable=False)
    team = relationship("Team")

    def __repr__(self):
        return self.team_id

class Attack(Model):
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer)
    attack_rating = Column(Integer)
    team_id = Column(Integer, ForeignKey('team.team_id'), nullable=False)
    team = relationship("Team")

    def __repr__(self):
        return self.team_id
