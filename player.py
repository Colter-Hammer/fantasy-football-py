import requests
import json

class FBPlayer:

  def __init__(self, player=None):
    self.player = player

    self.first = ''
    self.full_name = ''
    self.projected = 0
    self.injured_status = ''
    self.is_injured   = ''
    self.default_position = ''
    self.current_slot = ''
    self.eligible_slots = []

    if player is not None:

      # FOR TESTING
      self.player_keys = self.player['playerPoolEntry']['player'].keys()
      # FOR TESTING END

      self.first = self.player['playerPoolEntry']['player']['firstName']
      self.full_name = self.player['playerPoolEntry']['player']['fullName']
      self.initProjected()
      self.initInjuredStatus()
      self.is_injured   = self.player['playerPoolEntry']['player']['injured']
      self.default_position = self.player['playerPoolEntry']['player']['defaultPositionId']
      self.current_slot = self.player['lineupSlotId']
      self.eligible_slots = self.player['playerPoolEntry']['player']['eligibleSlots']      
    

  @property
  def fullName(self):
    return self.player['playerPoolEntry']['player']['fullName']

  @staticmethod
  def newDummyFBPlayer(projected=0):
    player = FBPlayer()
    player.projected = projected
    
    return player
    
  # This needs to be in a try/except to account for the 'D/SP' Position, which will not have an injured_status
  def initInjuredStatus(self):
    self.injured_status = 'N/A'
    try:
      self.injured_status = self.player['playerPoolEntry']['player']['injuryStatus']
    except:
      pass

  def initProjected(self):
    for stat in self.player['playerPoolEntry']['player']['stats']:
      if stat['statSourceId'] == 1 and stat['statSplitTypeId'] == 2:
        self.projected = round(stat['appliedAverage'], 1)
        break

  def displayProjected(self):
    print(f'{self.fullName} - {self.projected} Points')

  def injuredStatus(self):
    print(f'{self.is_injured} {self.injured_status}')
