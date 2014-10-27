from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from feed.models import FeedItem

@login_required
def home(request):
    """
    User's home.
    """
    context = {
        "feed_list": None,
        "feed_title": "",
    }

    pfilter = request.GET.get("filter")
    if pfilter == "tracking":
        # Posts of everyone I'm tracking plus my own posts.
        context["feed_list"] = (FeedItem.objects.filter(user_id=request.user.id) | FeedItem.objects.filter(user__registereduser__tracks__user=request.user.id)).distinct()
        context["feed_title"] = _("Me and I'm tracking posts")
    elif pfilter == "all":
        # Everyone's posts (including my posts)
        context["feed_list"] = FeedItem.objects.all()
        context["feed_title"] = _("Everyone's posts")
    else:
        # (default) My posts
        context["feed_list"] = FeedItem.objects.filter(user_id=request.user.id)
        context["feed_title"] = _("My posts")

    return render(request, "feed/home.html", context)
