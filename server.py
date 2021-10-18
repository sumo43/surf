#!/usr/bin/python3

import zerorpc

class WebsiteHandler(object):
    def printWesiteName(self, websiteName : str):
        print(websiteName)

    def websiteHandler(self, websiteName : str):
        # TODO make the website name into a dict with useful info


        return
    

    def dataHandler(self, data : dict):


website_server = zerorpc.Server(WebsiteHandler())
website_server.bind("tcp://0.0.0.0:4240")
website_server.run()
