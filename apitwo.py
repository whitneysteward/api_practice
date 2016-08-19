# These code snippets use an open-source library. http://unirest.io/python
import requests
#response = requests.get("https://yoda.p.mashape.com/yoda?sentence=You+will+learn+how+to+speak+like+me+someday.++Oh+wait.",
 # headers={
    #"X-Mashape-Key": "e6XdAi9bYMmshvoKhj1ZCGZULyolp1QM3JqjsnlbxDZ4o2SO7A",
#    "Accept": "text/plain"
 # }
#)
#print(response.text)
#yoda
#sentence = input("Enter a sentence you would like to convert! ")
#cmd = "https://yoda.p.mashape.com/yoda?sentence=" + sentence
#response = requests.get(cmd,
  #headers={
    #"X-Mashape-Key": "e6XdAi9bYMmshvoKhj1ZCGZULyolp1QM3JqjsnlbxDZ4o2SO7A",
    #"Accept": "text/plain"
  #}
#)
#print(response.text)


# These code snippets use an open-source library. http://unirest.io/python
# sentence = input("Enter a sentence you would like to convert!")
# cmd = "https://loudelement-free-natural-language-processing-service.p.mashape.com/nlp-text/?text=" + sentence
# response = requests.get(cmd,
# headers={
#     "X-Mashape-Key": "e6XdAi9bYMmshvoKhj1ZCGZULyolp1QM3JqjsnlbxDZ4o2SO7A",
#     "Accept": "application/json"
#   }
# )
# print(response.text)

response = requests.get("https://mashape-community-urban-dictionary.p.mashape.com/define?term=wat",
  headers={
    "X-Mashape-Key": "e6XdAi9bYMmshvoKhj1ZCGZULyolp1QM3JqjsnlbxDZ4o2SO7A",
    "Accept": "text/plain"
  }
)
