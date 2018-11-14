from dash_package.seed import *

engine = create_engine('sqlite:///basketball.db')
Session = sessionmaker(bind = engine)
session = Session()


session.add_all(coach_instances)
session.add_all(team_instances)
session.commit()
