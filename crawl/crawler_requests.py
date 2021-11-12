import requests
from bs4 import BeautifulSoup as soup
from lxml import etree
from queue import Queue
from urllib.parse import urlparse
from crawl.store_data import StoreData

MAX_DEPTH = 2

class SurfCrawler:

    root_url = None
    urls = dict()
    MAX_DEPTH = 2
    
    def __init__(self):
        self.root_url = None

    # this is basically a BFS: We visit websites in the order in which they are added to queue
    # we stop visiting sites after they reach a certain depth

    def run(self, url):

        self.root_url = url            
        site_queue = Queue()
        site_queue.put(self.root_url)

        self.initialize_data(self.root_url, 0)
    
        visited = []
        link_count = 0
        
        print(f"initializing crawl from root: {self.root_url}")

        # add an http to the url just for requests

        while not site_queue.empty():

            link_count += 1

            if(link_count > 100):
                break
            
            curr_site = site_queue.get()
            curr_depth = self.urls[curr_site]['depth']

            visited.append(curr_site)

            req_url = 'https://' + curr_site

            try:
                req = requests.get(req_url)
            except Exception as e:
                continue
            req_tree = etree.HTML(req.content)

            if(req_tree == None):
                continue

            for a in req_tree.xpath('//a/@href'):

                if('https://' not in a):
                    continue

                parser = urlparse(a)
                neighbor = self.process(parser.netloc)

                if(neighbor not in self.urls.keys()):
                    self.initialize_data(neighbor, curr_depth + 1)
                    neighbor_depth = curr_depth + 1
                else:
                    neighbor_depth = self.urls[neighbor]['depth']

                if neighbor not in visited and neighbor_depth <= MAX_DEPTH:
                    site_queue.put(neighbor)
                
                self.add_child(curr_site, neighbor)
        
        print(f"crawl finished for root {self.root_url}")

        self.crawl_finished()

    def add_child(self, parent: str, child: str):
        if child not in self.urls[parent]['out_links'] and child != parent:
            self.urls[parent]['out_links'].append(child)
        if parent not in self.urls[child]['in_links'] and child != parent:
            self.urls[child]['in_links'].append(parent)

    def process(self, url : str):

        if('www' not in url):
            url = 'www.' + url

        return url

    def crawl_finished(self):
        # crawl is finished

        print("crawl is finished")
        StoreData(self.urls)

    def pprint_urls(self):
        for key in self.urls.keys():
            print("url: " + key + " depth: " + str(self.urls[key]['depth']))
            print("in_links: " + str(self.urls[key]['in_links']))
            print("out_links: " + str(self.urls[key]['out_links']))
            print()
            
    def initialize_data(self, dict_loc, depth=0):
        # initialize the data representation for each website/node
        # mainly doing this for depth (crawl to x depth)
        # for now, 'data' is just a list of the outbound links from a website
        self.urls[dict_loc] = dict()
        self.urls[dict_loc]['in_links'] = []
        self.urls[dict_loc]['out_links'] = []
        self.urls[dict_loc]['depth'] = depth

    def error_handler(self, err):
        print("there was an error...")
        print(err)

def run():
    print("ran")
