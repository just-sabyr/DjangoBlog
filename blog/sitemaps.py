from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from taggit.models import Tag
from .models import Post



class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()
    
    def lastmod(self, obj):
        return obj.updated
    

class TagSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        # Return all tags used in the blog
        return Tag.objects.all()
    
    def location(self, item):
        # Generate the URL for each tag
        return reverse('blog:post_list_by_tag', args=[item.slug])