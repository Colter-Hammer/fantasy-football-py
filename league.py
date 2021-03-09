import requests
import json

class League:
  def __init__(self, league):
    self.settings = league['settings']
    self.roster_settings = self.settings['rosterSettings']
    self.allowed_positions = { k: v for k, v in self.roster_settings['lineupSlotCounts'].items() if v > 0 }
    