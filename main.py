from flask import Flask, request, render_template
from urllib.parse import urlparse
from crawl.crawler_requests import SurfCrawler
import zerorpc
import zmq
import atexit

def process_site(website : str):
    
    website = website.replace("https://", "")
    website = website.replace("http://", "")

    if(website[len(website) - 1] == '/'):
        website = website[:len(website) - 1]

    return website

class WebsiteHandler(object):

    def __init__(self):
        super(WebsiteHandler, self).__init__() 
        self.crawler = SurfCrawler()
        
    def websiteHandler(self, website : dict):
    
        # TODO make the website name into a dict with useful info

        processed_site = process_site(website['text'])

        print(f"Received new link: {processed_site}")
        self.crawler.run(processed_site)

app = Flask(__name__)

# pass the list of page, name, desc to the html 

@app.route('/')
def index():
    return render_template('index.html', name='Surf', _cache=_cache) 

@app.route('/urls', methods=["GET", "POST"])
def root_handler():

    global _cache
    global cache
    global spider

    url = request.args.get('url')

    parser = urlparse(url)

    #make a ec3, google cloud
    if('0.0.0.0' in url):
        return "bad url, skipping..."
     
    parsed_url = parser.scheme + "://" + parser.netloc

    print("the url is " + parsed_url)

    # this _cache is no good
    # make a better cache

    if parsed_url in _cache:
        _cache[parsed_url] += []
    else:
        _cache[parsed_url] = []

    spider.push_url(parsed_url)


    _cache = spider.get_cache()
    print(_cache)

    # cache.push_url(parsed_url)
    # receive root
    # add root to database, but keep it in memory
    # for each link in root links: 
        #add the link to the database, search its roots if within 3deg of sep

    return "url " + parsed_url + " has been received"

if __name__ == '__main__':
    try:
        website_server = zerorpc.Server(WebsiteHandler())
        website_server.bind("tcp://0.0.0.0:4001")
        website_server.run()
        def exit_handler():
            with open("file.txt", "w") as file:
                file.write("aaa")
        atexit.register(exit_handler)
    except zmq.error.ZMQError:
        print("Socket already in use, is the server already running?") 
