from django.db import models
from django.core.exceptions import ValidationError

# def validate_labels(value):
#     if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
#         raise ValidationError('Labels must be a list of strings.')
    
class Section(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Hero(models.Model):
    section = models.OneToOneField(Section, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False, default="<YOUR NAME HERE>")
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    # labels = models.JSONField(validators=[validate_labels], default=['Programmer'])
    labels = models.CharField(max_length=255, default='Programmer')
    slogan = models.CharField(max_length=512, null=False, blank=False)
    contacts = models.ManyToManyField(Contact, blank=True)
    cv = models.ImageField(upload_to='static/core/cv/')
    link_to_section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='professionals')
    image = models.ImageField(upload_to='static/core/me/', blank=True, null=True)

    def __str__(self):
        return self.section.title
    

class Style(models.Model):
    name = models.CharField(max_length=100)
    primary_color = models.CharField(max_length=8, null=True, blank=True)
    # custom_css = models.TextField(null=True, blank=True)
    secondary_color = models.CharField(max_length=8, null=True, blank=True)
    terciary_color = models.CharField(max_length=8, null=True, blank=True)
    dark_mode = models.BooleanField(default=True)
    white = models.CharField(max_length=8, null=True, blank=True, default="#fff")
    logo = models.FileField(null=True, blank=True)
    favicon = models.FileField(null=True, blank=True)
    hero_image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name
    
# class CV():
#     title = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='CV/')


# class About(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()

#     def __str__(self):
#         return self.title

# class PortfolioItem(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     image = models.ImageField(upload_to='portfolio_images/')
#     link = models.URLField()
#     style = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return self.title

# class Contact(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     style = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return self.name


# class Style(models.Model):
#     name = models.CharField(max_length=100)

#     primary = models.CharField(max_length=8, null=True, blank=True)

#     custom_css = models.TextField(null=True, blank=True)

#     secondary = models.CharField(max_length=8, null=True, blank=True)

#     terciary = models.CharField(max_length=8, null=True, blank=True)

#     white = models.CharField(max_length=8, null=True, blank=True, default="#fff")

#     logo = models.FileField(null=True, blank=True)

#     favicon = models.FileField(
#         null=True, blank=True, storage=storage.staticfiles_storage
#     )

#     hero_image = models.FileField(
#         null=True, blank=True, storage=storage.staticfiles_storage
#     )