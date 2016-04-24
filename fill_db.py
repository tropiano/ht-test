import logging
import datetime
import random
import pandas as pd
from app import db
import sys
from app.models import Team, Midfield, Attack, Defence

log = logging.getLogger(__name__)

db.create_all()

reload(sys)
sys.setdefaultencoding('utf8')

try:
    teams_data = pd.read_csv("static/test_teams.csv")
    for index, row in teams_data.iterrows():
        team = Team()
        team.team_id   = int(row["team_id"])
        team.team_name = row["team_name"].decode('utf-8')
        team.series_id = int(row["series_id"])
        db.session.add(team)
        db.session.commit()
except Exception as e:
        log.error("Update ViewMenu error: {0}".format(str(e)))
        db.session.rollback()

try:
    teams_data = pd.read_csv("static/test_midfield.csv")
    for index, row in teams_data.iterrows():
        midfield = Midfield()
        midfield.team_id   = int(row["team_id"])
        midfield.midfield_rating = int(row["midfield_rating"])
        midfield.match_id = int(row["match_id"])
        db.session.add(midfield)
        db.session.commit()
except Exception as e:
        log.error("Update ViewMenu error: {0}".format(str(e)))
        db.session.rollback()

try:
    teams_data = pd.read_csv("static/test_attack.csv")
    for index, row in teams_data.iterrows():
        attack = Attack()
        attack.team_id   = int(row["team_id"])
        attack.attack_rating = row["att_rating"]
        attack.match_id = int(row["match_id"])
        db.session.add(attack)
        db.session.commit()
except Exception as e:
        log.error("Update ViewMenu error: {0}".format(str(e)))
        db.session.rollback()

try:
    teams_data = pd.read_csv("static/test_defence.csv")
    for index, row in teams_data.iterrows():
        defence = Defence()
        defence.team_id   = int(row["team_id"])
        defence.defence_rating = row["def_rating"]
        defence.match_id = int(row["match_id"])
        db.session.add(defence)
        db.session.commit()
except Exception as e:
        log.error("Update ViewMenu error: {0}".format(str(e)))
        db.session.rollback()
