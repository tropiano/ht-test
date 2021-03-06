import logging
from datetime import datetime
import random
import pandas as pd
from app import db
import sys
from app.models import Team, Ratings

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
        team.series_name = row["series_name"]
        db.session.add(team)
        db.session.commit()
except Exception as e:
        log.error("Update ViewMenu error: {0}".format(str(e)))
        db.session.rollback()

try:
    teams_data = pd.read_csv("static/test_ratings.csv")
    for index, row in teams_data.iterrows():
        team = Ratings()
        team.team_id   = int(row["team_id"])
        team.match_date   = datetime.strptime(row["match_date"],'%Y-%m-%d %H:%M:%S').date()
        team.midfield_rating = int(row["midfield_rating"])
        team.defence_rating= int(row["defence_rating"])
        team.attack_rating = int(row["attack_rating"])
        db.session.add(team)
        db.session.commit()
except Exception as e:
    log.error("Update ViewMenu error: {0}".format(str(e)))
    db.session.rollback()
