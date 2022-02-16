import typing
import strawberry
from urllib.request import urlopen
import json
from cache import Cache

domain = "http://universities.hipolabs.com/search?"

cacheUniversity = Cache(10)
cacheCountries = Cache(10)

@strawberry.type
class University:
    name: str
    country: str
    alpha_two_code: typing.Optional[str]
    web_pages: typing.Optional[typing.List[str]]
    domains: typing.Optional[typing.List[str]]
    def __init__(self,name,country):
        self.name = name
        self.country = country
    @strawberry.field
    def keywords(self)->str:
        return f"{self.country}&{self.name}"
        
    def fromDict(d: dict):
        u = University(d['name'],d['country'])
        u.alpha_two_code = d['alpha_two_code']
        u.web_pages = d['web_pages']
        u.domains = d['domains']
        return u
  

async def getUniversity(root: University)->typing.List[University]:
    data = cacheUniversity.getData(root.keywords())
    if data == []:
        url = domain
        url += f"country={root.country}&name={root.name}"
        response = urlopen(url.replace(" ", "%20"))
        data = json.loads(response.read())
        if data != []:
            newData = []
            for d in data:
                newData.append(University.fromDict(d))
            data = newData
            cacheUniversity.insert(root.keywords(),data)       
    return data
async def getCountries():
    data = cacheCountries.getData('')
    if data == []:
        url = domain + "country="
        response = urlopen(url)
        data = json.loads(response.read())
        if data != []:
            newdata = set()
            for d in data:
                newdata.add(d['country'])
            data = list(newdata)
            cacheCountries.insert('',data)
            
    return data
@strawberry.type
class Query:
    @strawberry.field
    def university(self, name:str="",country:str="")->typing.List[University]:
        return getUniversity(University(name=name,country=country))


