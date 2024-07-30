from django.contrib import admin
from .models import Hero, Section, ContactItem, Contact, Portfolio, PortfolioItem, Skills, SkillsTopic, SkillItem, CV, About, Aside, AsideLink, ThemeColors
# Register your models here.
# admin.site.register(User)
# admin.site.register(Style)

admin.site.register(Section)


admin.site.register(CV)

admin.site.register(ThemeColors)

admin.site.register(Aside)
admin.site.register(AsideLink)

admin.site.register(Hero)

admin.site.register(About)

admin.site.register(ContactItem)
admin.site.register(Contact)

admin.site.register(PortfolioItem)
admin.site.register(Portfolio)

admin.site.register(Skills)
admin.site.register(SkillsTopic)
admin.site.register(SkillItem)