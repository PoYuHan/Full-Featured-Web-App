## Shell Things
from blog.models import Post
from django.contrib.auth.models import User

### Query the user with SQL-like command
user = User.objects.get(id = 1)


### Add post with Post object
post_1 = Post(title='Blog 1', content = 'First Post Content!', author = user)

Then save to the database

post_1.save()



## Register model to admin page to control
1. Go to the admin.py under the app. (i.e. app blog)
2. import the 'object' from the models.py
3. admin.site.register('object')