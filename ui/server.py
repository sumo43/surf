from flask import Flask, render_template



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
