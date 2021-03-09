from enum import Enum

class Slots(Enum):
  QB    = 0 # Quarterback
  TQB   = 1 # Team Quaterback
  RB    = 2 # Runningback
  RBWR  = 3 # flex?
  WR    = 4 # Receiver
  WRTE  = 5 # Receiver/Tight end
  TE    = 6 # Tight end
  OP    = 7 # Offensive Player Utility
  DT    = 8 # Defensive Tackle
  DE    = 9 # Defensive End
  LB    = 10 # Linebacker
  DL    = 11 # Defensive Line? 
  CB    = 12 # Corner back
  S     = 13 # Safety
  DB    = 14 # Defensive Back
  DP    = 15 # Defensive Player Utility
  DST   = 16 # Defense/Special Teams
  K     = 17 # Kicker
  P     = 18 # Punter
  HC    = 19 # Head coach
  BENCH = 20 # Bench
  IR    = 21 # Injured Reserve
  FLEX  = 23 # FLEX?


class Positions(Enum):
  TQB = 0
  QB = 1
  RB = 2
  WR = 3
  TE = 4
  K = 5
  a = 6
  b = 7
  c = 8
  d = 9
  e = 10
  f = 11
  g = 12
  h = 13
  i = 14
  j = 15
  DST = 16
  k = 17