## In this Repository, we have used django-oauth-toolkit for authentication

1. Install with pip:

```
pip install django-oauth-toolkit
```

2. Add oauth2_provider to your INSTALLED_APPS

```
INSTALLED_APPS = (
    ...
    'oauth2_provider',
)
```

3. If you need an OAuth2 provider you’ll want to add the following to your urls.py. Notice that oauth2_provider namespace is mandatory.

```
urlpatterns = [
   path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')), 
]
```

## This repo is also on docker hub, just need to take pull and start the container
```
docker pull kumarm5/django_oauth
```

## start the container in the background
```
docker run -d -p 8000:8000 kumarm5/django_oauth
```

## To check container, just type command
```
docker container ls
```