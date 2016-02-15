import pytz
import datetime
import time
import urllib2
import json
import os
import xml.etree.ElementTree as ET
import cgi

# e.g. http://scores.nbcsports.msnbc.com/ticker/data/gamesMSNBC.js.asp?jsonp=true&sport=MLB&period=20120929
 
def today(league):
  url = 'http://scores.nbcsports.msnbc.com/ticker/data/gamesMSNBC.js.asp?jsonp=true&sport=%s&period=%d'
  yyyymmdd = int(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime("%Y%m%d"))
  games = []
  
  try:
    currentTime=time.strftime('%I:%M %p',time.localtime())
    currentDate=time.strftime('%m/%d/%Y',time.localtime())
    f = urllib2.urlopen(url % (league, yyyymmdd))
    jsonp = f.read()
    f.close()
    count = 0
    json_str = jsonp.replace('shsMSNBCTicker.loadGamesData(', '').replace(');', '')
    json_parsed = json.loads(json_str)
    for game_str in json_parsed.get('games', []):
      count += 1
      game_tree = ET.XML(game_str)
      visiting_tree = game_tree.find('visiting-team')
      home_tree = game_tree.find('home-team')
      gamestate_tree = game_tree.find('gamestate')
      home = home_tree.get('nickname')
      away = visiting_tree.get('nickname')
      visitingScore = visiting_tree.get('score')
      homeTeamScore = home_tree.get('score')
      os.environ['TZ'] = 'US/Eastern'
      start = int(time.mktime(time.strptime('%s %d' % (gamestate_tree.get('gametime'), yyyymmdd), '%I:%M %p %Y%m%d')))
      del os.environ['TZ']
      
      if visitingScore:
        pass
      else:
        visitingScore = '0'
        
      if homeTeamScore:
        pass
      else:
        homeTeamScore = '0'
        
      if count == 1:
        score = ET.Element('score')
        score.attrib['filedate'] = currentDate
        score.attrib['filetime'] = currentTime
        game = ET.SubElement(score, 'game')
        game.attrib['hometeam']= home
        game.attrib['awayteam']= away
        awayscore = ET.SubElement(game, 'awayscore')
        awayscore.text = visitingScore
        homescore = ET.SubElement(game, 'homescore')
        homescore.text = homeTeamScore
        gameTime = ET.SubElement(game, 'starttime')
        gameTime.text = gamestate_tree.get('status')
      else:  
        game = ET.Element('game')
        game.attrib['hometeam']= home
        game.attrib['awayteam']= away
        awayscore = ET.SubElement(game, 'awayscore')
        awayscore.text = visitingScore
        homescore = ET.SubElement(game, 'homescore')
        homescore.text = homeTeamScore
        gameTime = ET.SubElement(game, 'starttime')
        gameTime.text = gamestate_tree.get('status')
        score.append(game)
      gameXML = ET.tostring(score)
      print gameXML
      print count




      
##      games.append({
##        'league': league,
##        'start': start,
##        'home': home,
##        'away': away,
##        'home-score': home_tree.get('score'),
##        'away-score': visiting_tree.get('score'),
##        'status': gamestate_tree.get('status'),
##        'clock': gamestate_tree.get('display_status1'),
##        'clock-section': gamestate_tree.get('display_status2')
##      })
##    
    with open('scoreFile.xml','w') as scoreData:
      scoreData.write(str(gameXML))
  except Exception, e:
    print e
  
##  return games
 
if __name__ == "__main__":
##  for league in ['NFL', 'MLB', 'NBA', 'NHL']:
##    print today(league)
    today('MLB')
    time.sleep(10)
