import requests

s=requests.get('http://127.0.0.1:5000/get',params=
        {'Arrival_date':'12-11-2021',
        'Arrival_time':'12:00',
        'date_dep':'12-11-2021',
        'time_dep':'12:00',
        'Source':'Delhi',
        'Destination':'Cochin',
        'stops':1,
        'Airline':'SpiceJet',
        'source':'Delhi',
        'destination':'Cochin',})
print(s.text)