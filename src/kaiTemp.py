#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : PI Integracion de sistemas IoT (Pilco - García)
# Created Date: 30/7/22
# version ='1.0'

from datetime import datetime, timezone
import sys
import requests
import time

#URL base de API Kaiterra y KEY del sensor
API_BASE_URL = "https://api.kaiterra.com/v1/"
API_KEY = "NGZkOTRlZGUzYWE1NGEzYzk2NWYyYTY0Zjk1NjdlNmYwODhh"

# Sesión al server
session = requests.session()

def do_get(relative_url, *, params={}, headers={}):
    import json

    params['key'] = API_KEY
    url = API_BASE_URL.strip("/") + relative_url
    
    response = session.get(url, params=params, headers=headers)
    
    content_str = ''
    if len(response.content) > 0:
        content_str = response.content.decode('utf-8')
        print()

    response.raise_for_status()
        
    if len(content_str) > 0:
        return json.loads(content_str)

    return None


def get_laser_egg(id: str):
    return do_get("/lasereggs/" + id)


def summarize_laser_egg(id: str):
    data = get_laser_egg(id)
    latest_data = data.get('info.aqi')
    
    if latest_data:
        ts = parse_rfc3339_utc(latest_data['ts'])
        ts_ago = (datetime.now(timezone.utc) - ts).total_seconds()
        
        temp = latest_data['data'].get('temp')
        if temp:
            print("  TEMPERATURA LST:   {} °C".format(temp))
            return temp
        else:
            print("  TEMPERATURA LST:   no data")

    else:
        print("Kaiterra no ha cargado datos aún")


def check_available(name):
    import importlib
    try:
        _ = importlib.import_module(name, None)
    except ImportError:
        print("Missing module '{}'.  Please run this command and try again:".format(name))
        print("   pip -r requirements.txt")
        sys.exit(1)


def parse_rfc3339_utc(ts: str) -> datetime:
    '''
    Parses and returns the timestamp as a timezone-aware time in the UTC time zone.
    '''
    return datetime.strptime(ts, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)


if __name__ == "__main__":
    check_available("requests")
    from datetime import datetime, timezone
    time.sleep(11) #tiempo en que se conecta el controlador AC
    while True:
        summarize_laser_egg("dd85475c-a5ef-4a15-b00f-206e408528b2") #obtiene valores del Kaiterra con el ID
        time.sleep(60)
