import urllib, urllib2, re, json, requests


def main():
    url = 'https://api.github.com/repos/dionyziz/ting/issues'
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    respData = resp.read()
    jsonData = json.loads(respData)
    alreadyIssue = []

    for elem in jsonData:
        title = elem['title']
        alreadyIssue.append(title)
    
    url = 'https://trello.com/1/Boards/XZf55h1s?cards=visible'
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    respData = resp.read()
    jsonData = json.loads(respData)
    
    url = 'https://api.github.com/repos/dionyziz/ting/issues'
    
    session = requests.session()
    session.auth = ("username", "pass")

    for card in jsonData['cards']:
        name = card['name'] 
        
        if name in alreadyIssue:
            continue
        
        payload = {'title': name}
        req = session.post(url, json.dumps(payload))
        
        if req.status_code == 201:
            print "Succesfully created issue\n"
        else:
            print "Couldn't create issue"
            print "Response:", req.content
        
   
if __name__ == "__main__":
    main()
