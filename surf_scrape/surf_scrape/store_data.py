import numpy as np
import pickle
import os

class StoreData():

    # meta file stores the entire graph of websites in dict() form, along with their metadata (keys are website names)
    # schema file stores key-value pairs of matrices to website names
    # matrix file stores numpy matrix for pagerank

    data_dir = '../../../data'
    meta_file = 'meta.json'
    schema_file = 'schema.json'
    matrix_file = 'matrix.json'

    # original data from web crawler
    crawl_data = None
    
    # "cleaned" meta dict 
    cleaned_dict = None

    meta_path = os.path.join(data_dir, meta_file)
    schema_path = os.path.join(data_dir, schema_file)
    matrix_path = os.path.join(data_dir, matrix_file)

    def __init__(self, crawl_data):

        self.crawl_data = crawl_data
        for key in crawl_data.keys():

            #skip small in_link and out_link counts

            if(len(crawl_data[key]['in_links']) < 2 and len(crawl_data[key]['out_links']) < 2):
                continue

            print("url: " + key)
            print("in-links: ")
            print([in_link for in_link in crawl_data[key]['in_links']])
            print("out-links: ")
            print([out_link for out_link in crawl_data[key]['out_links']])
            print()
            


    
    # store cleaned meta data in meta_file
    def store_meta(self):
        return None

    
    # make mapping of website indices in matrix to website names from meta
    def generate_schema(self):
        return None

    # store schema in json 
    def store_scheme(self):
        return None

    # generate numpy matrix of websites from pagerank
    def generate_matrix(self):
        return None


    # store matrix in csv form
    def store_matrix(self):
        return None

    # trigger store_finished request handler on flask server
    def send_store_req(self):
        return None
