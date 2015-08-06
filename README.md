#pyshort

This is a simple class for string/url shortening.

It saves the string on a local json file passed to the class via the constructor.

For this design concern, it's not intended to be used in a production environment.

##How to use

First import

```
import pyshort
```

Then create the instance specifying the json file you want to use to store the data:

```
myshort = pyshort("sites_archive.json")
```

And last create the shortening:

```
shorten, title = myshort.generate(astring="http://www.gianlucanieri.com",checksite=False)
```

Note that:

_astring_: is the string/url you want to shorten;
_checksite_: is True if you want to get the site title, False by default

The class raises the following errors:

_myshort.SiteConnectionError_: if __checksite__  __==__  __True__ and the script cannot connect to the url;
_myshort.HtmlParsingError_I if __checksite__  __==__  __True__ and the script cannot parse the result page;

