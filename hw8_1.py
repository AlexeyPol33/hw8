import requests as rq

def get (url):

    req = rq.get(url=url)    
    return req.json()
    
def finde_heroes (finde_list, list_heroes):

    finded = []
    for i in finde_list:
        if i['name'] in list_heroes:
            finded.append(i)
    return finded

def best_hero (url, heroes, option = 'intelligence'):

    comparable_list = finde_heroes(finde_list=get(url),list_heroes=heroes)
    the_best = comparable_list[0]
    for i in comparable_list:
        if i['powerstats'][option] > the_best['powerstats'][option]:
            the_best = i
    return the_best['name']

if __name__ == '__main__':

    url = 'https://akabab.github.io/superhero-api/api/all.json'
    list_heroes = ['Hulk', 'Captain America', 'Thanos']
    print(best_hero(url=url,heroes=list_heroes))
    