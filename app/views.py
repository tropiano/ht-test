from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder.charts.views import DirectByChartView, GroupByChartView
from flask.ext.appbuilder import ModelView
from models import Team, Midfield, Defence, Attack
from app import appbuilder, db, fill_db
from flask.ext.appbuilder.models.group import aggregate_count, aggregate_sum, aggregate_avg
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction, FilterEqual, FilterSmaller
#from flask import g 
"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""


class MidfieldListSerieA(ModelView):
    datamodel = SQLAInterface(Midfield)
    list_columns = ['team.team_name', 'team.series_name','midfield_rating', 'match_id']
    base_filters = [['team.series_name', FilterStartsWith, 'S']]

class MidfieldListII(ModelView):
    datamodel = SQLAInterface(Midfield)
    list_columns = ['team.team_name', 'team.series_name','midfield_rating', 'match_id']
    base_filters = [['team.series_name', FilterStartsWith, 'II.']]	

class MidfieldListIII(ModelView):
    datamodel = SQLAInterface(Midfield)
    list_columns = ['team.team_name', 'team.series_name','midfield_rating', 'match_id']
    base_filters = [['team.series_name', FilterStartsWith, 'III.']]
	
class DefenceModelView(ModelView):
    datamodel = SQLAInterface(Defence)
    list_columns = ['team.team_name', 'defence_rating', 'match_id']

class AttackModelView(ModelView):
    datamodel = SQLAInterface(Attack)
    list_columns = ['team.team_name', 'attack_rating', 'match_id']

class TeamsModelView(ModelView):
    datamodel = SQLAInterface(Team)
    list_columns = ['team_id', 'team_name', 'series_id']
    related_views = [MidfieldListSerieA]

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404


class MidfieldChartView(DirectByChartView):
    datamodel = SQLAInterface(Midfield)
    chart_title = 'Midfield Example'
    chart_type = 'Histogram'
    #base_filters = [['team.team_name', FilterStartsWith, 'A']]

    
    definitions = [
        {
            'label': 'Midfield',
            'group': 'team.team_name',
            'series': [(aggregate_avg,'midfield_rating')]
            },
        {
            'label': 'League',
            'group': 'team.series_name',
            'series': [(aggregate_sum,'midfield_rating')]
            }
        ]
    
appbuilder.add_view(TeamsModelView, "List Teams", icon="fa-folder-open-o", category="Statistics")
appbuilder.add_view(MidfieldListSerieA, "List Teams Midfield Serie A", icon="fa-folder-open-o", category="Midfield Stats")
appbuilder.add_view(MidfieldListII, "List Teams Midfield II", icon="fa-folder-open-o", category="Midfield Stats")
appbuilder.add_view(MidfieldListIII, "List Teams Midfield III", icon="fa-folder-open-o", category="Midfield Stats")
#appbuilder.add_view(MidfieldListSerieA, "List Teams Midfield", icon="fa-folder-open-o", category="Midfield Stats")

appbuilder.add_view(DefenceModelView, "List Teams Defence", icon="fa-folder-open-o", category="Defence Stats")
appbuilder.add_view(AttackModelView, "List Teams Attack", icon="fa-folder-open-o", category="Attack Stats")
appbuilder.add_view(MidfieldChartView, "Show Midfield Chart", icon="fa-dashboard", category="Midfield Stats")


