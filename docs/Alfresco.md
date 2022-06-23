# Intro

Alfresco is an open source sofware that helps you with the information management.

For more information visit: https://www.alfresco.com/



# How to obtain information

### Search
There are several ways to make a search in Alfresco, whether using queries, solr or 
by the API base endpoint to find sites, folders and files by a term. 

In these project the search query is used, and the language the query uses is `afts` (Alfresco Full Text Search), others
can be used such as `cmis`, `lucene`.

In order to do a search, a session and a query is needed (These are the parameters) and the output will be a dictionary 
containing the response of the query.

### Example

**Session**
```
import requests

session = requests.Session()
session.headers.update({'x-api-key': ALFRESCO_API_KEY})
```

**Search query**

In this example we are requesting the files that share the type `sipecam:image`and also has the 
property `sipecam:CumulusName:92`. In summary, we are searching for the images on the 92 cumulus.
```
query =  "+TYPE: \"sipecam:image\" AND (sipecam:CumulusName:\"92\")"
```

**Obtain results**
```
req = session.post(
        config.get("ALFRESCO_API_ENDPOINT"),
        data=json.dumps({
            "query": {
                "query": query,
                "language": "afts"
            },
            "include": ["properties", "path"],
            "sort": [{"type": "FIELD", "field": "cm:name", "ascending": "false"}],
        })
    )

result = req.json()
```
