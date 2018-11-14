{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# from sqlalchemy.orm import sessionmaker\\n\",\n",
    "#     \"from sqlalchemy import create_engine\\n\",\n",
    "#     \"from bs4 import BeautifulSoup\\n\",\n",
    "#     \"import requests\\n\",\n",
    "#     \"from models import *\\n\",\n",
    "#     \"from scrape import *\"\n",
    "\n",
    "from sqlalchemy.orm import sessionmaker\n",
    "from sqlalchemy import create_engine\n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "from models import *\n",
    "from scrape import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# \"engine = create_engine('sqlite:///basketball.db')\\n\",\n",
    "#     \"Session = sessionmaker(bind = engine)\\n\",\n",
    "#     \"session = Session()\"\n",
    "\n",
    "enginer = create_engine('sqlite:///basketball.db')\n",
    "Session = sessionmaker(bind = engine)\n",
    "session = Session()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def Instantiate(year1,year2):\n",
    "    coachsite_objects = CoachSite()\n",
    "    lowered = list(map(lambda school : school.lower(),coachsite_objects.salaries[1]))\n",
    "    school_list = list(map(lambda school : school.replace(' ', '-'), lowered))\n",
    "    teamsite_objects = {}\n",
    "    for school in school_list:\n",
    "        teamsite_objects[school] = TeamSite(school,year1,year2)\n",
    "    return teamsite_objects, coachsite_objects"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "everything = (Instantiate(2017,2018))\n",
    "teamsite = everything[0] # gives you a dictionary with keys = school name and values\\n\",\n",
    "             # are TeamSite instances\\n\",\n",
    "keys = list((teamsite).keys())\n",
    "coachsite = everything[1] #gives you object instance\\n\",\n",
    "school_instances = []\n",
    "for key in keys:\n",
    "    years_ = teamsite[key].years\n",
    "    winloss_ = teamsite[key].winloss\n",
    "    team_points_ = teamsite[key].team_points\n",
    "    opp_points_ = teamsite[key].opp_points\n",
    "    for i in range(0,len(years_)):\n",
    "        team_instances = School(name = key, years = years_[i], winloss = winloss_[i],\\\n",
    "                            team_points = team_points_[i], opp_points = opp_points_[i])\n",
    "    session.add(team_instances)\n",
    "\n",
    "coach_instances = []\n",
    "for tup in coachsite.salaries[0]:\n",
    "    c_instances = Coach(name = tup[0] , years = tup[1] , salary = tup[2],\\\n",
    "                        sal_school = tup[3])\n",
    "    session.add(c_instances)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "session.commit()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
