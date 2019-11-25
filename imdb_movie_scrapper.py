from seleniumrequests import Firefox
from bs4 import BeautifulSoup as bs
import json
driver = Firefox()
movie_links = [] 
data = {}
data['movie'] = []
MAX_NO_FILMS = 250
imdb_url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
class Scarper:
    def __init__(self, url):
        self.url = url
        self.response = ''

    
    def load_url(self):
        self.response = driver.request('GET', self.url)
   
    def get_movie_links(self):
        raw_data = bs(self.response.text, 'lxml')
        list_of_movies = raw_data.find('tbody', {'class' : 'lister-list'})
        movies = list_of_movies.findAll('tr')
        for movie in movies:
            movie_details = movie.findAll('td')
            movie_links.append(movie_details[0].find('a')['href'])

    def get_movie_details(self):
        for i in range(0,250):
            print((i+1),'/',250,end='\r')
            movie_detail_response = driver.request('GET', 'https://www.imdb.com/'+movie_links[i])
            #parse the html response
            movie_details = bs(movie_detail_response.text, 'lxml')
            movie = {}
            #extract the title
            movie['title'] = movie_details.find('div', {'class' : 'title_wrapper'}).find('h1').text
            #extract the directors
            #movie_details_list = movie_details.find('div', {'class' : 'plot_summary'}).findAll('div', {'class' : 'credit_summary_item'})[2].find('a')[3]['href']
            #see_full_cast_url = movie_details.find('div', {'class' : 'titleCast'}).find('div', {'class' : 'see-more'}).find('a')['href']
            see_full_cast_url = movie_links[i].split('?')[0] + movie_details.find('div', {'class' : 'plot_summary'}).findAll('div', {'class' : 'credit_summary_item'})[2].findAll('a')[3]['href']
            see_full_cast_response = driver.request('GET', 'https://www.imdb.com/'+see_full_cast_url)
            see_full_cast_details = bs(see_full_cast_response.text, 'lxml')
            full_cast_details = see_full_cast_details.find('div', {'id' : 'fullcredits_content', 'class' : 'header'}).findAll('table', {'class' : 'simpleTable simpleCreditsTable'})

            director_list = full_cast_details[0].findAll('tr')
            movie['director'] = []
            for director in director_list:
                movie['director'].append(director.find('td', {'class' : 'name'}).find('a').text.strip())
            #extract the writers
            writer_list = full_cast_details[1].findAll('tr')
            movie['writer'] = []
            for writer in writer_list:
                if writer.find('td', {'class' : 'name'}) != None:
                    movie['writer'].append(writer.find('td', {'class' : 'name'}).find('a').text.strip())
            #extract the stars
            star_list = see_full_cast_details.find('div', {'id' : 'fullcredits_content'}).find('table', {'class' : 'cast_list'}).findAll('tr')
            movie['star'] = []
            '''
            for star in star_list:
                if not star.find('td')['class'].__contains__('castlist_label'):
                    movie['star'].append(star.findAll('td')[1].find('a').text.strip())
            '''
            for j in range(1, 4):
                movie['star'].append(star_list[j].findAll('td')[1].find('a').text.strip())
            #extract poster url
            movie['poster'] = movie_details.find('div', {'class' : 'poster'}).find('img')['src']
            #extrcat rating
            movie['rating'] = movie_details.find('span', {'itemprop' : 'ratingValue'}).text
            #extract release dates of each movie
            dates_url = movie_details.find('a', {'title' : 'See more release dates'})['href']
            dates_response = driver.request('GET', 'https://www.imdb.com/' + dates_url)
            dates_details = bs(dates_response.text, 'lxml')
            movie['date'] = {}
            dates_list = dates_details.findAll('tr', {'class': 'ipl-zebra-list__item release-date-item'})
            for date in dates_list:
                date_info = date.findAll('td')
                if(date_info[0].text.strip() not in movie['date'].keys()):
                    movie['date'][date_info[0].text.strip()] = date_info[1].text
            data['movie'].append(movie)

#Create scraper object and initialize with url
scraper = Scarper(imdb_url)
#send request to the giver url
scraper.load_url()
#get all links of each movie
scraper.get_movie_links()
#get details of each movie
scraper.get_movie_details()
with open('movies.json', 'w') as outfile:
    json.dump(data, outfile)
driver.close()
