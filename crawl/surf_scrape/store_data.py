import numpy as np
import pickle
import os
import json

class StoreData():

    # meta file stores the entire graph of websites in dict() form, along with their metadata (keys are website names)
    # schema file stores key-value pairs of matrices to website names
    # matrix file stores numpy matrix for pagerank

    data_dir = '../../data'
    meta_file = 'meta.json'
    schema_file = 'schema.json'
    matrix_file = 'matrix.json'

    # data from crawler, can "clean" or modify this later 
    new_entries = dict()
    
    # "cleaned" meta dict 
    # we will add our new websites to this dict
    meta_dict = None

    meta_path = os.path.join(data_dir, meta_file)
    schema_path = os.path.join(data_dir, schema_file)
    matrix_path = os.path.join(data_dir, matrix_file)


    # store_data uses local storage for now, but will use a json-like backend
    # like firebase later
    # data is stored in 

    def __init__(self, crawl_data):
        
        for key in crawl_data.keys():
            if(len(crawl_data[key]['in_links']) < 2 and len(crawl_data[key]['out_links']) < 2):
                continue
            else:
                self.new_entries[key] = crawl_data[key]
        
        self.store_meta()
    
    # store cleaned meta data in meta_file
    def store_meta(self):
        with open(self.meta_path, 'r') as meta_file:

            try:
                self.meta_dict = json.load(meta_file)
            except Exception as e:
                self.meta_dict = dict()


        for key in self.new_entries.keys():
            if key in self.meta_dict:
                # add in_links for key
                for in_link in self.new_entries[key]['in_links']:
                    if in_link not in self.meta_dict[key]['in_links']:
                        self.meta_dict[key]['in_links'].append(in_link)

                # add out_links for key
                for out_link in self.new_entries[key]['out_links']:
                    if out_link not in self.meta_dict[key]['out_links']:
                        self.meta_dict[key]['out_links'].append(out_link)

            else:
                self.meta_dict[key] = dict()
                self.meta_dict[key]['in_links'] = self.new_entries[key]['in_links']
                self.meta_dict[key]['out_links'] = self.new_entries[key]['out_links']

            #skip small in_link and out_link counts
    
        with open(self.meta_path, 'w') as out_meta_file:
            json.dump(self.meta_dict, out_meta_file)
    
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
