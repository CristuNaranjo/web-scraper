import games

try:
    year=int(raw_input('Insert Season Year:'))
except ValueError:
    print "Not a number"

gamesHref = games.getGames(year)
data = list()
data = games.getData(gamesHref[0])

# for game in gamesHref:
#     data = games.getData()
#
#
# print games
