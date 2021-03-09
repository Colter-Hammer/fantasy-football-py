import requests
import json
from fantasy_football import FantastyFootball
from player import FBPlayer
from enums import Slots, Positions
from credentials import cookies, team_id, league_id

def main():
  # config
  league  = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/2020/segments/0/leagues/'
  league += league_id + '?rosterForTeamId=21&view=mDraftDetail&view=mLiveScoring&view=mMatchupScore&view=mPendingTransactions&view=mPositionalRatings&view=mRoster&view=mSettings&view=mTeam&view=modular&view=mNav'
  week    = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/2020/segments/0/leagues/'
  week += league_id + '?forTeamId=21&scoringPeriodId=17&view=mRoster'

  ffb = FantastyFootball(cookies['swid'], cookies['espn_s2'])
  ffb.loadWeek(week)
  # ffb.getLeague(league)

  # [print(player.full_name, player.player_keys) for player in ffb.players]
  ffb.findStrongestByPosition(Slots.FLEX.value)

  # for player in ffb.findWeaklings(45):
  #   player.displayProjected()

main()