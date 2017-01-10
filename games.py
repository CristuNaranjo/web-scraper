from lxml import html
import requests
import render

base_url = 'http://www.basketball-reference.com'

def getGames(year):
    base_url_games = base_url + '/leagues/NBA_'+ str(year) + '_games'
    # months = ['-october.html', '-november.html','-december.html','-january.html','-february.html','-march.html','-april.html','-may.html','-june.html']
    months = ['-october.html']
    games = list()
    for ele in months:
        url = base_url_games+ele
        page = requests.get(url)
        tree = html.fromstring(page.content)
        #List games:
        games += tree.xpath('//*[@id="schedule"]/tbody/tr[*]/td[6]/a//@href')
    return games

def getData(game):
    base_url_data = base_url + game
    webRender = Render(base_url_data)
    result = r.frame.toHtml()
    



    print base_url_data
    headers= {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"}
    data_page = requests.get(base_url_data, headers = headers)
    data_tree = html.fromstring(data_page.content)
    team_visit = data_tree.xpath('//*[@id="line_score"]/tbody/tr[*]/td[1]/a//@href')
    team_local = data_tree.xpath('//*[@id="line_score"]/tbody/tr[3]/td[1]/a/text()')
    # teams = data_tree.xpath('//*[@id="line_score"]/tbody/tr[3]/td[1]/a//@href')
    # print teams
    print team_local
    print team_visit
    # #team_local.lower() --> minusculas
    # id_local_box = 'box_' + team_local.lower() + '_basic'
    # id_visit_box = 'box_' + team_visit.lower() + '_basic'

    data = data_tree.xpath('//*[@id="box_was_basic"]/tbody/tr[1]/td[*]')
    print data
    return data


    # return games
