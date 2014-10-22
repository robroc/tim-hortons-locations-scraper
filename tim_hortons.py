import requests
from bs4 import BeautifulSoup
import unicodecsv
import time

# These are latitude-longitude pairs to send to the Tim Hortons API. 
# It will return stores withing a 5-km radius of those locations.
# Edit the list according to your needs.

centres = [[45.434599,-73.91681],[45.458686,-73.848832],[45.47554,-73.786347],[45.501534,-73.718369],[45.473133,-73.67923],[45.462057,-73.600953],[45.537137,-73.651764],[45.529922,-73.598206],[45.516452,-73.561127],[45.573678,-73.630478],[45.564064,-73.594773],[45.547717,-73.558381],[45.604911,-73.613999],[45.584731,-73.577607],[45.571274,-73.537095],[45.625563,-73.574173],[45.631326,-73.526108],[45.668765,-73.511002],[45.58377,-73.440964],[45.526555,-73.496583],[45.492871,-73.473237],[45.454833,-73.459504],[45.503941,-73.381913],[45.546755,-73.817933],[45.58329,-73.752701],[45.61884,-73.698456],[45.657728,-73.623612],[45.387842,-73.577607],[45.643328,-73.843338],[45.788115,-74.0047],[45.369514,-73.93683]]
start = 'http://www.timhortons.com/ca/en/php/getRestaurants.php?origlat='
mid = '&origlng='
end = '&units=km&rad=10&_=1414009182244'

f = open('timhortons.csv', 'wb')
data = unicodecsv.writer(f)
data.writerow(['storeid','address','city','lat','lng'])

for centre in centres:
    print "Fetching data for coordinates %s" %centres.index(centre)
    r = requests.get(start + str(centre[0]) + mid + str(centre[1]) + end)
    soup = BeautifulSoup(r.text)
    stores = soup.findAll("marker")
    for store in stores:
        # This will only write these five attributes of each store.
        data.writerow([store["storeid"], store["address2"], store["city"], store["lat"], store["lng"]])
    time.sleep(5)
f.close()