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