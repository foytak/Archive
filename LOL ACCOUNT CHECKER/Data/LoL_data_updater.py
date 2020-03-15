import os
import sys
import urllib
import urllib2
import json

legendarySkins = {
    92016:  'Dawnbringer Riven',
    157009: 'Nightbringer Yasuo',
    51011:  'Pulsefire Caitlyn',
    64011:  'God Fist Lee Sin',
    222004: 'Star Guardian Jinx',
    22008:  'PROJECT: Ashe',
    412005: 'Dark Star Tresh',
    14005:  'Mecha Zero Sion',
    18010:  'Dragon Trainer Tristana',
    11009:  'PROJECT: Yi',
    17008:  'Omega Squad Teemo',
    72003:  'Battlecast Alpha Skarner',
    122004: 'Dunkmaster Darius',
    45008:  'Final Boss Veigar',
    119003: 'Primetime Draven',
    68003:  'Super Galaxy Rumble',
    75005:  'Infernal Nasus',
    40005:  'Forecast Janna',
    34005:  'Blackfrost Anivia',
    10006:  'Aether Wing Kayle',
    56005:  'Eternum Nocturne',
    31005:  "Battlecast Prime Cho'Gath",
    3004:   'Gatekeeper Galio',
    9006:   'Surprise Party Fiddlesticks',
    23004:  'Demonblade Tryndamere',
    20004:  'Nunu Bot',
    2003:   'Brolaf',
    31002:  "Gentleman Cho'Gath"
}

ultimateSkins = {
    99007: 'Elementalist Lux',
    37006: 'DJ Sona',
    77003: 'Spirit Guard Udyr',
    81005: 'Pulsefire Ezreal'
}

ultraRareSkins = {
    33001: 'King Rammus',
    12001: 'Black Alistar',
    10001: 'Silver Kayle',
    59004: 'Victorious Jarvan',
    92004: 'Championship Riven',
    4001:  'PAX Twisted Fate',
    24004: 'PAX Jax',
    15005: 'PAX Sivir',
    27001: 'Riot Squad Singed',
    42001: 'UFO Corki',
    53001: 'Rusty Blitzcrank',
    13004: 'Triumphant Ryze',
    13001: 'Young Ryze',
    19001: 'Grey Warwick',
    19002: 'URF Warwick',
    27001: 'RIOT Singed',
    10005: 'Judgment Kayle'
}

api_version_url = 'https://ddragon.leagueoflegends.com/api/versions.json'
realm_version_url = 'https://ddragon.leagueoflegends.com/realms/na.json'
cdn_url = 'http://ddragon.leagueoflegends.com/cdn/'

def loadJsonFromUrl(url):
	r = urllib2.urlopen(url)
	str_r = r.read().decode('utf-8')
	return json.loads(str_r)

print 'Latest API Version: ' + loadJsonFromUrl(api_version_url)[0]

obj = loadJsonFromUrl(realm_version_url)

champs_vers = obj['n']['champion']
runes_vers = obj['n']['rune']

champs_url = '%s%s/data/en_US/championFull.json' % (cdn_url, champs_vers)
runes_url = '%s%s/data/en_US/rune.json' %(cdn_url, runes_vers)

print '\nRealm: NA'

print 'Champions: ' + champs_vers
print 'Runes: ' + runes_vers

print '\nDownload? y/n'
if raw_input() != 'y':
    sys.exit()

obj = loadJsonFromUrl(champs_url)

output = []

for ck, champion in sorted(obj['data'].items()):
    skins = []

    for skin in champion['skins']:
        skinId = int(skin['id'])
        skins.append({
            'Id': skinId,
            'Name': skin['name'],
            'Num': skin['num'],
            'ChampionId': int(champion['key']),
            'IsLegendary': skinId in legendarySkins.keys(),
            'IsUltimate': skinId in ultimateSkins.keys(),
            'IsUltraRare': skinId in ultraRareSkins.keys()
        })

    output.append({
        'Id': int(champion['key']),
        'Name': champion['id'],
        'DisplayName': champion['name'],
        'Skins': skins
    })

    print(champion['name'])


with open('Champions.json', 'w') as f:
	json.dump(output, f)

with open('Champions.Version', 'w') as f:
	f.write(champs_vers)

def getRuneType(str_type):
	type = {
		'red':		1,
		'yellow':	2,
		'blue':		3,
		'black':	4
	}
	return type[str_type] if str_type in type else 0


obj = loadJsonFromUrl(runes_url)

output = []

for rune_id in obj['data']:
	rune = {
		'Id':			int(rune_id),
		'Name':			obj['data'][rune_id]['name'],
		'Description':	obj['data'][rune_id]['description'],
		'Tier': 		int(obj['data'][rune_id]['rune']['tier']),
		'Type':			getRuneType(obj['data'][rune_id]['rune']['type'])
	}
	output.append(rune)
	
	print rune['Name']

with open('Runes.json', 'w') as f:
	json.dump(output, f)

with open('Runes.Version', 'w') as f:
	f.write(runes_vers)

print 'Press Enter to continue...' 
raw_input()
