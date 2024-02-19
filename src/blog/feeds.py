from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "Latest blog posts from Marcel Aguiar (marcelaguiar.com)"
    link = "/blog/"
    description = "Latest blog posts from Marcel Aguiar (marcelaguiar.com)"

    def items(self):
        return Post.objects.order_by("-created")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse("blog-post", args=[item.pk, item.slug])
