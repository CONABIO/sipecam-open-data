## How to mount webdav in your local

If you are working with Linux, add your variables:

```
IP_ALFRESCO="api.conabio.gob.mx"
ALFRESCO_PASSWORD_WEBDAV=<password alfresco webdav>
ALFRESCO_USER_WEBDAV=<user alfresco webdav>
ENDPOINT_ALFRESCO_WEBDAV=/alfresco/webdav
```

Update 
````
sudo apt-get update
````

Install Alfresco webdav

```
sudo apt-get install -y davfs2
```

Add secrets
```
sudo echo "http://$(echo $IP_ALFRESCO)/alfresco/webdav $ALFRESCO_USER_WEBDAV $ALFRESCO_PASSWORD_WEBDAV" >> /etc/davfs2/secrets
```

Create shared_volume folder
```
sudo mkdir /shared_volume
```

Mount 
```
sudo cd /shared_volume && sudo mkdir webdav_alfresco && sudo mount -t davfs http://$(echo $IP_ALFRESCO$ENDPOINT_ALFRESCO_WEBDAV) webdav_alfresco
```


## Notes
If you have any problem o question, feel free to contact us.
