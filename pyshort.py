class pyshort():
    __filename = ""
    __sites = []
    __random_size = 10

    class PyShortError(Exception):
        """ Base class for exceptions """
        pass

    class SiteConnectionError(PyShortError):
        """ Raised for error connecting to site"""
        pass

    class HtmlParsingError(PyShortError):
        """ Raised for error parsing with bs4 """
        pass

    def __random(self):
        """ Get a random ID exluding values existing in JSON file """
        size = 10
        charset = self.string.ascii_uppercase + self.string.digits
        existing = [x['short'] for x in self.__sites]
        while True:
            val = ''.join(self.random.choice(charset) for _ in range(self.__random_size))
            if val not in existing:
                break
        return val
    
    def __getsites(self):
        """ Populates __sites with a list of dict rapresenting the sites """
        try:
            self.__sites = tmp = self.json.loads(open(self.__filename).read())
        except:
            self.__sites = []

    def __savesites(self):
        """ Saves __sites to file """
        with self.io.open(self.__filename, 'w', encoding='utf-8') as f:
          f.write(unicode(self.json.dumps(self.__sites, ensure_ascii=False)))

    def __checkexists(self, astring):   
        """ Check if a site exists in the saved JSON object """
        tmp = [x['short'] for x in self.__sites if x['url']==astring]
        if not len(tmp):
            return ''
        else:
            return tmp[0]

    def __init__(self,archivename):
        
        self.datetime = __import__('datetime')
        self.bs4 = __import__('bs4')
        self.string = __import__('string')
        self.random = __import__('random')
        self.requests = __import__('requests')
        self.json = __import__('json')
        self.io = __import__('io')

        """ Loads JSON object """
        self.__filename = archivename
        self.__getsites()
        pass


    def generate(self, astring, checksite=False):
        """ Generates a short version for a string """
        title = ""
        timestamp = self.datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")
        # If need to download URL...
        if checksite:
            try:
                resp = self.requests.get(astring).text
                title = self.bs4.BeautifulSoup(resp).title.text
            except self.requests.exceptions.RequestException, e:
                raise PyShort.SiteConnectionError()
            except AttributeError, e:
                raise PyShort.HtmlParsingError()
            except Exception, e:
                print e

        # Create the site
        exists = self.__checkexists(astring)
        out = exists
        if (exists == ""):
            rnd = self.__random()
            site = {'url':astring, 'short':rnd,'title':title,'created':timestamp}
            self.__sites.append(site)
            self.__savesites()
            out = rnd 
        return [out,title]



