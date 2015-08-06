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

__astring__: is the string/url you want to shorten;
__checksite__: is True if you want to get the site title, False by default

The class raises the following errors:

__myshort.SiteConnectionError__: if _checksite_  _==_  _True_ and the script cannot connect to the url;
__myshort.HtmlParsingError__: if _checksite_  _==_  _True_ and the script cannot parse the result page;

