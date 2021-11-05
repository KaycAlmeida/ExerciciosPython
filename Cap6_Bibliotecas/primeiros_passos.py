from pygeocoder import Geocoder

endereco = '150, Rua Theodomiro Garcia, São Paulo, SP'

print(Geocoder('AIzaSyD7QQA79hNkqRbgLjGPuMPE567ZVKQnah0').geocode(endereco).coordinates)