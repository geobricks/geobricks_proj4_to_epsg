import requests
import json
from geobricks_proj4_to_epsg.core.proj4_to_epsg import get_proj4_json_from_string

# TODO: @Deprecated

# dirty methods to get epsg/proj4 codes
epsg_json = []
cached_epsg_codes = []

def create_epsg_json_file():
    with open("../data/epsg.json", "r") as f:
        projection_list = json.load(f)
        for p in projection_list:
            if p["epsg"] not in cached_epsg_codes:
                cached_epsg_codes.append(p["epsg"])
                print p["epsg"]
                proj4_text = get_proj4_from_spatialreference(p["epsg"])
                print proj4_text
                data = get_proj4_epsg_json(p["epsg"], proj4_text)
                if data is not None:
                    epsg_json.append(data)
    print "----"
    # print epsg_json
    write_json_file(epsg_json)


def get_proj4_from_spatialreference(epsg):
    r = requests.get("http://spatialreference.org/ref/epsg/"+ str(epsg) +"/proj4/")
    return r.text


def get_proj4_epsg_json(epsg, proj4_text):
    if "Not found" in proj4_text:
        return None
    return {
        "epsg": epsg,
        "proj4": get_proj4_json_from_string(proj4_text)
    }


def write_json_file(json_data):
    with open('../data/epsg.json', 'w') as outfile:
        print "wrinting file"
        print json_data
        json.dump(json_data, outfile)


# this method clean the json produced from create_epsg_json_file(). There are no valid data
# return from the web service
def _clean_epsg_json_data():
    epsg_json_data = []
    with open("epsg.json", "r") as f:
        projection_list = json.load(f)
        for p in projection_list:
            if p is not None and "proj" in p["proj4"]:
                epsg_json_data.append(p)
    write_json_file(epsg_json_data)


# spatialref doesn't have 3857 and 900913...
def _add_google_mercator_epsg_codes():
    epsg_json_data = []
    with open("../data/epsg_original.json", "r") as f:
        projection_list = json.load(f)
        projection_list.append({ 'epsg': '3857', 'proj4': get_proj4_json_from_string('+proj=merc +lon_0=0 +k=1 +x_0=0 +y_0=0 +a=6378137 +b=6378137 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')})
        projection_list.append({ 'epsg': '900913', 'proj4' : get_proj4_json_from_string('+proj=merc +lon_0=0 +k=1 +x_0=0 +y_0=0 +a=6378137 +b=6378137 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')})

    write_json_file(projection_list)


# methods to run
#create_epsg_json_file()
#_clean_epsg_json_data()
#_add_google_mercator_epsg_codes()
# print get_proj4_from_spatialreference(3857)