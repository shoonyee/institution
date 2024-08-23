# create Django + Vue (one vue app)

### Create Virtual Enviroment and Django Project
```
virtualenv django-vue
cd django-vue
source bin/activate
```
```
pip3 install django
```
```
django-admin startproject institution
cd institution
```

```
pip3 install django-webpack-loader
pip3 install pytz
```

### Run Django 
```
python manage.py migrate
```
you can run the following command, and visit http://127.0.0.1:8000 
```
python manage.py runserver
```

### Mapping URLs and folders
#### _institution/settings.py_, add the following lines after BASE_DIR: 
```
TEMPLATES_DIR = BASE_DIR / 'templates'
FRONTEND_DIR = BASE_DIR / 'vueapp')
```
#### update TEMPLATES
```
TEMPLATES = [    
    {        
        'BACKEND': 
        'django.template.backends.django.DjangoTemplates',        
        'DIRS': [TEMPLATES_DIR,],        
        'APP_DIRS': True,        
        'OPTIONS': {            
        'context_processors': 
            [ 
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth', 
                'django.contrib.messages.context_processors.messages', 
            ],
        },
    },
]
```
#### Create templates
Create _templates_ folder in the root directory
Create _application.html_ file in the template directory
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <link rel="icon" href="<%= BASE_URL %>favicon.ico">
    <title>Django Vue Integration</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Material+Icons">
  </head>
  <body>
    <noscript>
      <strong>We're sorry but frontend doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
    </noscript><div id="app">
     <app></app>
 </div>{% render_bundle 'app' %}<!-- built files will be auto injected -->
  </body>
</html>
```
#### map the url to our vue application in _urls.py_ 
```python
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateViewurlpatterns = [
    path('admin/', admin.site.urls),
    path("",
        TemplateView.as_view(template_name="application.html"),
        name="app",
    ),
]
```

### Vue app
#### create vueapp
```
vue create vueapp
```
#### install webpack bundle tracker
```
cd vueapp
npm install --save-dev webpack-bundle-tracker
```

### Configuring webpack and devServer
#### update _vue.config.js_
```javascript
const { defineConfig } = require('@vue/cli-service')
const BundleTracker = require('webpack-bundle-tracker')

module.exports = defineConfig({
  publicPath: process.env.NODE_ENV === 'production' ? '/static/dist/' : 'http://localhost:8080',
  outputDir: '../static/dist',
  indexPath: '../templates/index.html',
  transpileDependencies: true,
  configureWebpack: {
    plugins: [
      new BundleTracker({ path: __dirname, filename: 'webpack-stats.json' }),
    ],
  },
})
```
we’re configuring the bundle tracker plugin to generate the _webpack-stats.json_ in the project frontend folder. This is where the WEBPACK_LOADER config in settings.py should point to.
#### add to settings
Django will try to find static files from here:
```javascript
STATICFILES_DIRS = [
  BASE_DIR / "static",
]
```