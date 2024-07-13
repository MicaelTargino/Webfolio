from django.db import models



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

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    style = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    link = models.URLField()
    style = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    style = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


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