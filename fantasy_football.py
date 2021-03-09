import requests
import json
from player import FBPlayer
from league import League
from enums import Slots

class FantastyFootball:

  def __init__(self, swid, espn_s2):
    self.sesh = requests.Session()
    self.sesh.cookies['swid']    = swid
    self.sesh.cookies['espn_s2'] = espn_s2

  def loadWeek(self, week):
    response = self.sesh.get(week)
    self.data = json.loads(response.text)
    self.players = [ FBPlayer(player_data) for player_data in self.data['teams'][0]['roster']['entries'] ]

  def getLeague(self, league):
    response = self.sesh.get(league)
    self.league = League(json.loads(response.text))
    
    print(self.league.allowed_positions)

  def findWeaklings(self, threshold = 0):
    weaklings = []
    
    for player in self.players:
      if player.projected < threshold or player.injured_status not in ['ACTIVE', 'N/A']:
        weaklings.append(player)
    return weaklings

  def findStrongestByPosition(self, slot = Slots.QB.value):

    possible = [player for player in self.players if slot in player.eligible_slots]
    strongest = FBPlayer.newDummyFBPlayer(projected = -1000)

    # Find the highest projected score among those players
    for player in possible:
      if (player.projected > strongest.projected):
        strongest = player

    print(strongest.full_name, strongest.projected)

    
    return possible