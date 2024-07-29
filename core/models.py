from PIL import Image
from django.db import models
from django.core.exceptions import ValidationError

    
class Section(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class ContactItem(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=False, blank=False, default="username")
    link = models.CharField(max_length=255, null=True, blank=True)
    logo_file = models.ImageField(upload_to='static/core/contactlogos/', null=True, blank=True)
    logo_url = models.URLField(max_length=1024, null=True, blank=True)
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    section = models.OneToOneField(Section, on_delete=models.CASCADE, primary_key=True)
    title1 = models.CharField(max_length=255, null=True, blank=True)
    subtitle1 = models.CharField(max_length=255, null=True, blank=True)
    title2 = models.CharField(max_length=255, null=True, blank=True)
    subtitle2 = models.CharField(max_length=255, null=True, blank=True)
    contacts = models.ManyToManyField(ContactItem, blank=True)

    def __str__(self):
        return self.section.title

    

class CV(models.Model):
    cv = models.ImageField(upload_to='static/core/cv/')

    def __str__(self):
        return self.cv.name
    
# def validate_labels(value):
#     if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
#         raise ValidationError('Labels must be a list of strings.')
    
class Hero(models.Model):
    section = models.OneToOneField(Section, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False, default="<YOUR NAME HERE>")
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    # labels = models.JSONField(validators=[validate_labels], default=['Programmer'])
    labels = models.CharField(max_length=255, default='Programmer')
    slogan = models.CharField(max_length=512, null=False, blank=False)
    contacts = models.ManyToManyField(ContactItem, blank=True)
    link_to_section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="hero_link_to_section")
    cv = models.ForeignKey(CV, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='static/core/me/', blank=True, null=True)

    def __str__(self):
        return self.section.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    

        img = Image.open(self.image.path)

        max_width = 330
        max_height = 400

        if img.height > max_height or img.width > max_width:
            print('resizing image')
            output_size = (max_width, max_height)
            img.thumbnail(output_size)
            img.save(self.image.path)

class AsideLink(models.Model):
    name = models.CharField(max_length=99, default="<LINK NAME HERE>")
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="aside_link_to_section")

    def __str__(self): 
        return self.section.title

class Aside(models.Model):
    section = models.OneToOneField(Section, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=6, null=True, blank=True)
    links = models.ManyToManyField(AsideLink, blank=True)

    def __str__(self):
        return self.section.title
    

# class Style(models.Model):
#     name = models.CharField(max_length=100)
#     primary_color = models.CharField(max_length=8, null=True, blank=True)
#     # custom_css = models.TextField(null=True, blank=True)
#     secondary_color = models.CharField(max_length=8, null=True, blank=True)
#     terciary_color = models.CharField(max_length=8, null=True, blank=True)
#     dark_mode = models.BooleanField(default=True)
#     white = models.CharField(max_length=8, null=True, blank=True, default="#fff")
#     logo = models.FileField(null=True, blank=True)
#     favicon = models.FileField(null=True, blank=True)
#     hero_image = models.FileField(null=True, blank=True)

#     def __str__(self):
#         return self.name
    
# class CV():
#     title = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='CV/')


class About(models.Model):
    section = models.OneToOneField(Section, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=99, null=True, blank=True)
    content = models.TextField()
    cv = models.ForeignKey(CV, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.section.title

class SkillItem(models.Model):
    name = models.CharField(max_length=16, null=True, blank=True)
    image = models.FileField(upload_to='static/core/skills')

    def __str__(self):
        return self.name

class SkillsTopic(models.Model):
    title = models.CharField(max_length=99, null=False, blank=False)
    skills_items = models.ManyToManyField(SkillItem, null=False, blank=False) 

    def __str__(self):
        return self.title   

class Skills(models.Model):
    section = models.OneToOneField(Section, on_delete=models.CASCADE, primary_key=True)
    topics = models.ManyToManyField(SkillsTopic, blank=False)

    def __str__(self):
        return self.section.title

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=96)
    image = models.ImageField(upload_to='static/core/portfolio_images/')
    repo_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    section = models.OneToOneField(Section, on_delete=models.CASCADE, primary_key=True)
    projects = models.ManyToManyField(PortfolioItem, blank=True)

    def __str__(self):
        return self.section.title


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